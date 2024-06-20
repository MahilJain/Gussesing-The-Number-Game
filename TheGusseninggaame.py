import random
n=random.randint(1,100)
a=-1
guesses=0
while(a != n):
    a=int(input("Guess the number: "))
    if(a>n):
        print("Lower Number Please")
        guesses +=1
    elif(a<n):
        print("Higher Number Please")    
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} number of attempt")