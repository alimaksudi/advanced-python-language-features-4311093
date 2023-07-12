# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use set comprehensions


# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# TODO: build a set of unique Fahrenheit temperatures
# list comprehension
ftemps1 = [(t * 9/5) + 32 for t in ctemps]
print(ftemps1)

# set comprehension
s_temp = {(t * 9/5) + 32 for t in ctemps}
print(s_temp)

# TODO: build a set from an input source
s_temp = "The quick brown fox jumped over the lazy dog"

# create a set of uppercase characters from the string s_temp, ignoring whitespace
uppercase_chars = {char.upper() for char in s_temp if not char.isspace()}
print(uppercase_chars)