import re
equation = input("please enter your Equation ")

pattern1 = r'\(.*?\)'  #Brackets
pattern2 = r'\d*\d*\d\*\*\d\d*'  #Exponets 
pattern3 = r'\d\d*\d*\d*'  #isolate numbers from symbols
pattern4 = r'\(' #Find number of bracket sets

'''
match = re.findall(pattern1,equation)


if match: 
    Bedmas(equation)
    '''
'''
    isolatedB = ''.join(match)
    print(isolatedB)
    brokenpart2 = re.findall(pattern2,isolatedB)
    isolatedE = ''.join(brokenpart2)
    print(isolatedE)
    [x1,x2] = re.findall(pattern3,isolatedE)
    print([x1,x2])
    sum1 = int(x1) ** int(x2)
    print(sum1)
    updatedEquation = equation.replace(isolatedE,str(sum1))
    print(updatedEquation)


else:
    print("2")
'''
def doublecheck(type,input):
    if type == 0:
        Bedmas(input)

    elif type == 1:
        bEdmas(input)
    elif type == 2:
        beDMas(input)
    elif type == 3:
        bedmAS(input)







def find_innermost_brackets(expression):
    stack = []
    innermost_brackets = []

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')'ç
            if stack:
                start = stack.pop()
                innermost_brackets.append((start, i))
            else:
                return "Error: Mismatched brackets"
    print(innermost_brackets)
    return innermost_brackets

def Bedmas(var):
   [start,end,a,s,d,f,g,h,j,k,x,z,c,t,n,b,] = find_innermost_brackets(var)
   var[start,end]
   print(var[start,end])

def bEdmas(var2):
    brokenpart2 = re.findall(pattern2,var2)
    isolatedE = ''.join(brokenpart2)
    #print(isolatedE)
    [x1,x2] = re.findall(pattern3,isolatedE)
    #print([x1,x2])
    sum1 = int(x1) ** int(x2)
    #print(sum1)
    updatedEquation = equation.replace(isolatedE,str(sum1))
    print(updatedEquation)


def beDMas(var3):
    var3

def bedmAS(var4):
    var4





match = re.findall(pattern1,equation)


if match: 
    find_innermost_brackets(equation)
    Bedmas(equation)






''' count = re.findall(pattern4,var)
    counter = len(count)
    print(count,counter)
    match = re.findall(pattern1,var)
    isolatedB = ''.join(match)
    print(isolatedB,"1", isolatedB[1:-1])
    if counter > 0:
        doublecheck(0,isolatedB[1:-1])'''