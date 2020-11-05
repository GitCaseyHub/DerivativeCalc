# Program to perform general differentiation
# Issue with DiffMultiTerm of term separation (of course!)
# Differentiations functions of the form: ax^(f(x))
def polyRule(function,variable):
    if '^' not in function:
        returnVal = function[:-1] if function[:-1] !='' else '1'
        if returnVal=='[' or returnVal==']' or returnVal=='(' or returnVal==')':
            returnVal='1'
            
        return returnVal

    else:
        [coefficient,power] = function.split('^')
        if '(' in power or ')' in power:
            power=power.replace('(','')
            power=power.replace(')','')
        elif '<' in power or '>' in power:
            power=power.replace('<','')
            power = power.replace('>','')

        try:
            new_power = "^"+str(float(power)-1) if float(power)-1 !=1 else ""
            coefficient = 1 if coefficient[:-1] == '' else coefficient[:-1]
            return '('+power+variable+new_power+')' if coefficient is "" else '('+str(float(coefficient)*float(power))+variable+new_power+')'
    
        except:
            return '('+function+')('+productRule('<'+power+'>*<ln('+str(coefficient)+')','x')+')'

# Differentiate Cosine Function
def diffCosine(function,variable):
    [coeff,inside] = function.split('cos(',1)
    inside=inside[:-1]
    if '+' or '-' in inside and checkLowestChain(inside,variable)==True:
        return '-'+coeff+'sin('+inside+')('+diffMultiTerm(inside,variable)+')' if diffMultiTerm(inside,variable) != '1' else '-'+coeff+'sin('+inside+')'
    else:
        return '-'+coeff+'sin('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable) != '1' else '-'+coeff+'sin('+inside+')'

# Differentiate Sine Function
def diffSine(function,variable):
    [coeff,inside] = function.split('sin(',1)
    inside=inside[:-1]
    if '+' or '-' in inside and checkLowestChain(inside,variable)==True:
        return coeff+'cos('+inside+')('+diffMultiTerm(inside,variable)+')' if diffMultiTerm(inside,variable)!='1' else coeff+'cos('+inside+')'
    else:
        return coeff+'cos('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else coeff+'cos('+inside+')'

# Differentiates Tangent Function
def diffTan(function,variable):
    [coeff,inside] = function.split('tan(',1)
    inside=inside[:-1]
    if '+' or '-' in inside and checkLowestChain(inside,variable)==True:
         return coeff+'[sec('+inside+')]^(2)('+diffMultiTerm(inside,variable)+')' if diffMultiTerm(inside,variable)!='1' else coeff+'[sec('+inside+')]^(2)'
    else:
        return coeff+'[sec('+inside+')]^(2)('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else coeff+'[sec('+inside+')]^(2)'

# Differentiates Secant Function
def diffCsc(function,variable):
    [coeff,inside] = function.split('csc(',1)
    inside=inside[:-1]
    if '+' or '-' in inside and checkLowestChain(inside,variable)==True:
        return '-'+coeff+'csc('+inside+')cot('+inside+')('+diffMultiTerm(inside,variable)+')' if diffMultiTerm(inside,variable)!='1' else '-'+coeff+'csc('+inside+')cot('+inside+')'
    else:
        return '-'+coeff+'csc('+inside+')cot('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else '-'+coeff+'csc('+inside+')cot('+inside+')'

# Differentiates Cosecant Function
def diffSec(function,variable):
    [coeff,inside] = function.split('sec(',1)
    inside=inside[:-1]
    if '+' or '-' in inside and checkLowestChain(inside,variable)==True:
        return coeff+'sec('+inside+')tan('+inside+')('+diffMultiTerm(inside,variable)+')' if diffMultiTerm(inside,variable)!='1' else coeff+'sec('+inside+')tan('+inside+')'
    else:
        return coeff+'sec('+inside+')tan('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else coeff+'sec('+inside+')tan('+inside+')'

