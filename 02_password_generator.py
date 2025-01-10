import random

import string
#  grab all lowercase & uppercase letters that exist + all special characters as well as all the numbers or digits
# learn more about the string lib here: https://docs.python.org/3/library/string.html

letters = string.ascii_letters
digits = string.digits
specials = string.punctuation

# print(letters, digits, specials)
# result: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# STEP 1: Create a function for the generator:
def password_generator(min_length, numbers=True, special_chars=True):
    characters = letters
    if numbers: # this will be =True because we set the default that way
        characters += digits
    if special_chars: # this is not an elif statement because numbers and special_chars can both happen
        characters += specials

    # print(characters)
# password_generator(10)
# atp: the result is abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ no matter which number is of min_length
# it's because we haven't conditioned the function to loop through a limited length and also haven't made the combination to be random

# STEP 2: Generate a combination that will meet certain criteria
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        # The while loop continues as long as either of these conditions is True. This ensures that:
# The loop keeps running until the password satisfies all criteria (meets_criteria becomes True).
# The loop keeps running until the password length reaches or exceeds min_length.

        # Does not Work Like "Negative + Negative = Positive"?
# Not quite. In Python, not doesn’t "negate twice." Instead, it inverts the logical value:
# If meets_criteria = False, then not meets_criteria = True.
# If meets_criteria = True, then not meets_criteria = False.
# Thus, not simply flips the boolean value, rather than compounding negatives like in arithmetic.

        # Conclusion: assigning meets_criteria = False is just a technique one should apply while working with while loop
# because you can always negate it with not and turn that condition into True to keep the loop running until it become False
# setting  meets_criteria = True
# while meets_criteria or len(pwd) < min_length: WON'T work because then meets_criteria is permanently True, the condition will always evaluate to True, even when len(pwd) >= min_length.
# The loop will never stop, creating an infinite loop.
# setting  meets_criteria = True
# while not meets_criteria or len(pwd) < min_length: WON'T work because then the first condition is always False and won't ever be checked.

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True

        meets_criteria = True
        # Why Set meets_criteria = True First?
# This is done to initialize meets_criteria so it can be progressively updated based on the conditions (numbers and special_chars).
        # Why This Works:
# meets_criteria = True is used as a starting point. The two if statements then progressively refine this value.
        # Overall this is a common pattern seen in programming: you actually start with a variable equal to True, then you try to prove the variable is False and if that's the case, you set it to False
        if numbers:
            meets_criteria = has_number # if numbers is False, this block will be skipped entirely, and meets_criteria remains True (from its initial value).
        if special_chars:
            meets_criteria = meets_criteria and has_special
    # Recap of if Logic
    # If the condition is True: The block executes.
    # If the condition is False: The block is completely skipped—nothing inside the block runs.

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers? (y/n) ").lower() == "y" # this equation will return a Bool, so if "y" is provided, then has_number=True
has_special = input("Do you want to have special characters? (y/n) ").lower() == "y"
pwd = password_generator(min_length, has_number, has_special)
print("The generated password is: ", pwd)


# FUTURE DEVELOPMENTS:
#     This could get more difficult if I want to restrict the number of numbers and the number of special characters
#     If the first character of the pwd must not be a special_char (or number)
#     And so far this is generating a correct pwd based on a list of criteria.. but what if we need to check if a given pwd is acceptable insetad of generating?



