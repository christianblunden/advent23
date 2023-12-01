from functools import reduce
import re

input = open('day1/sample2.txt','r')
input = open('day1/input.txt','r')

def part1(lines):
    digits = [re.findall('\d', l.strip()) for l in lines]
    return sum([int(d[0]+d[-1]) for d in digits])

part1(input.readlines())

def part2(x):
   replacements = {
       "one":"one1one",
       "two":"two2two",
       "three":"three3three",
       "four":"four4four",
       "five":"five5five",
       "six":"six6six",
       "seven":"seven7seven",
       "eight":"eight8eight",
       "nine":"nine9nine",
   }

   return reduce(lambda result,i: result.replace(i,replacements[i]), replacements.keys(), x)

part1([part2(l) for l in input.readlines()])