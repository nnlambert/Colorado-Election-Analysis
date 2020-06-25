'''print("Hello World")
print(5+2*3)
print(8//5-3)
print(8+22*2-4)
print(16-3/2+7-1)
print(3**3%5)
print(5+9*3/2-4)
print("Space")
print((5+2)*3)
print((8//5)-3)
print(8+(22*(2-4)))
print(16-3/(2+7)-1)
print(3**(3%5))
print(5+(9*3/(2-4)))'''

'''counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())'''

'''counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
'''
'''import datetime
now = datetime.datetime.now()
#print the present time.
print("The time right now is,", now)'''

'''
#Iterating through a list that takes inputs and correcting the case
#based on the name appearance
a = input("Friend 1 :")
b = input("Friend 2 :")
c = input("Friend 3 :")
d = input("Friend 4 :")
e = input("Friend 5 :")

#fl = ["NICK", "NICHOLAS", "NICOLAI", "NICO", "NICS"]
friend_list = [a,b,c,d,e]
friend_list_low = []
friend_list_correct = []

for i in friend_list:
    friend_list_low.append(i.lower())

for i in friend_list_low:
    friend_list_correct.append(i.title())

print(friend_list_correct)
'''

# define the function to take the average
def average(list):

    # lets get the total
    sum = 0

    # get the length of the list to get a divisor
    divisor = len(list)

    # iterate through list to add to our sum
    for i in list:
        sum += i

    #take the average
    avg = int(sum) / int(divisor)

    # magic average
    return avg

# creating lists for testing
list_1 = [90,80,70,60,50]
l2 = [1,2,3,4,5]
l3 = [12,46,12,13,90,13,12]

# lets see if it works
print(average(list_1))
print(average(l2))
print(average(l3))