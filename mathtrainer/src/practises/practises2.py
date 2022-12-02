import random
import os
from services.utilities import is_number, cancel

FINISH = 3
#Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, a, b):
    
    if level == 1:
        return f"x + {a}"
    
    if level == 2:
        return f"{a} - x"
    
    if level in [3,4]:
        return f"{a}x"

    if level == 5:
        return f"x/{a}"

    if level == 6:
        return f"{a}/x"    

def right_hand_func(level, a, b):
    
    if level in [1,2,3,4,5,6]:
        return f"{b}"

def left_value_func(level, a, b, x):
    
    if level == 1:
        return x + a
    
    if level == 2:
        return a - x
    
    if level in [3,4]:
            return a * x  

    if level == 5:
        return x/a  
    
    if level == 6:
        return a/x

def right_value_func(level, a, b, x):
    
    if level in [1,2,3,4,5,6]:
        return b
    
def feedback_left_func(level, a, b, x):

    if level == 1:
        return f"x + {a} = {x} + {a}  = {x + a}"

    if level == 2:
        return f"{a} - x = {a} - {x} = {a - x}"

    if level in [3,4]:
        return f"{a}x = {a}*{x} = {a * x}"

    if level == 5:
        return f"x/{a} = {x}/{a} = {x/a}"

    if level == 6:
        return f"{a}/x = {a}/{x} = {a/x}"

def feedback_right_func(level, a,b,x):

    if level in [1,2,3,4,5,6]:
        return f"{b}"  
       
def parameters(level):
    if level == 1:
        a = random.randint(-10,10)
        k = random.randint(1,10)
        b = a + k
        return a, b

    if level == 2:
        a = random.randint(-20,20)
        b = random.randint(-10,10)    
        return a, b

    if level == 3:
        a = random.randint(2,10)
        k = random.randint(2,10)    
        b = a * k
        return a, b 

    if level == 4:
        a = random.randint(-10,10)
        k = random.randint(-10,10)    
        b = a * k
        return a, b     

    if level == 5:
        a = random.randint(-10,10)
        b = random.randint(-10,10)            
        return a, b         

    if level == 6:
        k = random.randint(-10,10)
        b = random.randint(-10,10)            
        a = k * b
        return a, b         




def question(successive_correct, level):
     
    a, b = parameters(level)

    left_hand = left_hand_func(level, a,b)

    right_hand = right_hand_func(level, a,b)

    solve_task = "Ratkaise x, kun "  + left_hand + " = " + right_hand
    print(solve_task)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,... Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    ans = input ("x = ")
        
    if is_number(ans):
        x = int(ans)        
        left_value = left_value_func(level, a,b,x)
        right_value = right_value_func(level, a,b,x)   
        is_cancelled = False
    else:
        return cancel()  

    if left_value == right_value:           
        is_correct = True    
    else:    
        feedback_left = feedback_left_func(level, a,b,x)        
        feedback_right = feedback_right_func(level, a,b,x)
        left_value = left_value_func(level, a,b,x)
        right_value = right_value_func(level, a,b,x)
        feedback = f"Väärin, kun x = {x}, vasen puoli on " 
        feedback +=  feedback_left
        feedback += ", mutta oikea puoli " + feedback_right + "."
        print("="*len(feedback))        
        print(solve_task)
        print("Vastauksesi oli x =", x)
        print(feedback)
        is_correct = False   
        print("=" * len(feedback))

    if is_correct:
        successive_correct += 1
        print(f"Peräkkäisiä oikeita {successive_correct}/{FINISH}")

    is_finish = successive_correct == FINISH    

    return (is_correct, is_cancelled, is_finish)




    
    
   