is_male = True

if is_male:
    print("You are a male")

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are not a male nor tall ")


if is_male and is_tall:
    print("You are male and tall")
elif is_male and not is_tall:
    print("You are male but not tall")
elif not is_male and is_tall:
    print("You are not a male but are not tall")
else:
    print("you are not a male and not tall")