# Differentiates Cotangent Function
def diffCot(function,variable):
    [coeff,inside] = function.split('cot(',1)
    inside=inside[:-1]
    if '+' or '-' in inside and checkLowestChain(inside,variable)==True:
        return '-'+coeff+'[csc('+inside+')]^(2)('+diffMultiTerm(inside,variable)+')' if diffMultiTerm(inside,variable)!='1' else '-'+coeff+'[csc('+inside+')]^(2)'
    else:
        return '-'+coeff+'[csc('+inside+')]^(2)('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else '-'+coeff+'[csc('+inside+')]^(2)'

# Differentiates a Constant (for consistency)
def diffConstant(number):
    return '0'

# Performs some cleanup of the results of differentiation
def cleanup(function):
    if '<' in function or '>' in function:
        function=function.replace('<','(')
        function=function.replace('>',')')
    
    if '()' in function:
        function=function.replace('()','')

    if '+0' in function or '-0' in function:
        function=function.replace('+0','')
        function=function.replace('-0','')

    if '^(1.0)' in function or '^(1)' in function:
        function=function.replace('^(1.0)','')
        function=function.replace('^(1)','')
        
    if ')1' in function:
        function=function.replace(')1',')')

    if ')(1)' in function or '(1)(' in function:
        function=function.replace(')(1)',')')
        function=function.replace('(1)(','(')
        
    types=['cos','sin','tan','exp','csc','cot','sec','ln','arctan','arccos','arcsin','arccot','arcsec','arccsc','log_','x^','x']
    for typ in types:
        if '1'+typ in function or typ+'1' in function:
            function=function.replace('1'+typ,typ)
            function=function.replace(typ+'1',typ)

    return function

# Differentiates General Exponential Function
def diffExponential(function,variable):
    [coeff,coeffVar] = function.split('exp',1)
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '('+function+')('+diffMultiTerm(coeffVar[1:-1],variable)+')'
    else:
        return function+strParser(coeffVar[1:-1],variable)

# Differentiates Natural Log functions
def diffNaturalLog(function,variable):
    [coeff,coeffVar] = function.split('ln(',1)
    coeffVar=coeffVar[:-1]
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '('+coeff+')('+diffMultiTerm(coeffVar,variable)+')/('+coeffVar+')'
    else:
        return coeff+strParser(coeffVar,variable)+'/'+coeffVar

def diffLog(function,variable):
    [coeff,coeffVar] = function.split('log_',1)
    [base,argument] = coeffVar.split('(',1)
    if '+' or '-' in argument and checkLowestChain(coeffVar,variable)==True:
        return '('+coeff+')('+diffMultiTerm(argument,variable)+')/(ln('+base+')('+argument+'))'
    else:
        return '('+coeff+')('+strParser(argument,variable)+')/(ln('+base+')('+argument+'))'

# Differentiates Arctangent functions
def diffArctan(function,variable):
    [coeff,coeffVar] = function.split('arctan(',1)
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '('+coeff+')('+diffMultiTerm(coeffVar[:-1],variable)+')(1/(1+('+coeffVar[:-1]+')^2)'

    else:
        return '('+coeff+')('+strParser(coeffVar[:-1],variable)+')(1/(1+('+coeffVar[:-1]+')^2)'

# Differentiates Arcsine functions
def diffArcsin(function,variable):
    [coeff,coeffVar] = function.split('arcsin(',1)
    coeffVar=coeffVar[:-1]
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '('+coeff+')('+diffMultiTerm(coeffVar,variable) + ')(1/sqrt(1-('+coeffVar+')^2)'
    else:
        return '('+coeff+')('+strParser(coeffVar,variable) + ')(1/sqrt(1-('+coeffVar+')^2)'

# Differentiations Arccosine functions
def diffArccos(function,variable):
    [coeff,coeffVar] = function.split('arccos(',1)
    coeffVar=coeffVar[:-1]
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '(-1)('+coeff+')('+diffMultiTerm(coeffVar,variable) + ')(1/sqrt(1-('+coeffVar+')^2)'
    else:
        return '(-1)('+coeff+')('+strParser(coeffVar,variable) + ')(1/sqrt(1-('+coeffVar+')^2)'

