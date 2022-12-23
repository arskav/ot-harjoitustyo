"""Merkkijonona, jossa alussa '=' annetun lausekkeen arvon laskeminen.
Alkuperäinen idea https://stackoverflow.com/questions/2371436/
# evaluating-a-mathematical-expression-in-a-string

    Raises:
        KeyError: muu laskutoimitus kuin +, -, *, /.
        SyntaxError: syntaksiltaan väärä lauseke.
        TypeError: merkkijono ei tulkittavaksi lausekkeeksi.

    Returns:
        lausekkeen arvo lukuna tai None, jos väärin muodostettu lauseke.
    """

import ast
import operator as op
import time

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.USub: op.neg}

def calculator(expr):
    """Laskee luvuista ja operaattoreista +, -, *, / muodostetun
    lausekkeen arvon.
    """

    expr = "".join(expr.split())

    if len(expr) == 0:

        return None

    try:
        value = eval_(ast.parse(expr, mode='eval').body)
        print(expr,"=",value)
        time.sleep(1)
        return value

    except ZeroDivisionError:

        print("Nollalla ei voi jakaa.")
        time.sleep(1)

    except (KeyError, SyntaxError, TypeError):

        print("Sallitut laskutoimitukset +, -, *, / ja luvun edessä -")
        print(f"Lauseketta {expr} ei voi arvioida.")
        time.sleep(1)

    return None


def eval_(node):
    """Käsittelee rekursiivisesti lauseketta."""

    if isinstance(node, ast.Num): # <number>
        return node.n
    if isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    if isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    raise TypeError(node)
