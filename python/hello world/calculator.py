import re



equation = input("please enter your Equation ")

pattern1 = r'\(.*?\)'  #Brackets
pattern2 = r'\d*\d*\d\*\*\d\d*'  #Exponets 
pattern3 = r'\d*\.*\d*\d*\d'  #isolate numbers from symbols
pattern5 = r'\d*\d*\d\*\d\d*|\d*\d*\d\/\d\d*'  #mult and dividle 
pattern6 = r'[*/]'  # look at operator (*,/)
pattern7 = r'\d*\.*\d*\d\-\d\d*|\d*\.*\d*\d\+\d\d*'  #add and subtract
pattern8 = r'[+-]'  # look at operator (+,-)
pattern9 = r'\(|\)'  # look at brackets "(",")"
pattern10 = r'\*\*'  # 
pattern11 = r'\)\('
brackets_done = False
exponets_done = False
mult_div_done = False
add_sub_done = False


def double_bracket_issue_fixer(ori_equation):
    test = re.findall(pattern11,ori_equation)
    if len(test) > 0:
        #ori_equation = re.sub(")(",")*(",ori_equation)
        ori_equation = ori_equation.replace(")(",")*(")
        double_bracket_issue_fixer(ori_equation)
        return ori_equation
    else:
        return ori_equation
equation = double_bracket_issue_fixer(equation)
        


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
        return bEdmas(var)
    else:
        bracket_list = find_innermost_brackets(var)
        start = int(bracket_list[0][0])
        end = int(bracket_list[0][1])
        isolatedB = var[start+1:end]
        #print(var[start+1:end]
        #print(isolatedB)
        return isolatedB

def bEdmas(var2):
    test = re.findall(pattern10,var2)
    if len(test) == 0:
        global exponets_done
        exponets_done = True
        return beDMas(var2)
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
        return bedmAS(var3)
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
        #return complete_part(var4)
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

def loop_till_done(current_equation):

    if brackets_done == False:
        current_equation = Bedmas(current_equation)
    else:
        if exponets_done == False:
            current_equation = bEdmas(current_equation)
        else:
            if mult_div_done == False:
                current_equation = beDMas(current_equation)
            else:
                if add_sub_done == False:
                    current_equation = bedmAS(current_equation)
                else:
                    #print("Line:131  Done!", current_equation)
                    return segment_done_and_replaced_in_ori_equation_with_brackets(current_equation,equation)   
    global solvedpiece
    solvedpiece = current_equation
    return True

def segment_done_and_replaced_in_ori_equation_with_brackets(fin_piece,ori_equation):
    #print(ori_equation,"finished piece:" + fin_piece)

    test = re.findall(pattern9,ori_equation)
    if len(test) == 0:
        print("The anwser to you equation is:" + fin_piece)
        return False
    else:


        bracket_list = find_innermost_brackets(ori_equation)
        start = int(bracket_list[0][0])
        end = int(bracket_list[0][1])
        isolatedB = ori_equation[start:end+1]
        ori_equation = ori_equation.replace(isolatedB,str(fin_piece))
        #print("line:154  " + ori_equation)
        return next_brackets(ori_equation)

def next_brackets(ori_equation):
    global brackets_done,exponets_done,mult_div_done,add_sub_done,count,loop_stopper,solvedpiece,equation
    brackets_done = False
    exponets_done = False
    mult_div_done = False
    add_sub_done = False
    count = 1
    loop_stopper = True
    solvedpiece = ori_equation
    equation = ori_equation
    return True
 
solvedpiece = 0
count = 0
loop_stopper = True
while loop_stopper == True:
    print(solvedpiece)
    
    if count == 0:
        loop_till_done(equation)
        count += 1
        
    else:
        loop_stopper = loop_till_done(solvedpiece)

