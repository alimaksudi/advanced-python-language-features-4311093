# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use dictionary comprehensions


# define a list of temperature values
ctemps = [0, 12, 34, 100]

# TODO: Use a comprehension to build a dictionary
temp_dict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
print(temp_dict)
print(temp_dict[12])

# TODO: Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}

# Use a dictionary comprehension to merge two dictionaries
# Iterate over both teams and over each key-value pair in the team dictionary
# Add the key-value pair to a new dictionary
new_team = {k: v for team in (team1, team2) for k, v in team.items()}
print(new_team)


# create an empty dictionary to hold the merged teams
new_team2 = {}

# iterate over both teams
for team in (team1, team2):
    # iterate over each key-value pair in the team dictionary
    for k, v in team.items():
        # add the key-value pair to the new_team2 dictionary
        new_team2[k] = v

print(new_team2)


# create a new dictionary by copying the first team's dictionary
new_team3 = team1.copy()
# update the new dictionary with the second team's dictionary
new_team3.update(team2)
print(new_team3)
