#####################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
#####################################

"""
CINT.PY TAKES A WORD AS INPUT, AND FOR EACH LETTER
WILL CHECK ALL OPTIONS TO CHECK A VALID TOKEN
"""

import sys

"""
    int                 dec_int    = 28;
    unsigned            dec_uint   = 4000000024u;
    long                dec_long   = 2000000022l;
    unsigned long       dec_ulong  = 4000000000ul;
    long long           dec_llong  = 9000000000LL;
    unsigned long long  dec_ullong = 900000000001ull;

    /* Octal Constants */
    int                 oct_int    = 024;
    unsigned            oct_uint   = 04000000024u;
    long                oct_long   = 02000000022l;
    unsigned long       oct_ulong  = 04000000000UL;
    long long           oct_llong  = 044000000000000ll;
    unsigned long long  oct_ullong = 044400000000000001Ull;

    /* Hexadecimal Constants */
    int                 hex_int    = 0x2a;
    unsigned            hex_uint   = 0XA0000024u;
    long                hex_long   = 0x20000022l;
    unsigned long       hex_ulong  = 0XA0000021uL;
    long long           hex_llong  = 0x8a000000000000ll;
    unsigned long long  hex_ullong = 0x8A40000000000010uLL;
"""


bits={
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'a':'a',
    'A':'A',
    'b':'b',
    'B':'B',
    'c':'c',
    'C':'C',
    'd':'d',
    'D':'D',
    'e':'e',
    'E':'E',
    'f':'f',
    'F':'F',
    'prefix_x':'x',
    'prefix_X':'X',
    'unsigned_u':'u',
    'unsigned_U':'U',
    'long_l':'l',
    'long_L':'L',
    'long_ll':'ll',
    'long_LL':'LL',
}
valid_dec = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}
valid_hex = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'a':'a',
    'A':'A',
    'b':'b',
    'B':'B',
    'c':'c',
    'C':'C',
    'd':'d',
    'D':'D',
    'e':'e',
    'E':'E',
    'f':'f',
    'F':'F',
}

valid_oct={
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
}

suffix={
    'prefix_x':'x',
    'prefix_X':'X',
    'unsigned_u':'u',
    'unsigned_U':'U',
    'long_l':'l',
    'long_L':'L',
    
}

def split(word):
    return [char for char in word]

