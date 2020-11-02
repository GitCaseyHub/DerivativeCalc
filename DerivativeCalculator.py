# Program to perform general differentiation

# Differentiations functions of the form: ax^(f(x))
def polyRule(function,variable):
    if '^' not in function:
        return '1'

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
            return '('+function+')'+productRule('<'+power+'>*<ln('+str(coefficient)+')','x')

# Differentiate Cosine Function
def diffCosine(function,variable):
    [coeff,inside] = function.split('cos(',1)
    inside=inside[:-1]
    return '-'+coeff+'sin('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable) != '1' else '-'+coeff+'sin('+inside+')'

# Differentiate Sine Function
def diffSine(function,variable):
    [coeff,inside] = function.split('sin(',1)
    inside=inside[:-1]
    return coeff+'cos('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else coeff+'cos('+inside+')'

# Differentiates Tangent Function
def diffTan(function,variable):
    [coeff,inside] = function.split('tan(',1)
    inside=inside[:-1]
    return coeff+'[sec('+inside+')]^(2)('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else coeff+'[sec('+inside+')]^(2)'

# Differentiates Secant Function
def diffCsc(function,variable):
    [coeff,inside] = function.split('csc(',1)
    inside=inside[:-1]
    return '-'+coeff+'csc('+inside+')cot('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else '-'+coeff+'csc('+inside+')cot('+inside+')'

# Differentiates Cosecant Function
def diffSec(function,variable):
    [coeff,inside] = function.split('sec(',1)
    inside=inside[:-1]
    return coeff+'sec('+inside+')tan('+inside+')('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else coeff+'sec('+inside+')tan('+inside+')'

# Differentiates Cotangent Function
def diffCot(function,variable):
    [coeff,inside] = function.split('cot(',1)
    inside=inside[:-1]
    return '-'+coeff+'[csc('+inside+')]^(2)('+strParser(inside,variable)+')' if strParser(inside,variable)!='1' else '-'+coeff+'[csc('+inside+')]^(2)'

# Differentiates a Constant (for consistency)
def diffConstant(number):
    return '0'

# Performs some cleanup of the results of differentiation
def cleanup(function):
    for holder in ['<','>','[',']']:
        if holder in function:
            function = function.replace(holder,'')

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
    return function+strParser(coeffVar[1:-1],variable)

# Differentiates Natural Log functions
def diffNaturalLog(function,variable):
    [coeff,coeffVar] = function.split('ln(',1)
    return coeff+strParser(coeffVar,variable)+'/'+coeffVar

def diffLog(function,variable):
    [coeff,coeffVar] = function.split('log_',1)
    [base,argument] = coeffVar.split('(',1)
    return coeff+'('+strParser(argument,variable)+')/(ln('+base+')'+argument

