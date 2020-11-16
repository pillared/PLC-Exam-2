#####################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
#####################################

"""
OPS.PY TAKES A WORD AS INPUT, AND FOR EACH LETTER
WILL CHECK ALL OPTIONS TO CHECK A VALID TOKEN
"""

# // – Addition --> '+'
# // – Assignment --> '='
# // – Subtraction --> '-'
# // – Multiplication --> '*'
# // – Increment --> '++' | '+='
# // – Decrement --> '--' | '-='
# // – Modulo Operator --> '%'
# // – Logical And --> '&&' | 'and'
# // – Logical Or --> '||' | 'or'
# // – Logical Not --> '!' | 'not'
# // – Open Code Block --> '{' 
# // – CloCode Block --> '}'
# // – Open Function parameter – '('
# // - CloFunction parameter --> '):'

def validateToken_Ops(char):
	if (char == '+' ):
		pass
	elif ( char == '-' ): # – Addition --> '+'  1lvl
		pass
	elif ( char == '='): # – Assignment --> '=' 1lvl
		pass
	elif ( char == '-'): # – Subtraction --> '-' 1lvl
		pass
	elif ( char == '/'): # – Division --> '/' 1lvl
		pass
	elif ( char == '*'): # – Multiplication --> '*' 1lvl
		pass
	elif ( char == '%'): # – Modulo Operator --> '%' 1lvl
		pass
	elif ( char == '++' or char == '+='): # – Increment --> '++' | '+='  2lvl
		pass	
	elif ( char == '--' or char == '-='): # – Decrement --> '--' | '-=' 2lvl
		pass
	elif ( char == '&&' or char == 'and'): # – Logical And --> '&&' | 'and' 2lvl
		pass
	elif ( char == '||' or char == 'or'): # – Logical Or --> '||' | 'or' 2lvl
		pass
	elif ( char == '!' or char == 'not'): # – Logical Not --> '!' | 'not' 1lvl
		pass
	elif ( char == '{'): # – Open Code Block --> '{' 1lvl
		pass
	elif ( char == '}'): # – CloCode Block --> '}' 1lvl
		pass
	elif ( char == '('): # – Open Function parameter – '(' 1lvl 
		pass
	elif ( char == ')'): # - CloFunction parameter --> '):' 1lvl
		pass
	else:
		return False
	return True

def main():
	trueWords = ['+', '-', '(', ')', 'or', 'and', '*', '/', '%']
	falseWords = ['lk', '!', 'nand', 'xor', 'ur mom', '*=', '==', '()', '[]']
	for word in trueWords:
		print(word)
		print(validateToken_Ops(word))
		print()
	for word in falseWords:
		print(word)
		print(validateToken_Ops(word))
		print()

if __name__ == "__main__":
	main()
