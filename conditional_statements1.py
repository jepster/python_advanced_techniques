points = 174  # use this input to make your submission

# write your if statement here

prize = False

if points >=1 and points <= 50:
    result = "wooden rabbit"
    prize = True
elif points >= 51 and points <= 150:
    prize = False
elif points >= 151 and points <= 180:
    result = "wafer-thin mint"
    prize = True
elif points >= 181 and points <= 200:
    result = "penguin"
    prize = True

if prize == True:
    print("Congratulations! You won a {prize}!".format(prize=result))
else:
    result = "Oh dear, no prize this time."


for i in range(5, 35, 4):
    print(i)


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
newUsernames = []

# write your for loop here

for username in usernames:
    username = username.lower().replace(' ', '_')
    newUsernames.append(username)

print(newUsernames)