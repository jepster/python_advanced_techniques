# Write your code here

# HINT: create a dictionary from flowers.txt
flowersTextfile = open('flowers.txt', 'r')
flowersTextfileLines = flowersTextfile.readlines()

flowersDictionary = {}

for flowerLine in flowersTextfileLines:
    key, value = flowerLine.split(': ')
    flowersDictionary[key] = str(value).replace('\n', '')

# HINT: create a function to ask for user's first and last name
firstAndLastName = input('Enter your First [space] Last name only:')

while firstAndLastName != '':
    firstNameFromUserInput = firstAndLastName.split(' ')
    firstCharacterOfFirstname = firstNameFromUserInput[0][0]
    print(flowersDictionary[firstCharacterOfFirstname])
    tryMore = input('Would you like to try more? Type "yes" or "no".')
    if tryMore == 'no':
        break
    else:
        firstAndLastName = input('Enter your First [space] Last name only:')

# print the desired output