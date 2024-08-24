#   1-Assign a message to a variable & print that message
message : str = "Hello Python Crash Course Reader"
print(message)

#   2-Storing Multiple Value to a single Variable & printing it 
new_message : str = "\nHello Python & Gen_Ai Developer"
print(new_message)

new_message_1 : str = "Hello Dear Python Programmer"
print(new_message)

#   3-Variable Usage--print person_name & personal_message  
name : str = "Hanzla Saleem"
message : str = f"\nHello {name}, Would You like to Learn some Python today?"
print(message)

#   4-Print the person’s name in lowercase, uppercase, and title case.
name : str = "hanzla saleem"
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.lower())

#   5-Print the quote and the name of its author.
quote : str ='\nHanzla Saleem Once said,"Be firm in your stance, unless the World follows You " '
print(quote)

#   6-Using "famous_person" variable & Composing message & representing with variable
famous_person : str = "\nMoulana Jalal Ud Din Rumi"
message : str = f"{famous_person} once said, Do not Feel Lonely, The Entire Universe is inside You "
print(message)

#   7-Printing variables Using lstrip(),rstrip(),strip() Methods
variable : str = "   \n\tJunaid Sajjad   "
print(variable)
print(variable.rstrip())
print(variable.lstrip())
print(variable.strip())

#   8-Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum
print('\n')
x : int = 5
y : int = 10 
z : int = 15
sum : str = f"sum Of X:{x} + Y:{y} + Z:{z} = {x+y+z}"
print(sum)

#   9-Swap the values of two variables a and b. Print the values before and after the swap.
print('\n')
a : int = 10
b : int = 15
print('values before swap')
print(a)
print(b)
print('values after swap ')
c = a 
a = b 
b = c 
print(a)
print(b)

#   10-Create variable for favorite color and printing  it then changing the variable name & printing it again
favorite_color : str = "\nfavorite Color : Black, white, Blue "
print(favorite_color)
color : str = "favorite color : Black, white, Blue "
print(color)

#   11-Create a variable pet_name and set it to "Buddy". Changing the value of pet_name & print the new value.
pet_name : str = "\nPet Name : Buddy"
print(pet_name)
pet_name : str = "Pet Name : Max"
print(pet_name)

#   12-Observing NameError to a variable with value "sunshine " 
new_name : str = "sunshine : NameError Was OBSERVED CLEARLY "
print(new_name)

#   13-Assign the value 100 to a variable "score" & printing it then changing "score" value & printing it again
score : int = 100
score : str = f"\nScore is:{score}"
print(score)
score : int = 106 
score : str = f"Score is:{score} "
print(score)

#   14-Create a string variable city and assign it the name of a city you like. Print the city name.
city_name : str = "\nMadina Pak"
print(city_name)

#   15-Create a variable text with the value "python programming" and print it in title case.
text : str = '\ntitle_case:"python programming" '
print(text.title())

#   16-Assign a string with mixed cases to a variable and print it in all lowercase letters.
string : str = '\nlower_case:"PyThOn pRoGrAmmING" '
print(string.lower())

#   17-Assign a string with mixed cases to a variable and print it in all uppercase letters.
string_1 : str = '\nupper_case:"pYtHoN PrOGrAmMiNg"'
print(string_1.upper())

#   18-Create a variable temperature with the value 25. Print "The current temperature is [temperature] degrees." using the variable.
temperature : int = 25
print(f"\nThe current temperatre is {temperature} degrees ")

#   19-Printing a Poem

    #declaring variable poem 
poem :str 
    #iniiazlizign variable poem 
poem = '''\nLove has nothing to do with the five senses and the six directions:

\nits goal is only to experience the attraction exerted by the Beloved.

\nAfterwards, perhaps, permission will come from God:

\nthe secrets that ought to be told with be told with an eloquence nearer to the understanding
that these subtle confusing allusions.

\nThe secret is partner with none, but the knower of the secret:

\nin the skeptic’s ear, the secret is no secret at all '''
    #printing the poem 
print(poem)

