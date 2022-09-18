class RPN:
    def __init__(self, elements):
        self.elements = elements

    def calc(self):
        stack = list()
        for element in self.elements:
            if element in ['+', '-', '*', '/']:
                if len(stack) < 2:
                    raise Exception
    
                right = stack.pop()
                left = stack.pop()
    
                if element == '+':
                    result = left + right
                elif element == '-':
                    result = left - right
                elif element == '*':
                    result = left * right
                else:
                    result = left / right
    
                stack.append(result)
            else:
                stack.append(int(element))
    
        if len(stack) != 1:
            raise Exception
        return stack[0]
    
    def decode(self):
        stack = list()
        for element in self.elements:
            if element in ['+', '-', '*', '/']:
                if len(stack) < 2:
                    raise Exception
    
                right = stack.pop()
                left = stack.pop()
    
                if element == '+':
                    result = left + '+' + right
                elif element == '-':
                    if not right.isdigit():
                        if self._get_lowest_op(right) == 1:
                            right = '(' + right + ')'
                    result = left + '-' + right
                elif element == '*':
                    if not left.isdigit():
                        if self._get_lowest_op(left) == 1:
                            left = '(' + left + ')'
                    if not right.isdigit():
                        if self._get_lowest_op(right) == 1:
                            right = '(' + right + ')'
                    result = left + '*' + right
                else:
                    if not left.isdigit():
                        if self._get_lowest_op(left) == 1:
                            left = '(' + left + ')'
                    if not right.isdigit():
                        right = '(' + right + ')'
                    result = left + '/' + right
    
                stack.append(result)
            else:
                stack.append(element)
    
        if len(stack) != 1:
            raise Exception
        return stack[0]

    def _get_lowest_op(self, elements):
        paranthes_count = 0
        lowest = 2 # 1:+-, 2:*/

        for element in elements:
            if element == '(':
                paranthes_count = paranthes_count + 1
            elif element == ')':
                paranthes_count = paranthes_count - 1
            elif element not in ['+', '-', '*', '/']:
                continue
            else:
                if paranthes_count > 0:
                    continue
                else:
                    if element == '+' or element == '-':
                        lowest = 1

        return lowest

if __name__ == '__main__':
    exps = [
        '3 4 + 5 *'.split(),
        '3 4 * 5 +'.split(),
        '12 34 * 5 * 6 + 7 8 + - 9 -'.split(), #(12*34)*5+6-(7+8)-9
        '12 34 5 * * 6 + 7 8 + - 9 -'.split(), #12*(34*5)+6-(7+8)-9
        '12 3 + 4 * 5 6 7 * * 8 + 9 * +'.split(), #(12+3)*4+(5*(6*7)+8)*9
        '12 3 + 4 * 5 6 * 7 * 8 + 9 * +'.split(), #(12+3)*4+((5*6)*7+8)*9
        ['1', '2', '3', '/', '*', '4', '5', '6', '7', '*', '8', '*', '9', '*', '+', '+', '*'],
    ]

    for exp in exps:
        rpn = RPN(exp)
        print(rpn.decode() + '=' + str(rpn.calc()))

