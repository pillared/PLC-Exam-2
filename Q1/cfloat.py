#####################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
#####################################

"""
CFLOAT.PY TAKES A WORD AS INPUT, AND FOR EACH LETTER
WILL CHECK ALL OPTIONS TO CHECK A VALID TOKEN
"""

"""
15.75
1.575E1   /* = 15.75   */
1575e-2   /* = 15.75   */
-2.5e-3   /* = -0.0025 */
25E-4  

10.0L  /* Has type long double  */
10.0F  /* Has type float        */

.0075e2
0.075e1
.075e1
75e-2
"""

import sys

bits={
    'num0' : '0',
    'num1' : '1',
    'num2' : '2',
    'num3' : '3',
    'num4' : '4',
    'num5' : '5',
    'num6' : '6',
    'num7' : '7',
    'num8' : '8',
    'num9' : '9',
    'minus' : '-',
    'plus' : '+',
    'let_e' : 'e',
    'let_E' : 'E',
    'let_l' : 'l',
    'let_L' : 'L',
    'let_f' : 'f',
    'let_F' : 'F',
    'dec' : '.'
}

def split(word): 
    return [char for char in word]  

def validateToken_cFloat(arr):
    identifier = None
    first = None
    previous = None
    next = []
    firstIsDec = False
    allowDec = True
    allowE = True
    allowL = True
    allowF = True
    allowSign = True
    allowP = True
    noMore = False
    for char in arr:
        if (noMore):
            return False
        elif(char in bits.values()):            
            if (identifier == None):
                identifier = char
                first = char
                if(char.isnumeric()):
                    next = ["e", ".", '0-9']
                elif(char == "."): 
                    firstIsDec = True
                    allowDec = False
                    next = ['0-9']
                elif(char == "-"):
                    next = ['.', '0-9']
                else:
                    return False
            else:   
                if( char.isnumeric() ):
                    previous = char
                elif(allowDec and char == "."):
                    allowDec = False
                    if(firstIsDec):
                        return False
                    previous = char
                    next = ['0-9']
                elif(previous.isnumeric()):
                    if(allowE and (char == 'e' or char =='E')):
                        allowE = False
                        allowL = False
                        allowF = False
                        previous = char
                    elif(allowL and (char == 'l' or char =='L')):
                        allowE = False
                        allowL = False
                        allowF = False
                        noMore = True
                        previous = char
                    elif(allowF and (char == 'f' or char =='F')):
                        allowE = False
                        allowL = False
                        allowF = False
                        noMore = True
                        previous = char
                    else:
                        return False
                elif(allowSign and (char == "+" or char == "-")):
                    allowSign = False
                elif(allowSign == False):
                    return False    
                else:
                    return False
        else:
            return False  
    return True

def main():

    trueWords = ["15.75", "1.575E1", "1575e-2", "-2.5e-3", "25E-4", "10.0L", "10.0F", ".0075e2", "0.075e1", ".075e1", "75e-2"]
    falseWords = ["15.L75L", "1.57.5E1", "157.5e-+", "+2.5e-3", "25.L-4", "10.0LF", "1x0.0F", ".0075ef2", "0.075ee1", ".075e1f", "75e--2"]

    for word in trueWords:
        arr = split(word)
        print(word, validateToken_cFloat(arr))
        print('\n')

    for word in falseWords:
        arr = split(word)
        print(word, validateToken_cFloat(arr))
        print('\n')
    


if __name__ == "__main__":
    main()
