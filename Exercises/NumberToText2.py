#example

#                       ten=0   ten=1     tens=2
#
one2hundred_dict = {0: ('Zero', 'Ten'),
                    1: ('One', 'Eleven'),
                    2: ('Two', 'Twelve', 'Twenty'),
                    3: ('Three', 'thirteen', 'Thirty'),
                    4: ('Four', 'Fourteen', 'Forty'),
                    5: ('Five', 'Fifteen', 'fifty'),
                    6: ('six', 'sixteen', 'sixty'),
                    7: ('seven', 'seventeen', 'seventy'),
                    8: ('eight', 'eighteen', 'eighty'),
                    9: ('nine', 'nineteen', 'ninety')}

                    #...

def two_digits(str_num):
    if len(str_num) == 1:
        ones = int(str_num[0])    # ones = rows
        tens = 0                  # tens = columns
    else:
        tens = int(str_num[0])
        ones = int(str_num[1])
    if tens == 0 or tens == 1:
        return one2hundred_dict[ones][tens]
    else:
        word = one2hundred_dict[tens][2]
        word += ' ' + one2hundred_dict[ones][0]
        return word

def three_digits(str_num):
    hundreds = int(str_num[0])
    if hundreds == 0:
        return two_digits((str_num)[-2:])
    tens_ones = str_num[1:]
    word = one2hundred_dict[hundreds][0] + ' ' + 'Hundred'
    if tens_ones != '00':
        word += ' ' + two_digits(tens_ones)
    return word

word_list = ['','Thousand','Million','Billion']

while True:
    num = input("Type in a number: ")
    print(num)
    Words = ''
    if num == '0':
        Words = one2hundred_dict[0][0]
    else:
        while len(num) > 0:
            while num[0] == '0':
                num = num[1:]
            indx = int((len(num) -1) / 3)
            pos = len(num) % 3
            if pos == 0:
                pos = 3
                word = three_digits(num[:pos]) + ' ' + word_list[indx]
            else:
                word = two_digits(num[:pos]) + ' ' + word_list[indx]
            if Words:
                Words += ' ' + word
            else:
                Words = word
            num = num[pos:]
    print(Words)
print
