# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5
 
# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def is_word_in(self, text):
        """
        Returns True if self.word presents in the
        given argument text, or False otherwise.
        Noticed that this method should NOT be 
        case-sensitive.
        """
        word_list = []
        word = ''
        for c in text.lower():
            if c in string.punctuation or c == ' ':
##                print "will append: " + word
                word_list.append(word)
                word = ''
            else:
                word += c
        if len(word) != 0:
            word_list.append(word)
##        print self.word, "; word_list", word_list
        if self.word.lower() in word_list:
            return True
        else:
            return False

############ SELF TEST  
##word = 'soft'
##text1 = "microsoft go!"
##text2 = "this is soft"
##w = WordTrigger(word)
##print w.is_word_in(text1)
##print w.is_word_in(text2)
##############
        
# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def __init__(self, title):
        self.word = title
    def evaluate(self, story):
        return WordTrigger.is_word_in(self, story.title)

    
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def __init__(self, subject):
        self.word = subject
    def evaluate(self, story):
        return WordTrigger.is_word_in(self, story.subject)


# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def __init__(self, summary):
        self.word = summary
    def evaluate(self, story):
        return WordTrigger.is_word_in(self, story.summary)

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2
    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def evaluate(self, story):
        if self.word in story.title:
            return True
        elif self.word in story.subject:
            return True
        elif self.word in story.summary:
            return True
        else:
            return False

#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel freeto change this line!
    results = []
    for s in stories:
        for t in triggerlist:
            if t.evaluate(s):
                results.append(s)
    return results

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    triggers = []
    trigger_dict = {}
    index = 1   #trigger index
    for single_line in lines:
        word_list = []
        word = ''
        for char in single_line:
            if char in string.punctuation or char == ' ':
                word_list.append(word)
                word = ''
            else:
                word += char
        word_list.append(word)
        word = ''
        print "word_list", word_list
        if word_list[1] == "AND":
            t1 = trigger_dict[word_list[2]]
            t2 = trigger_dict[word_list[3]]
            t = AndTrigger(t1, t2)
            trigger_dict[word_list[0]] = t
        elif word_list[1] == "OR":
            t1 = trigger_dict[word_list[2]]
            t2 = trigger_dict[word_list[3]]
            trigger_dict[word_list[0]] = OrTrigger(t1, t2)
        elif word_list[1] == "NOT":
            t = trigger_dict[word_list[1]]
        elif word_list[0] == "ADD":
            for i in range(1, len(word_list)):
                t = trigger_dict[word_list[i]]
                triggers.append(t)
        else:
            if word_list[1] == "TITLE":
                t = TitleTrigger(word_list[2])
                trigger_dict[word_list[0]] = t
            elif word_list[1] == "SUBJECT":
                t = SubjectTrigger(word_list[2])
                trigger_dict[word_list[0]] = t
            elif word_list[1] == "PHRASE":
                phrase = ''
                for i in range(2, len(word_list)):
                    if i == len(word_list):
                        phrase += word_list[i]
                    else:
                        phrase += word_list[i] + " "
                t = PhraseTrigger(phrase)
                trigger_dict[word_list[0]] = t
            elif word_list[1] == "SUMMARY":
                t =  SummaryTrigger(word_list[2])
                trigger_dict[word_list[0]] = t
            else:
                raise TypeError("config file error!")
    
    return triggers
            


### SELF TEST
##readTriggerConfig("triggers.txt")
            
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
##    t1 = SubjectTrigger("Obama")
##    t2 = SummaryTrigger("MIT")
##    t3 = PhraseTrigger("Supreme Court")
##    t4 = OrTrigger(t2, t3)
##    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print("Polling...")

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print("Sleeping...")
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

