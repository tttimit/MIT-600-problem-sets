from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_comment(self, data):
        print('<!-- %s -->' % data)

    def handle_charref(self, name):
        print('!!&#%s;' % name)

    def handle_entityref(self, name):
        print('##&%s;' % name)

    def handle_data(self, data):
        print(data)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
