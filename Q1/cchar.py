#####################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
#####################################

"""
CCHAR.PY TAKES A WORD AS INPUT, AND FOR EACH LETTER
WILL CHECK ALL OPTIONS TO CHECK A VALID TOKEN
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
    'letA' : 'A',
    'letB' : 'B',
    'letC' : 'C',
    'letD' : 'D',
    'letE' : 'E',
    'letF' : 'F',
    'letG' : 'G',
    'letH' : 'H',
    'letI' : 'I',
    'letJ' : 'J',
    'letK' : 'K',
    'letL' : 'L',
    'letM' : 'M',
    'letN' : 'N',
    'letO' : 'O',
    'letP' : 'P',
    'letQ' : 'Q',
    'letR' : 'R',
    'letS' : 'S',
    'letT' : 'T',
    'letU' : 'U',
    'letV' : 'V',
    'letW' : 'W',
    'letX' : 'X',
    'letY' : 'Y',
    'letZ' : 'Z',
    'leta' : 'a',
    'letb' : 'b',
    'letc' : 'c',
    'letd' : 'd',
    'lete' : 'e',
    'letf' : 'f',
    'letg' : 'g',
    'leth' : 'h',
    'leti' : 'i',
    'letj' : 'j',
    'letk' : 'k',
    'letl' : 'l',
    'letm' : 'm',
    'letn' : 'n',
    'leto' : 'o',
    'letp' : 'p',
    'letq' : 'q',
    'letr' : 'r',
    'lets' : 's',
    'lett' : 't',
    'letu' : 'u',
    'letv' : 'v',
    'letw' : 'w',
    'letx' : 'x',
    'lety' : 'y',
    'letz' : 'z',
    'symbol0' : '~' ,
    'symbol1' : '`' ,
    'symbol2' : '!' ,
    'symbol3' : '@' ,
    'symbol4' : '#' ,
    'symbol5' : '$' ,
    'symbol6' : '%' ,
    'symbol7' : '^' ,
    'symbol8' : '&' ,
    'symbol9' : '*' ,
    'symbol10' : '(' ,
    'symbol11' : ')' ,
    'symbol12' : '-' ,
    'symbol13' : '_' ,
    'symbol14' : '+' ,
    'symbol15' : '=' ,
    'symbol16' : '{' ,
    'symbol17' : '[' ,
    'symbol18' : '}' ,
    'symbol19' : ']' ,
    'symbol20' : '|' ,
    'symbol21' : '\\' ,
    'symbol22' : ':' ,
    'symbol23' : ';' ,
    'symbol24' : '"' ,
    'symbol25' : "'" ,
    'symbol26' : '<',
    'symbol27' : ',',
    'symbol28' : '>',
    'symbol29' : '.',
    'symbol30' : '?',
    'symbol31' : '/',
    'BEGIN' : 1,
    'NEXT' : None
}




#\b	Backspace
#\f	Form feed
#\n	New line
#\r	Carriage return
#\t	Horizontal tab
#\”	Double quote
#\’	Single quote
#\\	Backslash
#\v	Vertical tab
#\a	Alert or bell
#\?	Question mark
#\N	Octal constant (N is an octal constant)
#\XN	Hexadecimal constant (N – hex.dcml cnst)


def split(word): 
    return [char for char in word]  

def validateToken_cChar(arr):
    size = len(arr)
    count = 1
    identifier = None
    first = None
    last = None
    previous = None
    next = []
    firstIsQuotation = False
    allowBackSlashChar = True
    isX = False
    noMore = False
    doubleSlash = False
    for char in arr:

        print(char)
        if (noMore):
            return False
        if(count == size):
            if(char != last):
                return False
        elif(char in bits.values()):            
            if (identifier == None):
                if(char == '\"' or char == "\'" ):
                    identifier = char
                    first = char
                    last = char
                else:
                    return False
            else:   
                if(previous == '\\'):
                    if(char == 'b'):
                        pass
                    elif(char == 'f'):
                        pass
                    elif(char == 'n'):
                        pass
                    elif(char == 'r'):
                        pass
                    elif(char == 't'):
                        pass
                    elif(char == '"'):
                        pass
                    elif(char == "'"):
                        pass
                    elif(char == '\\'):
                        doubleSlash = True
                        pass
                    elif(char == 'v'):
                        pass
                    elif(char == 'a'):
                        pass
                    elif(char == '?'):
                        pass
                    elif(char == 'N'):
                        pass
                    elif(char == 'X'):
                        isX = True
                        pass
                    else:
                        return False
                elif(char =="\\"):
                    previous = char
                elif(previous == "X" and isX):
                    if(char == "N"):
                        pass
                    else:
                        return False
                else:
                    previous = char

        else:
            return False  
        count+=1
    return True

def main():

    trueWords = ["\'2\'", "\'!\'", "\"&\"", "\'\n\'", "\'\?\'", "\'\\\'", "\'\f\'", "\'\XN\'", "\']\'", "\'n\'"]
    falseWords = ['\'x\"' , "a\'c\'",  ""]

    for word in trueWords:
        arr = split(word)
        print(word, validateToken_cChar(arr))
        print('\n')

    for word in falseWords:
        arr = split(word)
        print(word, validateToken_cChar(arr))
        print('\n')

if __name__ == "__main__":
    main()
