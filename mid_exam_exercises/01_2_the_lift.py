people = int(input())
current_wagons = [int(x) for x in input().split()]

max_people_in_wagon = 4

for i in range(len(current_wagons)):
    max_people = min(max_people_in_wagon - current_wagons[i], people)
    current_wagons[i] += max_people
    people -= max_people

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif any([wagon < max_people_in_wagon for wagon in current_wagons]):
    print("The lift has empty spots!")

print(*current_wagons)
