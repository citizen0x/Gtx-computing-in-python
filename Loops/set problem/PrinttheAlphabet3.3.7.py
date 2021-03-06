start_character = "A"
end_character = "Z"

# Print all the letters from start_character to end_character,
# each on their own line. Include start_character and
# end_character themselves.
#
# Remember, you can convert a letter to its underlying ASCII
# number using the ord() function. ord("A") would give 65.
# ord("Z") would give 90. You can use these values to write
# your loop.
#
# You can also convert an integer into its corresponding ASCII
# character using the chr() function. chr(65) would give "A".
# chr(90) would give "Z". So, for this problem, you'll need
# to convert back and forth between ordinal values and
# characters based on whether you're trying to loop over
# numbers or print letters.
#
# You may assume that both start_character and end_character
# are uppercase letters (although you might find it fun to
# play around and see what happens if you put other characters
# in instead!).

# Add your code here! With the original values for
# start_character and end_character, this will print the
# letters from A to Z, each on their own line.

# print(ord("A"))
# print(ord("Z"))
# print(ord(start_character))
# print(ord(end_character))
# print(chr(65))
# print(chr(90))
for i in range(ord(start_character), ord(end_character)+1):
    print(chr(i))

#################################################################
# GTx Solution:

# To write a loop, we want to start with "A" and end with "Z".
# So, we know those will be the arguments to the range part
# of our loop.
#
# Those are letters, though. How do we convert them to numbers?
#
# We can use the ord() function:

start_index = ord(start_character)
end_index = ord(end_character)

# Now we have the numbers for our range function. So, we write
# our for loop. We want to include the letter represented by
# end_index, so we'll go to end_index + 1:

for i in range(start_index, end_index + 1):
    # Now we want to print the current character. To do that,
    # we need to convert the number back into a character using
    # the chr() function:

    print(chr(i))