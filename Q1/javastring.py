#####################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
#####################################

"""
JAVASTRING.PY TAKES A WORD AS INPUT, AND FOR EACH LETTER
WILL CHECK ALL OPTIONS TO CHECK A VALID TOKEN
"""

import sys


"""
VALID
String s = "a dog jumped over the fucking moon!!";
String s = "N@I)INR@ )(#B ";
String s = "OI #OR\"NJ O#";
String s = "n210h_8";
String s = "";
String

Carriage return and newline: "\r" and "\n"
Backslash: "\\\\"
Single quote: "\'"
Horizontal tab and form feed: "\t" and "\f"

System.out.println('a'); //a
"""

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
    'symbol21' : ' ' ,
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
validbits = {
    't':'t',
    'r':'r',
    'n':'n',
    'f':'f',
    '"':'"',
    "'":"'",
    '\\':'\\',

}

def validateToken_JavaString(arr):
    identifier = None
    previous = None
    next = None
    isSlash = False
    isDoubleSlash = False
    first = None
    size = 0
    count = 0

    for char in arr:
        size = len(arr)
        if( count == 0  and first == None):
            if(char == "\""):
                first = char
                previous = char
            else:
                return False
        elif(count == size-1 ):
            if(char == '\"'):
                return True
            else:
                return False
        elif(isSlash == True):
            if(char in validbits.values()):
                pass
            elif(char == "\\"):
                isDoubleSlash = True
                isSlash = False
            else:
                return False
        elif(first != None):
            if(char in bits.values()):
                pass
            elif(char == "\\"):
                isSlash = True 
            else:
                return False
        else:
            return False  
        
        count+=1


def main():
    print('test')

    testStrings = ['"a"', '"string"', '"str ing\\t"', '"string\\"', '"stri\\"s"', '"st \\ \" ri\\"s"', "valid??@123", '"valisd@@@/.,[][33\\{1!@#$%"']
    for word in testStrings:
        print(word)
        print('\t' + str(validateToken_JavaString(word)))
        print()
        

if __name__ == '__main__':
    main()
    