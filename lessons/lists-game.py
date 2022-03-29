"""Examples of using lists."""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

# removing an item ("pop")
rolls.pop(len(rolls) - 1)

# sume the values of our rolls!
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(rolls)
print(f"Total score: {sum}")


# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)