# Differentiates Arccotangent functions
def diffArccot(function,variable):
    [coeff,coeffVar] = function.split('arccot(',1)
    coeffVar=coeffVar[:-1]
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '(-1)('+coeff+')('+diffMultiTerm(coeffVar,variable)+')(1/(1+('+coeffVar+')^2))'
    else:
        return '(-1)('+coeff+')('+strParser(coeffVar,variable)+')(1/(1+('+coeffVar+')^2))'

# Differentiates arcsecant functions
def diffArcsec(function,variable):
    [coeff,coeffVar] = function.split('arcsec(',1)
    coeffVar=coeffVar[:-1]
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '('+coeff+')('+diffMultiTerm(coeffVar,variable) + ')(1/(|'+coeffVar+'|sqrt(('+coeffVar+')^2+1))'
    else:
        return '('+coeff+')('+strParser(coeffVar,variable) + ')(1/(|'+coeffVar+'|sqrt(('+coeffVar+')^2+1))'

# Differentiates Arccosecant functions
def diffArccsc(function,variable):
    [coeff,coeffVar] = function.split('arccsc(',1)
    coeffVar=coeffVar[:-1]
    if '+' or '-' in coeffVar and checkLowestChain(coeffVar,variable)==True:
        return '(-1)('+coeff+')('+diffMultiTerm(coeffVar,variable) + ')(1/|'+coeffVar+'|sqrt(('+coeffVar+')^2+1))'
    else:
        return '(-1)('+coeff+')('+strParser(coeffVar,variable) + ')(1/|'+coeffVar+'|sqrt(('+coeffVar+')^2+1))'

# Differentiates functions that are separated by + and - operators
def diffMultiTerm(function,variable):
    [left,right]=[function,'']
    operations=[]
    terms = []
    diffedTerms=[]
    returnDiff=''
    while left !='':
    # Check for addition subtraction
        if '+' in left and '-' in left:
            if left.find('+')<left.find('-'):
                [left,right] = left.split('+',1)
                operations.append('+')
                terms.append(left)
                
            elif left.find('-')<left.find('+'):
                [left,right] = left.split('-',1)
                operations.append('-')
                terms.append(left)

        elif '+' in left and '-' not in left:
            [left,right] = left.split('+',1)
            operations.append('+')
            terms.append(left)

        elif '-' in left and '+' not in left:
            [left,right] = left.split('-',1)
            operations.append('-')
            terms.append(left)

        else:
            if len(terms)==0:
                terms.append(left)
            else:
                terms.append(right)
            left=''
 
    diffedTerms=[strParser(term,variable) for term in terms]
    counter=0
    for op in range(len(operations)):
        if operations[counter]=='-':
            diffedTerms[counter+1]='-'+diffedTerms[counter+1]
        counter+=1
        
    for trm in diffedTerms:
        if len(returnDiff)==0:
            returnDiff+=trm
        else:
            returnDiff+='+'+trm if '-' not in trm else trm
                           
    return returnDiff

# Parses the input to determine how to differentiate the term
def strParser(term,variable):
    if '(0)' in term:
        term='0'
        
    lowestTerm = chainRule(term,variable)
    if lowestTerm=='<':
        if '>*<' in term and '>/<' not in term:
            return productRule(term,variable)
        
        elif '>/<' in term and '>*<' not in term:
            return quotientRule(term,variable)
        
        elif '>/<' in term and '>*<' in term:
            if term.find('/')>term.find('*'):
                return quotientRule(term,variable)
            
            else:
                return productRule(term,variable)

    elif lowestTerm==']':
        return performTermCutting(term,variable)
    
    elif lowestTerm==']^':
        return exponentDiffRule(term,variable)

    elif lowestTerm=='cos':
        return diffCosine(term,variable)

    elif lowestTerm=='sin':
        return diffSine(term,variable)

    elif lowestTerm=='arctan':
        return diffArctan(term,variable)

    elif lowestTerm=='arcsin':
        return diffArcsin(term,variable)

    elif lowestTerm=='arccos':
        return diffArccos(term,variable)

    elif lowestTerm=='tan':
        return diffTan(term,variable)

    elif lowestTerm=='arccot':
        return diffArccot(term,variable)

    elif lowestTerm=='arccsc':
        return diffArccsc(term,variable)

    elif lowestTerm=='arcsec':
        return diffArcsec(term,variable)

    elif lowestTerm=='sec':
        return diffSec(term,variable)

    elif lowestTerm=='csc':
        return diffCsc(term,variable)

    elif lowestTerm=='cot':
        return diffCot(term,variable)

    elif lowestTerm=='exp':
        return diffExponential(term,variable)

    elif lowestTerm=='ln':
        return diffNaturalLog(term,variable)
    
    elif lowestTerm=='log_':
        return diffLog(term,variable)

    elif lowestTerm==variable+'^' or lowestTerm==variable:
        return polyRule(term,variable)

    elif lowestTerm=='const':
        return diffConstant(term)
    
    else:
        print('I don\'t know what this is.')

