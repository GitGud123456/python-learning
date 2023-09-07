import re
equation = input("please enter your Equation ")

pattern1 = r'\(.*?\)'  #Brackets
pattern2 = r'\d*\d*\d\*\*\d\d*'  #Exponets 
pattern3 = r'\.*\d\.*\d*\.*\d*\d*'  #isolate numbers from symbols
pattern4 = r'\(' #Find number of bracket sets
pattern5 = r'\d*\d*\d\*\d\d*|\d*\d*\d\/\d\d*'  #mult and dividle 
pattern6 = r'\*|\/'  # look at operator (*,/)
pattern7 = r'\d*\.*\d*\d\-\d\d*|\d*\.*\d*\d\+\d\d*'  #add and subtract
pattern8 = r'\+|\-'  # look at operator (+,-)
pattern9 = r'\(|\)'  # look at brackets "(",")"
pattern10 = r'\*\*'  # look at brackets "(",")"

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
        elif char == ')':
            if stack:
                start = stack.pop()
                innermost_brackets.append((start, i))
            else:
                return "Error: Mismatched brackets"
    #print(innermost_brackets)
    return innermost_brackets

def Bedmas(var):
    test = re.findall(pattern9,var)
    if len(test) == 0:
        bEdmas(var)
    else:
        bracket_list = find_innermost_brackets(var)
        start = int(bracket_list[0][0])
        end = int(bracket_list[0][1])
        isolatedB = var[start:end+1]
        #print(var[start+1:end]
        print(isolatedB)
        bEdmas(isolatedB)

def bEdmas(var2):
    test = re.findall(pattern10,var2)
    if len(test) == 0:
        beDMas(var2)
    else:
        brokenpart2 = re.findall(pattern2,var2)
        isolatedE = ''.join(brokenpart2)
        #print(isolatedE)
        [x1,x2] = re.findall(pattern3,isolatedE)
        #print([x1,x2])
        sum1 = float(x1) ** float(x2)
        #print(sum1)
        updatedEquation = var2.replace(isolatedE,str(sum1))
        print(updatedEquation)
        beDMas(updatedEquation)

def beDMas(var3):
    test = re.findall(pattern6,var3)
    if len(test) == 0:
        bedmAS(var3)
    else:
        brokenMD = re.findall(pattern5,var3)
        isolatedMD = ''.join(brokenMD)
        sign = re.findall(pattern6,isolatedMD)
        [x1,x2] = re.findall(pattern3,isolatedMD)
        if sign == ['*']:
            sum2 = float(x1) * float(x2)
        else:
            sum2 = float(x1) / float(x2)
        updatedEquation = var3.replace(isolatedMD,str(sum2))
        print(updatedEquation)
        bedmAS(updatedEquation)

def bedmAS(var4):
    brokenAS = re.findall(pattern7,var4)
    isolatedAS = ''.join(brokenAS)
    sign = re.findall(pattern8,isolatedAS)
    [x1,x2] = re.findall(pattern3,isolatedAS)
    if sign == ['+']:
        sum3 = float(x1) + float(x2)
    else:
        sum3 = float(x1) - float(x2)
    updatedEquation = var4.replace(isolatedAS,str(sum3))
    print(updatedEquation)
    return updatedEquation

Bedmas(equation)