# Differentiates Arctangent functions
def diffArctan(function,variable):
    [coeff,coeffVar] = function.split('arctan(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return coeff+strParser(coeffVar,variable)+'1/1+('+coeffVar+')^2'

# Differentiates Arcsine functions
def diffArcsin(function,variable):
    [coeff,coeffVar] = function.split('arcsin(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return coeff+strParser(coeffVar,variable) + '1/sqrt(1-('+coeffVar+')^2)'

# Differentiations Arccosine functions
def diffArccos(function,variable):
    [coeff,coeffVar] = function.split('arccos(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return '(-1)'+coeff+strParser(coeffVar,variable) + '1/sqrt(1-('+coeffVar+')^2)'

# Differentiates Arccotangent functions
def diffArccot(function,variable):
    [coeff,coeffVar] = function.split('arccot(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return '(-1)'+coeff+strParser(coeffVar,variable)+'1/1+('+coeffVar+')^2'

# Differentiates arcsecant functions
def diffArcsec(function,variable):
    [coeff,coeffVar] = function.split('arcsec(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return coeff+strParser(coeffVar,variable) + '1/|'+coeffVar+'|sqrt(('+coeffVar+')^2+1)'

# Differentiates Arccosecant functions
def diffArccsc(function,variable):
    [coeff,coeffVar] = function.split('arccsc(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return '(-1)'+coeff+strParser(coeffVar,variable) + '1/|'+coeffVar+'|sqrt(('+coeffVar+')^2+1)'

# Differentiates functions that are separated by + and - operators
def diffMultiTerm(function,variable):
    terms = []
    diffedTerms = []
    # Check for addition subtraction
    if '+' in function and '-' in function:
        plusRemoval = function.split('+')

        for term in plusRemoval:
            if '-' in term:
                for sub in term.split('-'):
                    terms.append('-'+sub if sub==term.split('-')[1] else sub)

            else:
                terms.append(term)

    elif '-' in function and '+' not in function:
        preTerms = function.split('-')
        for term in preTerms:
            terms.append('-'+term if '-'+term in function else term)

        for term in terms:
            if term =='' or term=='+' or term=='-':
                terms.remove(term)

    elif '+' in function and '-' not in function:
        preTerms = function.split('+')
        for term in preTerms:
            terms.append(term)

    else:
        terms = [function]

    for item in terms:
        diffedTerms.append(strParser(item,variable))

    result = ""
    for dfs in diffedTerms:
        result=result+str(dfs)+'+'

    return result[:-1]

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

    elif '+' in term or '-' in term:
        return diffMultiTerm(term,variable)

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

    else:
        return diffConstant(term)

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
    return currentLowest

# Differentiates products of functions
def productRule(function,variable):
    [pieceOne,pieceTwo] = function.split('>*<',1)
    [pieceOne,pieceTwo]= [pieceOne[1:],pieceTwo[:-1]]
    return '('+strParser(pieceOne,variable)+')('+pieceTwo+') + ('+pieceOne+')('+strParser(pieceTwo,variable)+')'

# Differentiates quotients of functions
def quotientRule(function,variable):
    [numer,denom] = function.split('>/<',1)
    [numer,denom] = [numer[1:],denom[:-1]]
    return '[('+denom+')('+strParser(numer,variable)+') - ('+numer+')('+strParser(denom,variable)+')]/('+denom+')^2'

# Differentiates a funciton raised to a power
def exponentDiffRule(function,variable):
    [beg,middle] = function.split('[',1)
    [inner,outer] = middle.split(']^(',1)
    [power,rest] = outer.split(')',1)
    try:
        new_power = str(float(power)-1)
        return power+'('+inner+')^('+new_power+')'+strParser(inner,variable)

    except:
        return function+productRule('<ln('+inner+')>*<'+power+'>','x')

# Appropriately cuts + and - operators from terms so that terms parititioned by [ ] are left alone
def performTermCutting(function,variable):
    terms=[]
    diffedTerms=[]
    if '[' in function and ']' in function and ('+' in function or '-' in function) and (function.find('[')<function.find('+') and function.find('+')<function.find(']')) or (function.find('[')<function.find('+') and function.find('-')<function.find(']')):
        [outer,inner]=[function,'']
        counter=1
        while outer!='':
            if outer.find('+')<outer.find('-') or ('-' not in outer and '+' in outer):
                [originalOuter,originalInner] = [outer,inner]
                [outer,inner] = ['+'.join(outer.split('+')[:counter]), '+'.join(outer.split('+')[counter:])]
                if '[' in outer and ']' not in outer:
                    counter+=1
                    [outer,inner]=[originalOuter,originalInner]

                elif ('[' in outer and ']' in outer) or ('[' not in outer and ']' not in outer):
                    terms.append(outer)
                    diffedTerms.append(strParser(outer,variable))
                    counter=1
                    [outer,inner]=[inner,'']

            elif outer.find('-')<outer.find('+') or ('+' in outer and '-' not in other):
                [originalOuter,originalInner]=[outer,inner]
                [outer,inner]='-'.join(outer.split('-')[:counter]), '-'.join(outer.split('-')[counter:])
                if '[' in outer and ']' not in outer:
                    counter+=1
                    [outer,inner]=[originalOuter,originalInner]

                elif ('[' in outer and ']' in outer) or ('[' not in outer and ']' not in outer):
                    terms.append(outer)
                    diffedTerms.append(strParser(outer,variable))
                    counter=1
                    [outer,inner] = [inner,'']

            else:
                terms.append(outer)
                diffedTerms.append(strParser(outer,variable))
                outer=''

        wholeDeriv = ''

        for term in diffedTerms:
            wholeDeriv+=term+'+'
        return wholeDeriv[:-1]

    else:
        return strParser(function,variable)

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
        print('Rules: \nIf you want to mult/div complex terms, type <term_1>*/<term_2>. For simple terms, just use term_1*/term_2.\nIf you want to raise a term to a power, type [term_1]^(power).\nIf you want to have a term have more than one addition/subtraction operation, type [term_1 + term_2+etc]')
        print('\n')
        recursiveAsk()

    else:
        print('(d/dx)('+diffedFunction+') = '+cleanup(performTermCutting(diffedFunction,'x')))
        print('\n')
        recursiveAsk()
