
def main():
    print ("Hi im chatbot")
    print("let's get to know each other!")
    intro()
    ask()
    color()
    place()
    vac()
    game()
    number()
    dog()
    bye()

def intro():
    answer = input("whats your name?--\n")
    print("Hi",answer,":)")
def ask():
    ans = input("\nHow old are you?--")
    print(ans,"is a great age!")
def color():
    ans = input("\nwhat is your favorite color?--")
    print(ans,"is my favorite color too :)")
    print("looks like we have alot in common")
def game():
        print("\nlets play a game")
        print("whats the color of the sky? blue or gray")
        user_input = input()
        if user_input == "blue":
            print("good you're not dumb ")
        elif user_input =="gray":
            print("damm you sooo STUPID")
        print("-Ok next question")
        print("Whats better popeyes or kfc?")
        user_inp = input()
        if user_inp == "popeyes":
            print("Ew you have bad taste")
        elif user_inp =="kfc":
            print("OH YEAH KFC for life")
        print("Ok lets do something else")
def vac():
     answer = input("\nWhat did you do last summer? ")
     print("That's so cool!")
     print ("I wish i could've",answer,)
     print("But i am not human:(")
def place():
    answer = input("\nWhere are you from?--")
    print("Ive heard of",answer,",apparently its a beautiful place to live ")

def number():
 num = int(input("\nIs it even(type a number): "))
 if (num % 2) == 0:
   print("True".format(num))
 else:
   print("false".format(num))
def dog():
    print("\nOk enough of that,do you have a dog? yes or no?--")
    user_input = input()
    if user_input == "yes":
        print("thats so cool ")
        print("i have one too wanna see?--")
        user_input = input()
        if user_input == "yes":
            print("look at him isnt he soo cute his name is mr.sparkles")
            print("╥━━━━━━━━╭━━╮━━┳")
            print("╢╭╮╭━━━━━┫┃▋▋┣")
            print("╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣")
            print("╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣")
            print("╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣")
            print("╨━━┗┛┗┛━━┗┛┗┛━━┻")
        elif user_input =="no":
            print("oh well")
    elif user_input =="no":
        print("oh so sad :(")
def bye():
    print("\nNow that we know so much about each other, is it ok if we could be best friends? yes or no--")
    user_input = input()
    if user_input == "yes":
        print(":) Yay!Well it was nice talking to you bestie")
        print("miss you already ( ˘ ³˘)♥ xoxo")
    elif user_input =="no":
        print("Its ok, i figured a human bot relationship wouldn't work :(")
        print("Bye,Bye")








main()
