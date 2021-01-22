# Write a program that reads in a sequence of characters, and determines whether it's parentheses,
# braces, and curly brackets are "balanced."

from task_24_1 import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    #print(f's.is_empty {s.is_empty()}')
    #print(f'balanced {balanced}')
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open_ch, close_ch):
    opens = "([{"
    closers = ")]}"
    return opens.index(open_ch) == closers.index(close_ch)


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))
print(parChecker('[()]'))
