# python3
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position
        
    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    
    #遍历该text中所有的文字
    for i, item in enumerate(text):
        #如果是（，{，[，储存在stack中
        if item == '(' or item == '[' or item == '{':
            opening_brackets_stack.append(Bracket(item, i))
        #如果是），}，]. 
        #若原数组为空，跳出循环并报没有匹配的item的位置
        #若原数组不为空，则把原数组最后一个值放入last_item中。判断last_item和item中的type相同。若不相同，则记录在opening_brackets_stack中
        if item == ')' or item == ']' or item == '}':
            if len(opening_brackets_stack) == 0:
                opening_brackets_stack.append(Bracket(item, i))
                break
            last_item = opening_brackets_stack.pop()
            if not last_item.Match(item):
                opening_brackets_stack.append(Bracket(item, i))
                break
    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        print(opening_brackets_stack.pop().position + 1)
