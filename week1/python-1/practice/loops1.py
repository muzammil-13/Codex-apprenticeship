# for i in range(1,14,2):
#     print(i)

import random

tops=[
    "Red Shirt", 
    "Blue Tshirt", 
    "Black Hoodie", 
    "Green Polo", 
    "White Sweater"
]
print("Tops: ",tops)

pants=[
    "Blue Jeans", 
    "Black Formal Pants", 
    "Grey Track Pants", 
    "Brown Chinos", 
    "White Shorts"
]
print("Pants: ",pants)

print("All possible outfits")

outfits=[]
for i in tops:
    for j in pants:
        outfit=f"{i} + {j}"
        outfits.append(outfit)
        # print(outfits)

random_outfits=random.sample(outfits, 5)
for outfit in random_outfits:
    print("random picks:", outfit)
