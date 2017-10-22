def insert0(x,ss):
    if ss != []:
        if x <= ss[0]:
            return [x] + ss
        else:
            return [ss[0]] + insert0(x,ss[1:])
    else:
        return [x]

def insert1(x,ss):
    def loop(ss,left):
        if ss != []:
            if x <= ss[0]:
                left = left + [x] + ss[:]
                return  left
            else:
                left = left + [ss[0]]
                return loop(ss[1:],left)
        else:
            left = left + [x]
            return left
    return loop(ss,[])

def insert(x,ss):
    left = []
    while not ss == []:
        if x <= ss[0]:
            left = left + [x] + ss
            return left
        else:
            ss, left = ss[1:], left + [ss[0]]
    left = left + [x]
    return left

def isort0(s):
    if s != []:
        return insert(s[0],isort0(s[1:]))
    else:
        return []

def isort1(s):
    def loop(s,ss):
        if s != []:
            ss = insert(s[0],ss)
            return loop(s[1:],ss)
        else:
            return ss
    return loop(s,[])

def isort2(s):
    ss = []
    while s!= []:
        s, ss = s[1:], insert(s[0],ss)
    return ss

def isort3(s):
    ss = []
    for x in s:
        ss = insert(x,ss)
    return ss

def merge1(left,right):
    def loop(left,right,ss):
        if not (left ==[] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return loop(left[1:],right,ss)
            else:
                ss.append(right[0])
                return loop(left, right[1:], ss)
        else:
            return ss + left + right
    return loop(left,right,[])

def merge2(left,right):
    ss = []
    while not(left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left = left[1:]
        else:
            ss.append(right[0])
            right = right[1:]
    return ss + right + left

def bsort(s):
    for k in range(len(s)-1):
        for i in range(len(s)-1-k):
            if s[i] > s[i+1]:
                s[i], s[i+1]= s[i+1], s[i]
    return s
