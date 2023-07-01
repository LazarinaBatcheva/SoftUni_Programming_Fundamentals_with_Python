class Party:
    def __init__(self):
        self.people = []


party = Party()

line = input()

while line != "End":
    name = line
    party.people.append(name)
    line = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")