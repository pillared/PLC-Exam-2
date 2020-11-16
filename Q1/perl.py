#####################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
#####################################

"""
PERL.PY TAKES A WORD AS INPUT, AND FOR EACH LETTER
WILL CHECK ALL OPTIONS TO CHECK A VALID TOKEN
"""

import sys
bits={
    'dollar' : '$',
    'at' : '@',
    'perc' : '%',
    'und' : '_',
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
    'BEGIN' : 1,
    'NEXT' : None
}
def split(word): 
    return [char for char in word]  

def validateToken_Perl(arr):
    identifier = None
    for char in arr:
        # and isnumeric() for numbers, otherwise check hard code wise
        if(char in bits.values()):
            # Make sure that identifier only happens once!!!! otherwise FAIl 
            if (identifier == None):
                if( (char == "$" or char == "%" or char == "@")):
                    identifier = char
                    #first letter, make sure doesnt happen again in word...
                    #make sure from now on letters, underscore, numbers,...
                    #print(char)
                else:
                    return False
            else:
                if( char.isalnum() or char == "_"):
                    pass
                else:
                    return False
        else:
            return False
    return True

def main():
    print("CORRECT PERL WORDS INCLUDE")
    print("$nwi_nw")
    print("@nwif13")
    print("%nwfm_n2ei\n")

    print("INCORRECT PERL WORDS INCLUDE")
    print("$nwi_#nw")
    print("@nwif%13")
    print("%nw@m_n2ei\n")

    print("OUR PERLWORD")
    perlword = '$nq93b'
    arr = split(perlword)
    print(perlword)
    print(arr)
    
    if( validateToken_Perl(arr) ):
        print("Arr is a PERL!")
    else:
        sys.exit("ERROR FAILED PARSING OF TOKEN ")

    """for key, value in bits.items():
        print(key, ' : ', value)"""


if __name__ == "__main__":
    main()

