from ps4 import *

def find_best_shifts(wordlist, text):
    print("now find on \'" + text + "\'") 
    shifts = []
    s = 0
    for i in range(27):
        temp_text = apply_shift(text[s:], -i)
        print("i=" + str(i) + " temp_text:\'" + temp_text + "\' s=" + str(s))
        if ' ' not in temp_text and is_word(wordlist, temp_text):
            return [(s, i), ]
        elif ' ' in temp_text:
            index = temp_text.find(' ')
            word = temp_text[s: index]
            if is_word(wordlist, word):
                shifts += [(s, i), ]
                s += index + 1
                shifts += find_best_shifts_rec(wordlist, temp_text[s:], s)
            return shifts


##s = random_scrambled(wordlist, 3)
##s = 'eqorqukvqtbmultiform wyy ion'

##s1 = "life good"
##s2 = "life good right"
##shift1 = [(0, 2), (5, 3)]
##shift2 = [(0, 2), (5, 3), (10, 1)]
####s = apply_shifts(s1, shift1)
##s = apply_shifts(s2, shift2)
##print("s:", s)
##shifts = find_best_shifts(wordlist, s)
##print("result:", shifts)

