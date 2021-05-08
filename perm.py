import string
import itertools

file1 = open("perm_wordlist.txt","w");
for x in itertools.product('abcdefghijklmnopqrst', repeat=5):
    y= ''.join(x)
    file1.write(y)
    file1.write("\n")
file1.close()
