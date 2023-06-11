food_gr = float(input()) * 1000
hay_gr = float(input()) * 1000
cover_gr = float(input()) * 1000
pig_weight_gr = float(input()) * 1000

# month = 30 days       hay = food * 0.05    cover = pig_weight / 3
day = 0

for i in range(1, 31):
    day += 1
    food_gr -= 300
    if day % 2 == 0:
        hay_gr -= food_gr * 0.05
    if day % 3 == 0:
        cover_gr -= pig_weight_gr / 3

if day == 30 and (food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0):
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: "
          f"{food_gr / 1000:.2f}, Hay: {hay_gr / 1000:.2f}, Cover: {cover_gr / 1000:.2f}.")
