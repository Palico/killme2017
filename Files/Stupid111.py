from __future__ import print_function 
import random
import time
import sys 




    
def rps():
    y = 0
    name = raw_input('What is your name?\n') #get's name
    while y == 0: #While loop
        a = raw_input('\n\nRock, Paper, or Scissors?:\n\n') #detects string input
        p1 = a.lower() #Lowercases input
        print('\n')
        if p1 == 'paper': #Input == paper
            paper(name)
        elif p1 == 'rock': #Input == rock
            rock(name)
        elif p1 == 'scissors': #Input == scissors
            scissors(name)
        elif p1 == 'end': #Stops game
            byebye(name)
            y += 1    
            sys.exit() #shuts down program
        else: #Input != anything
            wiseass()       

    
    

def rock(name):
    cpu = random.randint(1,3) #CPU chooses
    if cpu == 1: #CPU chooses rock
        print(name,' chose Rock and the CPU chose Rock. Tie!')
    if cpu == 2: #CPU chooses paper
        print('The CPU chose Paper and' ,name, 'chose Rock. You lose!') 
    if cpu == 3: #CPU chooses scissors
        print (name,' chose Rock and the CPU chose Scissors. You win!') 
        
def paper(name):
    cpu = random.randint(1,3) #CPU chooses    
    if cpu == 1: #CPU chooses rock
        print(name, 'chose Paper and the CPU chose Rock. You win!')
            
    elif cpu == 2: #CPU chooses paper
        print(name, ' chose Paper and the CPU chose Paper. Tie!')
            
    elif cpu == 3: #CPU chooses scissors
        print ('The CPU chose Scissors and' ,name, 'chose Paper. You lose!')    

def scissors(name):
    cpu = random.randint(1,3) #CPU chooses  
    if cpu == 1: #CPU chooses rock
        print('The CPU chose Rock and' ,name, 'chose Scissors. You lose!')
            
    elif cpu == 2: #CPU chooses paper
        print(name,' chose Scissors and the CPU chose Paper. You win!')
            
    elif cpu == 3: #CPU chooses scissors
        print (name,' chose Scissors and the CPU chose Scissors. Tie!')  
        
blah = "Wiseass\n"

def wiseass():
    for l in blah: #Prints a letter every .2 seconds
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)

def byebye(name):
    v = "Have a nice day " ,name, "!\n" 
    for l in v: #Prints a letter every .2 seconds
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)


# THE BOTTOM WASN'T NECESSARY >:(

def bot():
    o = 1
    while o < 21:
        time.sleep(1)
        p = ['rock', 'Rock', 'paper', 'Paper', 'scissors', 'Scissors', 'I am a turd']
        a = random.choice(p)
        p1 = a.lower()
        print ('\n\nTest #',o)
        print ('\n''Word: ',a, '\n')
        print ('Lowercased: ' ,p1,'\n')
        if p1 == 'paper':
            o += 1
            paper()
        elif p1 == 'rock':
            o += 1
            rock()
        elif p1 == 'scissors':
            o += 1
            scissors()
        else:
            o += 1
            wiseass()       

           
            



        
