from ps4 import *

def find_best_shifts(wordlist, text):
    print("now find on \'" + text + "\'") 
    shifts = []
    s = 0
    for i in range(27):
        temp_text = apply_shift(text[s:], -i)
        print("i=" + str(i) + " temp_text:\'" + temp_text + "\' s=" + str(s))
        if temp_text == ' ' or len(temp_text) == 0:
            break
        elif ' ' not in temp_text and is_word(wordlist, temp_text):
            shifts += [(s, i), ]
            break
        else:
            index = temp_text.find(' ')
            word = temp_text[s: index]
            if is_word(wordlist, word):
                shifts += [(s, i), ]
                s += index + 1
                shift = find_best_shifts(wordlist, temp_text[s:])
                shifts += [(shift[0][0] + s, shift[0][1]), ]
    return shifts


##s = random_scrambled(wordlist, 3)
##s = 'eqorqukvqtbmultiform wyy ion'

s1 = "life good"
s2 = "life good right"
shift1 = [(0, 2), (5, 3)]
shift2 = [(0, 2), (5, 3), (10, 1)]
s = apply_shifts(s1, shift1)
##s = apply_shifts(s2, shift2)
print("s:", s)
shifts = find_best_shifts(wordlist, s)
print("result:", shifts)
