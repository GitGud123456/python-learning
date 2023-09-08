import re
equation = input("please enter your Equation ")



pattern1 = r'\(.*?\)'  #Brackets
pattern2 = r'\d*\d*\d\*\*\d\d*'  #Exponets 
pattern3 = r'\d*\.*\d*\d*\d'  #isolate numbers from symbols
pattern5 = r'\d*\d*\d\*\d\d*|\d*\d*\d\/\d\d*'  #mult and dividle 
pattern6 = r'\*|\/'  # look at operator (*,/)
pattern7 = r'\d*\.*\d*\d\-\d\d*|\d*\.*\d*\d\+\d\d*'  #add and subtract
pattern8 = r'\+|\-'  # look at operator (+,-)
pattern9 = r'\(|\)'  # look at brackets "(",")"
pattern10 = r'\*\*'  # look at brackets "(",")"

brackets_done = False
exponets_done = False
mult_div_done = False
add_sub_done = False



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
        global brackets_done
        brackets_done = True
        return var
    else:
        bracket_list = find_innermost_brackets(var)
        start = int(bracket_list[0][0])
        end = int(bracket_list[0][1])
        isolatedB = var[start:end+1]
        #print(var[start+1:end]
        #print(isolatedB)
        #bEdmas(isolatedB)
        return isolatedB

def bEdmas(var2):
    test = re.findall(pattern10,var2)
    if len(test) == 0:
        global exponets_done
        exponets_done = True
       # beDMas(var2)
        return var2
    else:
        brokenpart2 = re.search(pattern2,var2)
        isolatedE = brokenpart2.group()        # = ''.join(brokenpart2[0][3])
        #print(isolatedE)
        [x1,x2] = re.findall(pattern3,isolatedE)
        #print([x1,x2])
        sum1 = int(x1) ** int(x2)
        #print(sum1)
        updatedEquation = var2.replace(isolatedE,str(sum1))
        #print(updatedEquation)
        return updatedEquation

def beDMas(var3):
    test = re.findall(pattern6,var3)
    if len(test) == 0:
        global mult_div_done
        mult_div_done = True
        return var3
    else:
        brokenMD = re.search(pattern5,var3)
        isolatedMD = brokenMD.group()     #''.join(brokenMD)
        sign = re.search(pattern6,isolatedMD).group()
        [x1,x2] = re.findall(pattern3,isolatedMD)
        if sign == '*':
            sum2 = int(x1) * int(x2)
        else:
            sum2 = int(x1) / int(x2)
            sum2 = str(sum2).replace(".0","")
            float(sum2)

        updatedEquation = var3.replace(isolatedMD,str(sum2))
        #print(updatedEquation)
        return updatedEquation

def bedmAS(var4):
    test = re.findall(pattern8,var4)
    if len(test) == 0:
        global add_sub_done
        add_sub_done = True
        return var4
    else:
        brokenAS = re.search(pattern7,var4)
        isolatedAS = brokenAS.group()     #''.join(brokenAS)
        sign = re.search(pattern8,isolatedAS).group()
        [x1,x2] = re.findall(pattern3,isolatedAS)
        if sign == '+':
            sum3 = int(x1) + int(x2)
            sum3 = str(sum3).replace(".0","")
            float(sum3)
        else:
            sum3 = int(x1) - int(x2)
            sum3 = str(sum3).replace(".0","")
            float(sum3)
        updatedEquation = var4.replace(isolatedAS,str(sum3))
        #print(updatedEquation)
        return updatedEquation



def loop_till_done(start_equation):
    current_equation = Bedmas(start_equation)
    #print(current_equation, start_equation)

    if brackets_done == True:
        current_equation = bEdmas(current_equation)
        #print(current_equation)

        if exponets_done == True:
            current_equation = beDMas(current_equation)
            #print(current_equation)
            if mult_div_done == True:
                current_equation = bedmAS(current_equation)
                #print(current_equation)
    if brackets_done == True & exponets_done == True & mult_div_done == True & add_sub_done == True:
        print("Done!", current_equation)
        return False
    #print(True,current_equation)
    global solvedpiece
    solvedpiece = current_equation
    return True

solvedpiece = 0
count = 0
loop_stopper = True
while loop_stopper == True:
    
    if count == 0:
        loop_till_done(equation)
        count += 1
        
    else:
        loop_stopper = loop_till_done(solvedpiece)


#Bedmas(equation)
