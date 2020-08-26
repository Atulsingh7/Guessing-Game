n=19
guess=1
print("WELCOME\n")
print("***********GUESS THE NUMBER GAME**********\n")
print("NOTE: The number lies bewtween 1-40. Your task is to guess the number which I am thinking.\n\n")
while(guess<=9):
    print("Enter The Number")
    num=int(input())

    if num>n:
        print("ENTER A SMALL NUMBER")
        guess+=1
        print("Total chances left :",10-guess,"\n")
    elif num<n:
        print("ENTER A LARGE NUMBER")
        guess+=1
        print("Total chances left :", 10 - guess, "\n")
    else:
        print("\n ****BRAVO****")
        print("YOU WON THE GAME")
        break

if(guess==10):
    print("YOU LOOSE THE GAME")
    print("***TRY AGAIN***")