# Checks for the ordering of the chain; then, uses recurrsion to keep differentiating until the chain is complete
def chainRule(term,variable):
    # Checks for Outer most item for chain rule
    types=['<','cos','sin','tan','exp','csc','cot','sec','ln','arctan','arccos','arcsin','arccot','arcsec','arccsc','log_',variable+'^',variable]
    lowNum=10000
    currentLowest=''
    for typ in types:
        if typ in term:
            if(term.find(typ)<lowNum):
                lowNum=term.find(typ)
                currentLowest=typ

    if '[' in term and ']' in term and ']^' not in term:
        if(term.find('[')<lowNum):
            lowNum=term.find('[')
            currentLowest=']'

    elif '[' in term and ']^' in term:
        if(term.find('[')<lowNum):
            lowNum=term.find('[')
            currentLowest=']^'
            
    try:
        num = float(term)
        currentLowest='const'
    except:
        pass
            
    return currentLowest

# Differentiates products of functions
def productRule(function,variable):
    [pieceOne,pieceTwo] = function.split('>*<',1)
    [pieceOne,pieceTwo] = [pieceOne[1:],pieceTwo[:-1]]
    if '+' or '-' in pieceOne and '+' or '-' not in pieceTwo:
        return '('+diffMultiTerm(pieceOne,variable)+')('+pieceTwo+') + ('+pieceOne+')('+strParser(pieceTwo,variable)+')'

    elif '+' or '-' not in pieceOne and '+' or '-' in pieceTwo:
        return '('+strParser(pieceOne,variable)+')('+pieceTwo+') + ('+pieceOne+')('+diffMultiTerm(pieceTwo,variable)+')'

    elif '+' or '-' in pieceOne and '+' or '-' in pieceTwo:
        return '('+diffMultiTerm(pieceOne,variable)+')('+pieceTwo+') + ('+pieceOne+')('+diffMultiTerm(pieceTwo,variable)+')'

    else:
        return '('+strParser(pieceOne,variable)+')('+pieceTwo+') + ('+pieceOne+')('+strParser(pieceTwo,variable)+')'

# Differentiates quotients of functions
def quotientRule(function,variable):
    [numer,denom] = function.split('>/<',1)
    if '+' or '-' in numer and '+' or '-' not in denom:
        return '[('+denom+')('+diffMultiTerm(numer,variable)+') - ('+numer+')('+strParser(denom,variable)+')]/('+denom+')^2'

    elif '+' or '-' not in numer and '+' or '-' in denom:
        return '[('+denom+')('+strParser(numer,variable)+') - ('+numer+')('+diffMultiTerm(denom,variable)+')]/('+denom+')^2'

    elif '+' or '-' in numer and '+' or '-' in denom:
        return '[('+denom+')('+diffMultiTerm(numer,variable)+') - ('+numer+')('+diffMultiTerm(denom,variable)+')]/('+denom+')^2'
    
    else:
        return '[('+denom+')('+strParser(numer,variable)+') - ('+numer+')('+strParser(denom,variable)+')]/('+denom+')^2'

