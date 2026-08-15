def hello_world():
    # print("Hello World")
    # print(42)
    # print(6 * 7)


    	# Echo an Integer
# Read an integer from the user and print it back.
    # num = int(input('enter the integer value: '))
    # print(f' the given num is: {num}')
# Echo Two Valuesi
# Read two integers and display both with clear labels (e.g. "first = 3, second = 8").
    # num = int(input('enter the first value: ')) 
    # num2 = int(input('enter the second value: '))
    # print(f'the first num is {num}, second = {num2}')  
    # Characters In & Out
# Assign a character constant to a variable and print it; then read a character from the user and print that too.
    initial = "A"
    # print(f"Assigned character: {initial}")
    # user_input = input("enter the dharacter: ")
    # user_char = user_input[0] if user_input else ""
    # print(f"user entered : {user_char}")

    
    # Read the text "Hello World" from input and print it. Explore why reading word-by-word (token input) drops everything after the space, and how line-based reading fixes it.
    text = input('enter the text: ')
    print(text)
    tokens = input('enter the input:').split()
    print(tokens[0])
hello_world()
