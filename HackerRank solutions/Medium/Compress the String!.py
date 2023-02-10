from itertools import groupby
string=input()
for key,groups in groupby(string):
    print((len(list(groups)),int(key)), end = " ")