# Differentiates a funciton raised to a power
def exponentDiffRule(function,variable):
    [beg,middle] = function.split('[',1)
    [inner,outer] = middle.split(']^(',1)
    [power,rest] = outer.split(')',1)
    try:
        new_power = str(float(power)-1)
        if '+' or '-' in inner:
            return '('+power+')('+inner+')^('+new_power+')('+diffMultiTerm(inner,variable)+')'
        else:
            return '('+power+')('+inner+')^('+new_power+')('+strParser(inner,variable)+')'

    except:
        if outer[len(outer)-1] ==')' and outer[len(outer)-2] ==')':
            outer=outer[:-1]
        return function+'('+productRule('<ln('+inner+')>*<'+outer+'>','x')+')'

# Cuts terms via the character, @
def performTermCutting(function,variable):
    terms = function.split('@')
    operations = []
    diffedTerms=[]
    returnStatement=''
    
    if terms[0][0] != '+' or '-':
        operations.append('+')
        
    elif terms[0][0] == '-':
        operations.append('-')
        terms[0] = terms[0][1:]

    counter=1
    for item in terms[1:]:
        operations.append(item[0])
        terms[counter] = item[1:]
        if ' ' in terms[counter]:
            terms[counter] = terms[counter].replace(' ','')
        counter+=1
    
    for item in terms:
        diffedTerms.append(strParser(item,variable))
    
    numCount=0
    for item in diffedTerms:
        if returnStatement=='':
            if operations[0]=='-':
                returnStatement+='-('+item+')'
            else:
                returnStatement+='('+item+')'
                
        else:
            returnStatement+=operations[numCount]+'('+item+')'
        numCount+=1
    
    return returnStatement

# The 'UI' function for people to input functions to be differentiated
def performTotalDifferentiation():
    print('Type \'stop\' if you don\'t want to continue differentiating. Type \'help\' for how to use program.')
    print('\n')
    recursiveAsk()

# Just a way for people to continuously ask the program to differentiate different functions, as well as a way for the person to ask for help/quit out
def recursiveAsk():
    diffedFunction = input('Input the function you\'d like to be differentiated: ')

    if diffedFunction=='stop':
        print('Goodbye')

    elif diffedFunction=='help':
        print('Rules: \nIf you want to mult/div complex terms, type <term_1>*/<term_2>. For simple terms, just use term_1*/term_2.\nIf you want to raise a term to a power, type [term_1]^(power).\nIf you want to have a term have more than one addition/subtraction operation, type [term_1 + term_2+etc]*[term_3].\nAnd if you want to find the derivative of a sum of functions, type: term_1 @+ term_2 @+ term_3 etc. Use @- for subtraction.')
        print('\n')
        recursiveAsk()

    else:
        print('(d/dx)('+diffedFunction+') = '+cleanup(performTermCutting(diffedFunction,'x')))
        print('\n')
        recursiveAsk()
        
def checkLowestChain(function,variable):
    terms=[]
    if '+' in function and '-' not in function:
        terms= function.split('+')
        for item in terms:
            if chainRule(item,variable)==variable or chainRule(item,variable)==variable+'^' or chainRule(item,variable)=='const':
                pass
            else:
                return False
            
    elif '-' in function and '+' not in function:
        terms=function.split('-')
        if chainRule(item,variable)==variable or chainRule(item,variable)==variable+'^' or chainRule(item,variable)=='const':
            pass
        else:
            return False
        
    elif '+' in function and '-' in function:
        [left,right] = [function,'space']
        while right!='':
            if left.find('+')<left.find('-') or ('+' in left and '-' not in left):
                [left,right] = left.split('+',1)
                if chainRule(left,variable)==variable or chainRule(left,variable)==variable+'^' or chainRule(left,variable)=='const':
                    pass
                    
                else:
                    return False
                
            elif left.find('-')<left.find('+') or ('-' in left and '+' not in left):
                [left,right] = left.split('-',1)
                if chainRule(left,variable)==variable or chainRule(left,variable)==variable+'^' or chainRule(left,variable)=='const':
                    pass
                    
                else:
                    return False
                
                
            else:
                break
        
    else:
        return True
    
    return True