def validateToken_cInt(arr):

    identifier = None
    previous = None
    next = None
    isHex = False
    isDecimal = False
    isOctal = False
    neverHex = False
    neverDecimal = False
    neverOctal = False
    first = None
    second = None
    firstSuffix = None
    noMoreHexPlease = False
    noMoreDecPlease = False
    noMoreOctPlease = False
    unsigned = False #u
    _long = False #l
    unsignedlong = False #ul
    _longlong = False #ll
    unsigned_longlong = False #ull
    ucount = 0
    lcount = 0
    
    for char in arr:
        if(char in bits.values()):
            if(isOctal):
                if(char in valid_oct.values()):
                    pass
                else:
                    if(firstSuffix == None):
                        noMoreOctPlease = True
                        if(char == 'u' or char == 'U'):
                            ucount+=1
                            unsigned = True
                        elif(char == 'l'):
                            lcount+=1
                            _long = True
                        else:
                            return False
                        firstSuffix = char
                        previous = firstSuffix
                    elif(noMoreOctPlease):
                        if(lcount > 2 or ucount > 1):
                            print(lcount,ucount)
                            return False
                        elif(previous == 'u'):
                            
                            unsigned = True
                            if(char is not None):
                                return False
                        elif(previous == 'l'):
                            if(firstSuffix == 'U' and char == 'l'):
                                lcount+=1
                                unsigned_longlong = True
                            elif(char == 'l'):
                                lcount+=1
                                _longlong = True
                            else:
                                return False
                        elif(previous == 'U'):
                            if(char == 'l' or char == 'L'):
                                lcount+=1
                                unsignedlong = True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False

            elif(isDecimal):
                if(char in valid_dec.values()):
                    pass
                else:
                    if(firstSuffix == None):
                        noMoreDecPlease = True
                        if(char == 'u'):
                            ucount+=1
                            unsigned = True
                        elif(char == 'l'):
                            lcount+=1
                            _long = True
                        elif(char == 'L'):
                            lcount+=1
                            _long = True
                        else:
                            return False
                        firstSuffix = char
                        previous = firstSuffix
                    elif(noMoreDecPlease):
                        print(lcount,ucount)
                        if(lcount > 2 or ucount > 1):
                            print(lcount,ucount)
                            return False
                        elif(previous == 'u'):
                            if(char == 'l'):
                                lcount+=1
                                unsignedlong = True
                                #print('unsignedlong = true')
                            elif(char != 'l'):
                                return False
                        elif(previous == 'l'):
                            if(firstSuffix == 'u' and char == 'l'):
                                lcount+=1
                                unsigned_longlong = True
                                #print('longlong = true')
                            elif(char == 'l'):
                                lcount+=1
                                _longlong = True
                            elif(char != 'l'):
                                return False
                            
                        elif(previous == 'L'):
                            if(char == 'L'):
                                lcount+=1
                                unsigned_longlong = True
                                #print('unsignedlonglong = true')
                        else:
                            return False
                    else:
                        return False
            elif(isHex):
                if(char in valid_hex.values()):
                    #print("no worries, only a hex value")
                    pass
                else:
                    if(firstSuffix == None):
                        noMoreHexPlease = True
                        if(char == 'u'):
                            ucount+=1
                            unsigned = True
                            #print('unsigned = true')
                        elif(char == 'l'):
                            lcount+=1
                            _long = True
                            #print('long = true')
                        else:
                            return False
                        firstSuffix = char
                        previous = firstSuffix
                    elif(noMoreHexPlease):
                        if(lcount > 2 or ucount > 1):
                            print(lcount, ucount)
                            return False
                        elif(previous == 'u'):
                            if(char == 'L'):
                                lcount+=1
                                unsignedlong = True
                                #print('unsignedlong = true')
                            elif(char != 'L'):
                                return False
                        elif(previous == 'l'):
                            if(char == 'l'):
                                lcount+=1
                                _longlong = True
                                #print('longlong = true')
                            elif(char != 'l'):
                                return False
                        elif(previous == 'L'):
                            if(char == 'L'):
                                lcount+=1
                                unsigned_longlong = True
                                #print('unsignedlonglong = true')
                        else:
                            return False
                    else:
                        return False
            elif(first == None):
                if(char != '0'):
                    neverHex = True
                    neverOctal = True
                    isDecimal = True
                    print("is Decimal")
                first = char
            elif(first == "0" and second == None):
                # the next can be a numer or it can be x for hex or b for binary
                second = char
                if(char == 'x' or char == 'X'):
                    print('is Hex')
                    neverOctal = True
                    neverDecimal = True
                    isOctal = False
                    isHex = True
                elif(char != 0):
                    print('is Octal')
                    neverDecimal = True
                    isOctal = True
                    isHex = False
                else:
                    pass #print('wtf')
            
            else:
                return False
        
        else:
            return False
        previous = char
        if(lcount > 2 or ucount > 1):
            print(lcount, ucount)
            return False 
    return True

def main():

    trueWords = ["28","4000000024u","2000000022l","4000000000ul","9000000000LL","900000000001ull","024","04000000024u","02000000022l","04000000000UL", "044000000000000ll","044400000000000001Ull", "0x2a","0XA0000024u", "0x20000022l","0XA0000021uL", "0x8a000000000000ll", "0x8A40000000000010uLL"]
    falseWords = ['28', '4000000024ulll', '2000000022lll', '4000000000uul', '9000000000LLL', '900000000001ulll', '024', '04000000024uu', '02000000022ll', '04000000000ULL', '044000000000000uull', '044400000000000001Ulll', '0x2a', '0XA0000024uu', '0x20000022ll','0XA0000021uLLL','0x8a000000000000lll','0x8A40000000000010uLLL']

    for word in falseWords:
        if( validateToken_cInt(word) ):
            print(str(word) + "  -----VALID------")
        else:
            print(str(word) + "  -----ERROR------")
        print()


if __name__ == "__main__":
    main()
