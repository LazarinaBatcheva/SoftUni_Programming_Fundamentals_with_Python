countries = [country for country in input().split(", ")]
capital_cities = [city for city in input().split(", ")]
information = dict(zip(countries, capital_cities))
for country, city in information.items():
    print(country, "->", city)