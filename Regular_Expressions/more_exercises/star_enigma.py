import re

number_of_lines = int(input())

attacked_planets = []
destroyed_planets = []
pattern = re.compile(
        r"(@)(?P<planet_name>[A-Za-z]+)([^@\-\!\:\>]*)"
        r":(?P<population>[0-9]+)([^@\-\!\:\>]*)"
        r"!(?P<attack_type>[A|D])!([^@\-\!\:\>]*)"
        r"->(?P<soldier_count>\d+)")

for line in range(number_of_lines):
    encrypted_message = input()
    decryption_key = 0
    message, decrypted_message = [], ""
    for letter in encrypted_message:
        if letter.lower() in "star":
            decryption_key += 1
        message.append(letter)
    for character in message:
        decrypted_ch = chr(ord(character) - decryption_key)
        decrypted_message += decrypted_ch
    match = re.finditer(pattern, decrypted_message)

    for value in match:
        planet, attack_type = value.group("planet_name"), value.group("attack_type")
        if attack_type == "A":
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")