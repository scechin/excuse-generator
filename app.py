import random
import math

# your code here

excuse = 'The dog eat my homework when I finished'
who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broked']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']


def getrandomnumber():
    return random.randint(0, 2)

print(who[getrandomnumber()] + " " + what[getrandomnumber()] + " " + when[getrandomnumber()])
