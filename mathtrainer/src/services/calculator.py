#alkuperäinen: https://stackoverflow.com/questions/2371436/
# evaluating-a-mathematical-expression-in-a-string
import ast
import operator as op
import time

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.USub: op.neg}

def calculator(expr):
    """
    +, -, *, / käytössä
    """

    expr = "".join(expr.split())

    if len(expr) == 0:

        return None

    try:
        value = eval_(ast.parse(expr, mode='eval').body)
        print(expr,"=",value)
        time.sleep(1)
        return value

    except KeyError:

        print("Sallitut laskutoimitukset +, -, *, / ja luvun edessä -")
        input("Jatka > ")
        return None

    except SyntaxError:

        print(f"Lauseketta {expr} ei voi arvioida")
        input("Jatka > ")
        return None

    except TypeError:

        print("Lopetus")
        input("Jatka > ")
        return None

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    if isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    if isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    raise TypeError(node)
