import random

def script():
    num_limit= 10
    num_limit_medium= 20
    num_limit_hard= 50

    answer_a = random.randint(1, 10)
    answer_m = random.randint(1, 20)
    answer_h = random.randint(1, 50)   

    chance = 6
    chance_medium= 4
    chance_hard= 3


    rule = '''Welcome to Guess Freak. To win the game you have to guess the correct number.
Enter easy for Easy mode
Enter medium for Medium mode
Enter hard for Hard mode
Enter end to terminate the game
'''
    print(rule)

    command = input('>').lower()

    if command == 'easy':
        while chance > 0 :
            print(f"You have {chance} guess(es) left")
            try:
                guess = int(input("Enter guess: "))
            except:
                print("Invalid input. Use numbers")
                continue
            if guess > num_limit:
                print('choose only numbers between 1 to 10')
            if guess == answer_a: 
                print("Congratulation YOU WON!!!") 
                break
            elif guess != answer_a: 
                print("Wrong guess!! ")
                chance -= 1
                            
            if chance == 0:
                print('Sorry, you Lost!!')

        yn=input('Do you want to play again? (Y) or (N): ').upper()
        if yn=='Y':
            script()

        elif yn=='N':
            print('Thank you. Goodbye \n')
            breakpoint
            
    elif command == 'medium':
        while chance_medium > 0 :
            print(f"You have {chance_medium} guess(es) left")
            try:
                guess = int(input("Enter guess: "))
            except:
                print("Invalid input. Use numbers")
                continue
            if guess > num_limit_medium:
                print('choose numbers between 1 to 20')
            if guess == answer_m: 
                print("Congratulation YOU WON!!!") 
                break
            elif guess != answer_m: 
                print("Wrong guess ")
                chance_medium -= 1
                
            if chance_medium == 0:
                print('Sorry, you Lost!!')

        yn=input('Do you want to play again? (Y) or (N): ').upper()
        if yn=='Y':
            script()

        elif yn=='N':
            print('Thank you. Goodbye \n')
            breakpoint 


    elif command == 'hard':
        while chance_hard > 0 :
            print(f"You have {chance_hard} guess(es) left")
            try:
                guess = int(input("Enter guess: "))
            except:
                print("Invalid input. Use numbers")
                continue
            if guess > num_limit_hard:
                print('choose numbers between 1 to 50')
            if guess == answer_h: 
                print("Congratulation YOU WON!!!") 
                break
            elif guess != answer_h: 
                print("Wrong guess ")
                chance_hard -= 1
                
            if chance_hard == 0:
                print('Sorry, you Lost!!')
        
        yn=input('Do you want to play again? (Y) or (N): ').upper()
        if yn=='Y':
            script()

        elif yn=='N':
            print('Thank you. Goodbye \n')
            breakpoint 
        
    elif command == 'end':
      breakpoint
  

    else:
        print("Select a invalid level selected.")
        script()

script()
        
    
