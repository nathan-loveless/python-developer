# PIP Install

# If you have pyCharm, you can install this through the interpreter (Settings->Project)
# If you are not using pyCharm you will need to install it through the terminal
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)
