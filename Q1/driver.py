#####################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
#####################################

"""
DRIVER.PY TAKES A TEXT FILE AS INPUT, AND FOR EACH STRING
WILL CHECK ALL FUNCTIONS TO FIND A VALID TOKEN
"""


from perl import validateToken_Perl
from javastring import validateToken_JavaString
from cint import validateToken_cInt
from cchar import validateToken_cChar
from cfloat import validateToken_cFloat
from ops import validateToken_Ops

import sys

def main():
    # a giant list of test words for function matching
    token={ 

        'token_A' : 'Perl',
        'token_B' : 'JavaString',
        'token_C' : 'cInt',
        'token_D' : 'cChar',
        'token_E' : 'cFloat',
        'token_F' : 'Ops'
        
    }
    arr = []
    string = ""  
    filex = open("q1.txt", "r")
    string = filex.read()
    arr = string.split( )
    print(arr)
    filex.close()
    ans = None
    xo= None

    for word in arr:
        # pass to all of the validations
        # if true, let it be known what token type that word is
        print(word)
        for each in token.values():
            try:
                # eval function
                xo = "validateToken_" + each + "(" + word + ")"
                # call each specific function to test same word.
                if(eval(xo)):
                    ans = each
                    print("TOKEN FOUND :", word, "is:", each, ans)
            except SyntaxError:
                pass
        print('\n')  


if __name__ == "__main__":
    main()