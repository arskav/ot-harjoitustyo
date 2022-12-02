import random
import os
from services.utilities import is_number, cancel


FINISH = 3
#Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, a, b):
    
    if level == 1:
        return f"{a} + {b}"
    
    if level == 2:
        return f"{a} - {b}"
    
    if level in [3,4]:
        return f"{a}*{b}"

    if level in [5,6]:
        return f"{a}/{b}"


def left_value_func(level, a, b):
    
    if level == 1:
        return a + b
    
    if level == 2:
        return a - b
    
    if level in [3,4]:
            return a * b

    if level in [5,6]:
        return a/b
    
        
def parameters(level):
    if level == 1:
        a = random.randint(0,100)
        b = random.randint(0,100)        
        return a, b

    if level == 2:
        a = random.randint(-50,50)
        b = random.randint(-50,50)    
        return a, b

    if level == 3:
        a = random.randint(2,10)
        b = random.randint(2,10)            
        return a, b 

    if level == 4:
        a = random.randint(-10,10)
        b = random.randint(-10,10)            
        return a, b     

    if level == 5:
        k = random.randint(1,10)
        b = random.randint(1,10)            
        a = k * b
        return a, b         

    if level == 6:
        k = random.randint(-10,10)
        b = random.randint(-10,10)
        a = k * b

        return a, b         




def question(successive_correct, level):
     
    a, b = parameters(level)

    calculation = left_hand_func(level, a, b)
    print("Laske " + calculation)    
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,... Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    ans = input ("x = ")
        
    if is_number(ans):
        y = int(ans)        
        left_value = left_value_func(level, a, b)
        right_value = y
        is_cancelled = False
    else:
        return cancel()        

    if left_value == right_value:           
        is_correct = True    
    else:    
        feedback_left =  calculation       
        feedback_right = f"{left_value}"
        feedback = f"Väärin, vastasit {y}, mutta " 
        feedback +=  feedback_left
        feedback += " = " + feedback_right + "."
        print("="*len(feedback))                
        print(feedback)
        is_correct = False   
        print("=" * len(feedback))

    if is_correct:
        successive_correct += 1
        print(f"Peräkkäisiä oikeita {successive_correct}/{FINISH}")

    is_finish = successive_correct == FINISH    

    return (is_correct, is_cancelled, is_finish)




    
    
   