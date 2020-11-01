# Program to perform general differentiation

# Differentiates Single Polynomial Term
def polyRule(function,variable):
    if '^' not in function:
        return function.split(variable)[0] if len(function)!=1 else '1'
    
    else:
        [coefficient,power] = function.split('^')
        if '(' in power or ')' in power:
            power=power.replace('(','')
            power=power.replace(')','')
        elif '<' in power or '>' in power:
            power=power.replace('<','')
            power = power.replace('>','')
            
        coefficient = 1 if coefficient[:-1] == '' else coefficient[:-1]
        new_power = "^"+str(float(power)-1) if float(power)-1 !=1 else ""
        return '('+power+variable+new_power+')' if coefficient is "" else '('+str(float(coefficient)*float(power))+variable+new_power+')'
    
# Differentiate Cosine Function
def diffCosine(function,variable):
    [coeff,inside] = function.split('cos(',1)
    return '-'+coeff+'sin('+inside+strParser(inside,variable) if strParser(inside,variable) != '1' else '-'+coeff+'sin('+inside+')'

# Differentiate Sine Function
def diffSine(function,variable):
    [coeff,inside] = function.split('sin(',1)
    return coeff+'cos('+inside+strParser(inside,variable) if strParser(inside,variable)!='1' else coeff+'cos('+inside
    
# Differentiates a Constant (for consistency)
def diffConstant(number):
    return '0'

def cleanup(function):
    checkers = ['<','>','[',']']
    for holder in checkers:
        if holder in function:
            function = function.replace(holder,'')
            
    if '+0' in function or '-0' in function:
        function=function.replace('+0','')
        function=function.replace('-0','')
        
    if '(1)' in function:
        function=function.replace('(1)','')
        
    if '^(1.0)' in function or '^(1)' in function:
        function=function.replace('^(1.0)','')
        function=function.replace('^(1)','')
            
    return function

# Differentiates General Exponential Function
def diffExponential(function,variable):
    [coeff,coeffVar] = function.split('exp',1)
    return function+strParser(coeffVar[1:-1],variable)

def diffNaturalLog(function,variable):
    [coeff,coeffVar] = function.split('ln(',1)
    return coeff+strParser(coeffVar,variable)+'/'+coeffVar

def diffArctan(function,variable):
    [coeff,coeffVar] = function.split('arctan(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return coeff+strParser(coeffVar,variable)+'1/1+('+coeffVar+')^2'
    
def diffArcsin(function,variable):
    [coeff,coeffVar] = function.split('arcsin(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return coeff+strParser(coeffVar,variable) + '1/sqrt(1-('+coeffVar+')^2)'
    
def diffArccos(function,variable):
    [coeff,coeffVar] = function.split('arccos(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return '(-1)'+coeff+strParser(coeffVar,variable) + '1/sqrt(1-('+coeffVar+')^2)'
    
def diffArccot(function,variable):
    [coeff,coeffVar] = function.split('arccot(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return '(-1)'+coeff+strParser(coeffVar,variable)+'1/1+('+coeffVar+')^2'

def diffArcsec(function,variable):
    [coeff,coeffVar] = function.split('arcsec(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return coeff+strParser(coeffVar,variable) + '1/|'+coeffVar+'|sqrt(('+coeffVar+')^2+1)'
    
def diffArccsc(function,variable):
    [coeff,coeffVar] = function.split('arccsc(',1)
    if ')' in coeffVar:
        coeffVar.replace(')','')
    return '(-1)'+coeff+strParser(coeffVar,variable) + '1/|'+coeffVar+'|sqrt(('+coeffVar+')^2+1)'
    
# Will be the final thing to implement; need to figure out how to find individual terms
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
    lowestTerm = chainRule(term,variable)
    
    if '>*<' in term:
        return productRule(term,variable)
    
    elif '>/<' in term:
        return quotientRule(term,variable)
    
    elif lowestTerm==']^':
        return exponentDiffRule(term,variable)
    
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
        inside = term.split('tan(')[1][:-1]
        outside = term.split('tan')[0]
        return quotientRule('(sin('+inside+'))/(cos('+inside+'))',variable)
    
    elif lowestTerm=='arccot':
        return diffArccot(term,variable)
    
    elif lowestTerm=='arccsc':
        return diffArccsc(term,variable)
    
    elif lowestTerm=='arcsec':
        return diffArcsec(term,variable)
    
    elif lowestTerm=='sec':
        inside = term.split('sec(')[1][:-1]
        return quotientRule('1/cos('+inside+')',variable)
        
    elif lowestTerm=='csc':
        inside = term.split('csc(')[1][:-1]
        return quotientRule('1/sin('+inside+')',variable)
    
    elif lowestTerm=='cot':
        inside = term.split('cot(')[1][:-1]
        outside = term.split('cot')[0]
        return quotientRule('(cos('+inside+'))/(sin('+inside+'))',variable)
    
    elif lowestTerm=='exp':
        return diffExponential(term,variable)
    
    elif lowestTerm=='ln':
        return diffNaturalLogarithm(term,variable)
    
    elif '*' in term:
        return productRule(term,variable)
        
    elif '/' in term:
        return quotientRule(term,variable)
    
    elif lowestTerm==variable+'^' or lowestTerm==variable:
        return polyRule(term,variable)
    
    else:
        return diffConstant(term)

# Checks for the ordering of the chain; then, uses recurrsion to keep differentiating until the chain is complete
def chainRule(term,variable):
    # Checks for Outer most item for chain rule
    types=['cos','sin','tan','exp','csc','cot','sec','ln','arctan','arccos','arcsin','arccot','arcsec','arccsc',variable+'^',variable]
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

def productRule(function,variable):
    if '*' in function and '>*<' not in function:
        [pieceOne,pieceTwo] = function.split('*',1)

        
    elif '>*<' in function:
        [pieceOne,pieceTwo] = function.split('>*<',1)

    return cleanup(strParser(pieceOne,variable)+pieceTwo+' + '+pieceOne+strParser(pieceTwo,variable))


def quotientRule(function,variable):
    returnStatement=''
    if '/' in function and '>/<' not in function:
        [numer,denom] = function.split('/',1)
        returnStatement= '('+denom+strParser(numer,variable)+' - '+numer+strParser(denom,variable)+'/'+denom+')^2'
        
    elif '>/<' in function:
        [numer,denom] = function.split('>/<',1)
        returnStatement= '('+denom+strParser(numer[1:],variable)+' - '+numer+strParser(denom[:-1],variable)+')/('+denom[:-1]+')^2'
    
    return cleanup(returnStatement)
    
# Differentiates a funciton raised to a power
def exponentDiffRule(function,variable):
    [beg,middle] = function.split('[',1)
    [inner,outer] = middle.split(']^(',1)
    [power,rest] = outer.split(')',1)
    new_power = str(float(power)-1)
    
    return power+'('+inner+')^('+new_power+')'+strParser(inner,variable)

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
        
def performTotalDifferentiation():
    print('Type \'stop\' if you don\'t want to continue differentiating. Type \'help\' for how to use program.')
    print('\n')
    recursiveAsk()
    
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