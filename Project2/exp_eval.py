#Terence Tong
#CSC 202 - 9
from Stacks import StackArray
import operator
ops = { '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '%' : operator.mod,
        '^' : operator.xor
        }
"""
Signature:  a string containing an infix expression where tokens are space separated is
    the single input parameter returns a string containing a postfix expression w
    here tokens are space separated
input: String 
Output: String
"""
def infix_to_postfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression """
    prec = {'^':4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opstack = StackArray(30)
    postfixList = []
    tokenList = infixexpr.split(' ')#returns an array with elements split
    for tok in tokenList:
        if tok not in "^*()-/+": #if token is a number put in the list
            postfixList.append(tok)
        elif tok == '(': #if token is open parenthesis put it in list output
            opstack.push(tok)
        elif tok == ')': #if token is close parenthesis
            toptoken = opstack.pop() #take the top token of stack
            while toptoken != '(': #pop through the stack and append to output list until you get to the open parenthesis
                postfixList.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.is_empty()) and (prec[opstack.peek()] >= prec[tok]):#handle precedence
                if opstack.peek() == '^' and tok == "^":
                    break#dont append
                postfixList.append(opstack.pop())
            opstack.push(tok)

    while not opstack.is_empty():#if empty append everything else
        postfixList.append(opstack.pop())
    return " ".join(postfixList)

"""
Evaluates a postfix expression
input: postfix expression (string)
output： float
"""
def postfix_eval(postfixExpr):
    """  Purpose """
    operandStack = StackArray(30)
    listexp = postfixExpr.split(' ')
    for token in listexp:
        if token not in "^*-+/":
            operandStack.push(float(token))
        else:
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            if token == '^':
                operandStack.push(doMath(token, float(op2), float(op1)))
            else:
                operandStack.push(doMath(token, float(op1), float(op2)))
    return operandStack.pop()

"""
does math 
input: string, int/float, int/float
output: int/float
"""
def doMath(op, op1, op2):
    """  Purpose """
    if op == '/' and op2 == 0:
        raise ValueError("Divide by 0")
    return ops[op](op1, op2)

'''
checks whether an expression can be evaluated using postfix steps
input: string
output: boolean
'''
def postfix_valid(postfixexpr):
    expr = postfixexpr.split(' ')
    count = 0
    for tok in expr:
        if tok not in "*^/-+" and float(tok) < 0:
            count -= 1
            if count < 0:
                return False
            count += 2
        elif tok not in "*^/-+":
            count += 1
        else:
            count -= 2
            if count < 0:
                return False
            count += 1
    return count == 1
