# 1. Write a function called shout that takes in a string as an argument and returns it in all caps.
def shout(string):
    output = string.upper()
    return output

a = shout("hello there my name is alex")
print(a)

# 2. Write a function called whisper that takes in a string as an argument and returns it in all lowercase.





# 3. Write a function called how_many_letters that takes in a string as an argument and returns the number of letters in that string.

def how_many_letters(string):
    output = len(string)
    return output

c = how_many_letters("Hello")
print(c)




# 4. Write a function called work_it that takes in a string as an argument and returns it backwards and with the first letter capitalized.
#    For example, work_it("I put my thing down flip it and reverse it") would return "Ti esrever dna ti pilf nwod gniht ym tup i"


def work_it(string):
    output = string[::-1]
    return output

d = work_it("i put my thing down flip it and reverse iT")
print(d)


# 5. Write a function called repeat_it that takes in a word and a number, and returns the word that many times.
#    For example, repeat_it("Banana", 3) would return "BananaBananaBanana"

def repeat_it(string, number):
    output = string*number
    return output

e = repeat_it("Banana", 3)
print(e)



# 6. Write a function called will_it_nametag that takes in a name and a number, and tells you whether the name can be printed on a nametag that size.
#    For example, will_it_nametag("Peter", 10) will return True, but will_it_nametag("Peter", 4) will return False, because "Peter" is 5 letters long, and needs at least 5 spaces to fit on a nametag.

def will_it_nametag(string, number):
    if len(string) <= number:
        return True
    else:
        return False

f = will_it_nametag("Peter", 6)
print(f)






# 7. Write a function called add_liar that takes in two numbers and prints out a lie like "Sorry, I don't know how to add ___ and ___."
#    BUT even though it *prints* that it doesn't know the answer, have the function return the correct answer anyways.

def add_liar(number1, number2):
    output = number1 + number2
    print("Sorry, I dont know how to add ",number1," and ",number2,".")
    print(output)
    return(output)

add_liar(1,2)






# 8. CHALLENGE: Now that you've written all these functions, try combining them. what would happen if you tried to call repeat_it(work_it("Stressed"), 3) ?


x = repeat_it(work_it("Stressed"), 3)
print(x)


# 9. MEGA CHALLENGE: Write a function called doubler that takes in a string and returns it with every letter doubled.
#    For example, doubler("Lost in the Woods") would return "LLoosstt iinn tthhee WWooooddss"


# 10. SUPER MEGA CHALLENGE: Head to https://codingbat.com/python/String-2 and attempt some of the challenges there!
