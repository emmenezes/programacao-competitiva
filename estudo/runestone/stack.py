class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    
    return s.is_empty()

def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
    return s.is_empty()

def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)

# print(balance_checker('{({([][])}())}'))
# print(balance_checker('[{()]'))

def divide_by_2(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2
    
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string

# print(divide_by_2(256))    
# print(divide_by_2(128))

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "01123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while(not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ". join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))