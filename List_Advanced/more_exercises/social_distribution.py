def distribution_of_wealth(people, minimum_wealth):
    for current_man_wealth in people:
        the_richest = max(people)
        if current_man_wealth < minimum_wealth:
            current_man_index = people.index(current_man_wealth)
            the_richest_index = people.index(the_richest)
            difference = minimum_wealth - current_man_wealth
            current_man_wealth += difference
            people.insert(current_man_index + 1, current_man_wealth)
            people.pop(current_man_index)
            the_richest -= difference
            people.insert(the_richest_index + 1, the_richest)
            people.pop(the_richest_index)
        if the_richest < minimum_wealth:
            return "No equal distribution possible"
    return people


population = [int(number) for number in input().split(", ")]
wealth = int(input())
print(distribution_of_wealth(population, wealth))
