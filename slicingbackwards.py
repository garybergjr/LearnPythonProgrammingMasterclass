letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

# create a slice that produces the characters qpo
backwards2 = letters[16:13:-1]
print(backwards2)

# slice the string to produce edcba
backwards3 = letters[4::-1]
print(backwards3)

# slice the string to produce the last 8 characters, in reverse order
backwards4 = letters[:17:-1]
print(backwards4)