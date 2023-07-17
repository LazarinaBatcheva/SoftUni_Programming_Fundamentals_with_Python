import re


def demon_info(health, damage, operators):
    health = re.findall(health, demon)
    health = sum(ord(letter) for letter in health)
    damage = re.findall(damage, demon)
    if damage:
        damage = sum(float(number[0]) for number in damage)
        operators = re.findall(operators, demon)
        if operators:
            for operator in operators:
                if operator == "*":
                    damage *= 2
                elif operator == "/":
                    damage /= 2
    else:
        damage = 0
    print(f"{demon} - {health} health, {damage:.2f} damage")


demon_names = input().split(",")
demon_names = [demon.strip() for demon in demon_names]

health_pattern = r"[^\d\+\-\*\/\.]"
damage_pattern = r"([-+]?\d+(\.\d+)?)"
action_pattern = r"[*\/]"

for demon in sorted(demon_names):
    demon_info(health_pattern, damage_pattern, action_pattern)