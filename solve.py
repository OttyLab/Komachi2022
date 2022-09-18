import patterns
import rpn

PATTERNS = patterns.get_patterns()

def get_split_nums():
    split_nums= []
    def dfs(acc, num):
        if num == 10:
        #if num == 4:
            split_nums.append(acc)
            return
        dfs(acc + str(num), num + 1)
        if acc != '':
            dfs(acc + ' ' + str(num), num + 1)
    dfs('', 1)
    return split_nums

def get_elements(split_num):
    elements = []
    def dfs(cnt, ops, nums):
        if cnt == 1:
            element = [ops, nums]
            elements.append(element)
            return
        dfs(cnt - 1, ops + ['+'], nums);
        dfs(cnt - 1, ops + ['-'], nums);
        dfs(cnt - 1, ops + ['*'], nums);
        dfs(cnt - 1, ops + ['/'], nums);

    dfs(len(split_num), [], split_num)

    return elements

split_nums = get_split_nums()

for split_num in split_nums:
    elements = get_elements(split_num.split())
    for element in elements:
        pattern = PATTERNS[len(element[1])-1]
        for p in pattern:
            exp = []
            j = 0
            k = 0
            for i in range(len(element[0]) + len(element[1])):
                if i in p:
                    exp = exp + [element[0][j]]
                    j = j + 1
                else:
                    exp = exp + [element[1][k]]
                    k = k + 1

            #print(exp)
            r = rpn.RPN(exp)
            try:
                result = r.calc()
                if 2021.999 < result and result < 2022.001:
                    print(exp, r.decode() + '=' + str(result), flush=True)
            except:
                pass



