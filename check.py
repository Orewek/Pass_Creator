import heapq
from collections import namedtuple

# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
# print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]


# line = 'asdf fjdk; afed, fjek,asdf, foo'
# import re
# res = re.split(r'[;,\s]\s*', line)
# print(res)

# from fnmatch import fnmatch, fnmatchcase
# print(fnmatch('foo.txt', '*.txt'))
# print(fnmatch('foo.txt', '?oo.txt'))
# print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
# names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
# print([name for name in names if fnmatch(name, 'Dat*.csv')])

# text.rjust(20,'=')
# text.center(20,'*')
# format(text, '<20')
# '{:>10s} {:>10s}'.format('Hello', 'World')

# s = '{name} has {n} messages.'
# s.format(name='Guido', n=37)

# name = 'Guido'
# n = 37
# print(sub('Hello {name}'))
# Hello Guido
# print(sub('You have {n} messages.'))
# You have 37 messages.
# print(sub('Your favorite color is {color}'))
# Your favorite color is {color}


# print(textwrap.fill(s, 40))
# Look into my eyes, look into my eyes,
# the eyes, the eyes, the eyes, not around
# the eyes, don't look around the eyes,
# look into my eyes, you're under.

# format(x, 'e')
# '1.234568e+03'
# format(x, '0.2E')
# '1.23E+03
# 'The value is {:0,.2f}'.format(x)
# 'The value is 1,234.57'


# from fractions import Fraction
# a = Fraction(5, 4)
# b = Fraction(7, 16)
# print(a + b)
# 27/16
# print(a * b)
# 35/64


# headers = ['Symbol','Price','Date','Time','Change','Volume']
# rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
#        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
#        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
#        ]
# with open('stocks.csv','w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)


# import json
# data = {
#     'name' : 'ACME',
#     'shares' : 100,
#     'price' : 542.23
# }
# json_str = json.dumps(data)