import re
from functools import reduce
from itertools import takewhile

def mapFn(mapping):
    (dest, src, n) = [int(i) for i in re.findall('\d+',mapping)]
    return lambda s: dest+s-src if (s>=src and s<src+n) else None

def parseMaps(acc,mapping):
    if mapping=='':
        return acc
    
    name = re.match('(.*) map:', mapping)
    if name:
        acc['current']=name[1]
        acc[name[1]]=[]
    else:
        acc[acc['current']].append(mapFn(mapping))
    return acc

def seedToLocation(seed, mappings):
    return reduce(lambda n,key: next((fn(n) for fn in mappings[key] if fn(n) is not None), n),
                  ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature','temperature-to-humidity','humidity-to-location'],
                  seed)

input = open('day5/sample.txt','r')
# input = open('day5/input.txt','r')
(seeds,_,*ms) = input.read().splitlines()
mappings = reduce(parseMaps, ms, {})

# part1
min([seedToLocation(int(s),mappings) for s in re.findall('\d+',seeds)])

# part2
# reverse part1. start with lowest location and map back to seed using lambdas
def mapRevFn(mapping):
    (src, dest, n) = [int(i) for i in re.findall('\d+',mapping)]
    return lambda s: dest+s-src if (s>=src and s<src+n) else None

def parseRevMaps(acc,mapping):
    if mapping=='':
        return acc
    
    name = re.match('(.*) map:', mapping)
    if name:
        acc['current']=name[1]
        acc[name[1]]=[]
    else:
        acc[acc['current']].append(mapRevFn(mapping))
    return acc

def locationToSeed(loc, mappings):
    return reduce(lambda n,key: next((fn(n) for fn in mappings[key] if fn(n) is not None), n),
                  reversed(['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature','temperature-to-humidity','humidity-to-location']),
                  loc)

# input = open('day5/sample.txt','r')
input = open('day5/input.txt','r')
(seeds,_,*ms) = input.read().splitlines()
rmappings = reduce(parseRevMaps, ms, {})

def seedRangeFn(rs):
    (start,n) = rs.split(' ')
    return lambda s: s>=int(start) and s<int(start)+int(n)

def buildSeedRanges(seeds):
    result = []
    for rs in re.findall('\d+ \d+', seeds):
        result.append(seedRangeFn(rs))
    return result

seedRanges = buildSeedRanges(seeds)

location = 0
seed = 0
while True:
    seed = locationToSeed(location,rmappings)
    if any(rFn(seed) for rFn in seedRanges):
        print(location,seed)
        break
    location+=1