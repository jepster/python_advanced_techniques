# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

a = map(len, ["apple", "orange", "pear"])
aResult = list(a)
b = map(str.upper, ["apple", "orange", "pear"])
bResult = list(b)
c = map(lambda text: text[::-1], ["apple", "orange", "pear"])
cResult = list(c)
d = map(lambda text: text[:2], ["apple", "orange", "pear"])
dResult = list(d)


# Practice with filter
# Fill out the rest of the filter functions.
# You can define additional functions if you need to.
# (a) range(100) => (0, 3, 6, 9, ...)  (div by 3)
# (b) range(100) => (0, 5, 10, 15, ...)  (div by 5)
# (c) range(100) => (0, 15, 30, 45, ...)  (div by 15)
# (d) range(100) => (1, 2, 4, 7, 8, 11, 13, 14)  (not div by 3 and not div by 5)

aFilter = filter(lambda item: item % 3 == 0, range(100))
aFilterResult = list(aFilter)
bFilter = filter(lambda item: item % 5 == 0, range(100))
bFilterResult = list(bFilter)
cFilter = filter(lambda item: item % 15 == 0, range(100))
cFilterResult = list(cFilter)
dFilter = filter(lambda item: item % 3 != 0 and item % 5 != 0, range(100))
dFilterResult = list(dFilter)