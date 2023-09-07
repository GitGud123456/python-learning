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
        print(isolatedB)
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
        brokenpart2 = re.findall(pattern2,var2)
        isolatedE = ''.join(brokenpart2)
        #print(isolatedE)
        [x1,x2] = re.findall(pattern3,isolatedE)
        #print([x1,x2])
        sum1 = int(x1) ** int(x2)
        #print(sum1)
        updatedEquation = var2.replace(isolatedE,str(sum1))
        print(updatedEquation)
        beDMas(updatedEquation)

def beDMas(var3):
    test = re.findall(pattern6,var3)
    if len(test) == 0:
        global mult_div_done
        mult_div_done = True
       # bedmAS(var3)
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
    test = re.findall(pattern8,var4)
    if len(test) == 0:
        global add_sub_done
        add_sub_done = True
        return var4
    else:
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



def loop_till_done(b_done,e_done,dm_done,as_done,start_equation):
    current_equation = Bedmas(start_equation)
    if b_done == True & e_done == False:
        current_equation = bEdmas(current_equation)
    elif e_done == True & mult_div_done == False:
        current_equation = beDMas(current_equation)
    elif mult_div_done == True & as_done == False:
        current_equation = bedmAS(current_equation)
    elif b_done == True & e_done == True & dm_done == True & as_done == True:
        print("Done!", current_equation)
        return False

    return True

while loop_till_done:
    loop_till_done(brackets_done,exponets_done,mult_div_done,add_sub_done,equation)


#Bedmas(equation)

'''
if brackets_done == True:
    print("working")
else:
    print("fuck")
 
'''
