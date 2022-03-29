"""Demonstrations of Dictionary."""

# Declaring a type of dictionary
school: dict[str, int]

# Initializing to an empty dictionary
schools = dict()

# Set a key-value pairing
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150


print(schools)

# Access a value "lookup"
print(f"UNC has {schools['UNC']} students")

# Removing a key value
schools.pop("Duke")

# Testing for the existence of a key 
print('Duke' in schools)

# # Update / Reassign a key-value
# schools['UNC'] = 20000
# schools['NCSU'] += 200

# print(schools)

# invert_schools: dict[int, str]
# invert_schools = dict()
# invert_schools[19400] = "UNC"

# print(invert_schools)

# # Demostrations of dictionary literals

# schools = {}  # Same as dict()
# print(schools)

# schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
# print(schools)

# # Important Notes:
# # Cannot have duplicate keys but can have duplicate values