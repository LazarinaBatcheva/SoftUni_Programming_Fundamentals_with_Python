def check_for_mileage(cars_info, car, is_car_old=False):
    if cars_info[car][0] >= 100_000:
        return True


def drive_car(cars_info, car, distance, fuel):
    if fuel <= cars_info[car][1]:
        cars_info[car][0] += distance
        cars_info[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if check_for_mileage(cars_info, car):
        print(f"Time to sell the {car}!")
        del cars_info[car]


def refuel_car(cars_info, car, fuel):
    maximum_fuel = 75
    refuel = 0
    if (cars_info[car][1] + fuel) > maximum_fuel:
        refuel = maximum_fuel - cars_info[car][1]
        cars_info[car][1] = maximum_fuel
    else:
        refuel = fuel
        cars_info[car][1] += fuel
    print(f"{car} refueled with {refuel} liters")


def revert_car(cars_info, car, kilometers):
    least_kilometers = 10_000
    cars_info[car][0] -= kilometers
    if cars_info[car][0] < least_kilometers:
        cars_info[car][0] = least_kilometers
    print(f"{car} mileage decreased by {kilometers} kilometers")


def result(cars_info):
    for car, item in cars_info.items():
        print(f"{car} -> Mileage: {item[0]} kms, Fuel in the tank: {item[1]} lt.")


def base_function(command, cars_info):
    while command != "Stop":
        command, *params = command.split(" : ")
        if command == "Drive":
            car, distance, fuel = params[0], int(params[1]), int(params[2])
            drive_car(cars_info, car, distance, fuel)
        elif command == "Refuel":
            car, fuel = params[0], int(params[1])
            refuel_car(cars_info, car, fuel)
        elif command == "Revert":
            car, kilometers = params[0], int(params[1])
            revert_car(cars_info, car, kilometers)
        command = input()


def get_cars_info(number, cars_info):
    for car in range(number):
        car, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
        cars_info[car] = [mileage, fuel]


number_of_lines = int(input())
cars_info_dict = dict()
get_cars_info(number_of_lines, cars_info_dict)
current_command = input()
base_function(current_command, cars_info_dict)
result(cars_info_dict)