# Exercise Logical Operators
is_magician = False
is_expert = False

# Check if both Magician AND Expert and print "You are a master Magician"
# Check if Magician but not an expert print "At least you're getting there"
# If not a Magician "You need magic powers"
if is_magician and is_expert:
    print("You are a master Magician")
elif is_magician and not is_expert:
    print("At least you are getting there")
else:
    print("You need magic powers")
