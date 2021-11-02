import random 
from hangman import parts
words=['python','program']
word=random.choice(words)
print("the word has ",len(word),"letters")

right=['_']*len(word)
wrong=[]
def update():
    for i in right:
        print(i,end =' ')
    print()
update()
parts(len(wrong))
while True:
    print("=============================")
    guess=input("Guess the word !!!: ")
    if guess in word:
        index=0
        for i in word:
            if i==guess:
                right[index]=guess
            index=index+1
        update()
    else:
        if guess not in wrong:
            wrong.append(guess)
            parts(len(wrong))
        else:
            print(" you already guessed that ")
        print(wrong)
    if len(wrong) > 4:
        print("you lost")
        print("The Word was",word.upper())
        break
    if '_' not in right:
        print("you won")
        print("The Word was: ",word.upper())
        print("you saved the man ")
        break
        
        
