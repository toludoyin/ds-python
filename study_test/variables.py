strings_ = 'Gender'   # datatypes
float_ = 3.14
integers_ = 654
booleans_ = True or False
# complex_ = 4 + 123y
dictionary_ = {'name': 'jam jam',  # data structures
               'age': 100,
               'married': False}
set_ = {'name', 35, True, 13.6}
list_ = ['name', 35, True, 13.67]
tuple_ = ('name', 35, True, 13.67)
print(f'1. {type(set_)}\n')

print('String formating in text %s numbers %d and float %f' % (strings_,  integers_, float_))          # c-style string formatting

# basic operation evaluation rule; parenthesis, exponential, (multiplication division, remainder), (addition, subtraction) -->left >> right.
number = 13 + 8 * 9 / 4 ** 3
print(f'3. Expression result: {round(number,2)}\n')

# assigning variables to value and expressions to solve a quadratic equation
import math
a = 6  # assignment statement
b = 10
c = 12
quadratic_equation = -b +- (math.sqrt(b ** 2) - (4 * a * c))/ 2 * a  #expression
print(f'4. The quadratic equation result is %s \n' % quadratic_equation)

# swapping variables
adapter = 'postilion'
intent = 'reversal'
bank = adapter
adapter = intent
intent = bank
print(f'5. {intent} \n')

# input finction to welcome user
intro = input('what is your name? ').title()
intro1 = input(str("Let's get to know you, what is your favorite programming language?")).upper()
result = f"Welcome {intro}. We love your,favorite programming,language {intro1}\n"
print(result.replace(',', ' '))  # string manipulation
hrs = input('Enter hours to learn your programming language: ') # an input function to give users their toatal pay based on their imput
rate = input('Enter rate: ')
try:
    print('Pay:', float(hrs) * float(rate))
except:
    print('Input Error')

# strings library
name = ' TOLUDOYIN SHOPEIN '  # stripping whitespace
name.rstrip()
name.lstrip()
name.strip()
name.startswith(' TOLU')

# split function
fruit = 'orange mango pineapple watermelon'
fruits = fruit.split()
for f in fruits:
    print(f)