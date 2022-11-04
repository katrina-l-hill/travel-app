import random

location_list = [
    "Lisbon",
    "Madrid",
    "Tokyo",
    "Munich",
    "Paris",
    "Auckland",
    "Sydney",
    "Seoul",
    "Göbekli Tepe",
    "Nan Madol",
    "Newgrange",
    "Skellig Islands",
    "Oslo",
    "Brussels",
]

# https://pynative.com/python-random-choice/

# print(location)

# x = len(location)
# print(x)

# for x in location:
#     print(x)

print(random.choice(location_list))

# i = random.randrange(len(location_list))
# item = location_list[i]
# print("Randomly selected item", location_list[i], "is present at index:", i)
