def adding_neighborhood(neighborhood_data, address):
    while address != "collectApartments":
        name, blocks = address.split(" -> ")
        blocks = blocks.split(",")
        if name not in neighborhood_data:
            neighborhood_data[name] = {}
        for block_number in blocks:
            neighborhood_data[name][int(block_number)] = {}
        address = input()
    return neighborhood_data


def adding_apartments(neighborhood_data, apartments):
    while apartments != "report":
        address_info, apartments_info = apartments.split(" -> ")
        address, number = address_info.split("&")
        apartments_count, single_price = apartments_info.split("|")
        number = int(number)
        if address in neighborhood_data and number in neighborhood_data[address]:
            del neighborhood_data[address][number]
            neighborhood_data[address][number] = {}
            neighborhood_data[address][number][apartments_count] = single_price
        apartments = input()
    return neighborhood_data


def show_result(neighborhood_data):
    for name in sorted(neighborhood_data):
        print(f"Neighborhood: {name}")
        for block in sorted(neighborhood_data[name]):
            if neighborhood_data[name][block]:
                for apartments, price in neighborhood_data[name][block].items():
                    print(f"* Block number: {block} -> {apartments} apartments for sale. Price for one: {price}")
            else:
                print(f"* Block number: {block} -> 0 apartments for sale. Price for one: None")


neighborhood = input()
addresses_data = {}
addresses_data = adding_neighborhood(addresses_data, neighborhood)
apartments_data = input()
addresses_data = adding_apartments(addresses_data, apartments_data)
show_result(addresses_data)