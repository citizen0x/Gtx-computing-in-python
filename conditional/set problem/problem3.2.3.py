rating = "G"
age = 15

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The United States has a movie rating system that rates
#movies with one of five ratings: G, PG, PG-13, R, and NC-17.
#Although some of the ratings are not binding, imagine that
#you are a parent who decides on the following rules:
#
# - Any child can see a G-rated movie.
# - To see a PG-rated movie, your child must be 8 or older.
# - To see a PG-13-rated movie, your child must be 13 or older.
# - To see an R-rated movie, your child must be 17 or older.
# - Your child may never see an NC-17 movie.
#
#The variables above give a rating and a child's age. Use
#these variables to select and print one of these two
#messages based on the criteria above:
#
# - "You may see that movie!"
# - "You may not see that movie!"
#
#However, there's one trick: you may not use the 'and' operator
#anywhere in this code!


#Add your code here!

if rating == "NC-17":
    print("You may not see that movie!")
if rating == "G":
    print("You may see that movie!")
if rating == "PG":
    if age >= 8:
          print("You may see that movie!")
    elif age < 7:
          print("You may not see that movie!")
if rating == "PG-13":
    if age >= 13:
        print("You may see that movie!")
    elif age<=13:
        print("You may not see that movie!")
if rating == "R":
    if age >= 17:
        print("You may see that movie!")
    elif age < 17:
          print("You may not see that movie!")
# 1st Gtx Solution:
rating = "R"
age = 15

# This exercise is made significantly harder because we're
# not allowed to use 'and'. Because of this, we have to take
# a nested approach.

# For two of the conditions, age doesn't matter. So, let's
# handle those first:

if rating == "NC-17":
    print("You may not see that movie!")
elif rating == "G":
    print("You may see that movie!")

# If the rating isn't G or NC-17, we need to worry about
# ages:

elif rating == "PG":
    if age >= 8:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating == "PG-13":
    if age >= 13:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating == "R":
    if age >= 17:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")

# Note, though, that there's a lot of repetition here.
# All the print statements are the same. We generally
# want to limit code duplication. Is there a more
# efficient way to do this? Yes! Check out
# sample_answer_2.py.
#######################################################
# 2nd Gtx Solution:
rating = "R"
age = 15

# Now, instead of printing within every branch of our
# conditionals, let's instead only print at the end. We'll
# create a boolean that will track whether the kid has
# permission, and then at the end we'll use it to decide what
# to print. That cuts down on our duplicate print statements.
#
# Then, we could do the same thing as we did in the other
# sample answer, just replacing the print statements with
# permission = True and permission = False. However, we can
# make it even simpler since we're not printing to the end.
# Instead of ever saying permission = True inside a
# conditional, let's instead just assume that it's True, and
# check for reasons to switch it to False. That lets us get
# rid of all our else blocks!

# So, assume permission is True unless we find reason to
# change it...
permission = True

# Check for reasons to change it...
if rating == "NC-17":
    permission = False
elif rating == "R":
    if age < 17:
        permission = False
elif rating == "PG-13":
    if age < 13:
        permission = False
elif rating == "PG":
    if age < 8:
        permission = False

# Then, decide what to print!
if permission:
    print("You may see that movie!")
else:
    print("You may not see that movie!")
