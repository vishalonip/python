from random import randint

choice = ["a", "b", "c", "d", "e", "f", "g", "h"]
numb = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
Symb = ["!", "£", "$","%", "^", "&", "*", "(", ")", "_", "-" ]

c1 = choice[randint(0,7)].lower()
print(c1)
c2 = choice[randint(0,7)].upper()
print(c2)
c3 = numb[randint(0,9)]
print(c3)
c4 = Symb[randint(0,10)]
print(c4)