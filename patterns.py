import pprint
import rpn

candidates = [
    [[], ['1']],
    [['+'], ['1', '2']],
    [['+', '+'], ['1', '2', '3']],
    [['+', '+', '+'], ['1', '2', '3', '4']],
    [['+', '+', '+', '+'], ['1', '2', '3', '4', '5']],
    [['+', '+', '+', '+', '+'], ['1', '2', '3', '4', '5', '6']],
    [['+', '+', '+', '+', '+', '+'], ['1', '2', '3', '4', '5', '6', '7']],
    [['+', '+', '+', '+', '+', '+', '+'], ['1', '2', '3', '4', '5', '6', '7', '8']],
    [['+', '+', '+', '+', '+', '+', '+', '+'], ['1', '2', '3', '4', '5', '6', '7', '8', '9']],
]

class Search:
    def __init__(self):
        self.result = []

    def dfs(self, ops, nums, elements):
        if len(ops) == 0 and len(nums) == 0:
            try:
                r = rpn.RPN(elements)
                r.calc()
                #print(elements, r.decode() + '=' + str(r.calc()))
                #print([i for i, x in enumerate(elements) if x == '+'])
                result = [i for i, x in enumerate(elements) if x == '+']
                self.result.append(result)
            except:
                #print(elements)
                return
    
            return
    
        if len(ops) > 0:
            op = ops.pop()
            self.dfs(ops, nums, [op] + elements)
            ops.append(op)
    
        if len(nums) > 0:
            num = nums.pop()
            self.dfs(ops, nums, [num] + elements)
            nums.append(num)

def get_patterns():
    result = {}
    for i, candidate in enumerate(candidates):
        search = Search()
        search.dfs(candidate[0], candidate[1], [])
        result[i] = search.result

    return result

if __name__ == '__main__':
    pprint.pprint(get_patterns())
