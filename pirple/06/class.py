#sets = { "element1", "element2", "element1" } 

# we CAN'T have repeating elements. doesn't care about the order. we care if it's there or not

#print(sets)

#if "element1" in sets:
#    print("yes")

countrylist = []

for i in range(5):
    country = input("escribí un país: ")
    countrylist.append(country)

countryset = set(countrylist)

#print("list: ",countrylist)
#print("set: ",countryset)

# dictionaries

#dictionary = { "key": "value", "key2": "value" }

#
countryDictionary = {}

for country in countrylist:
    if country in countryDictionary:
        countryDictionary[country] += 1
    else:
        countryDictionary[country] = 1 

print(countryDictionary)
