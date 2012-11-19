#!/usr/bin/python

import sys
array = [0] * 1000
current = 0

def matching_brackets(cmds):
	'''
		Analyze a subsequence splitted with an index 
		if seq [0:n+1] #("[") == seq[0:n+1] #("]")
			equal number of brackets -> return subseq to recursive call
	'''

	index = 0
	while cmds[0:index+1].count("[") != cmds[0:index+1].count("]"):
		index += 1

	return cmds[1:index]

def execute(cmds):
	'''
		Recursive function:
			- handles brain**ck parsing (not ,)
			- prints to STDOUT
			- receives input from main with STDIN (raw_input())
	'''

	# defined globally because of recursion
	global current
	global array

	# actual recursion position
	pos = 0

	while pos < len(cmds):
		comm = cmds[pos]

		if comm == '+':
			array[current] += 1

		elif comm == '-':
			array[current] -= 1

		elif comm == '<':
			current -= 1

		elif comm == '>':
			current += 1

		elif comm == '.':
			# damn! print adds a blank space and my test fails!
			sys.stdout.write( chr(array[current]) )

		elif comm == '[':
			# must find the next matching brackets subsequence then call execute recursively
			valid_sub = matching_brackets(cmds[pos:])
			
			while array[current] != 0:
				# recursive call, if current = 0 all subcode is executed
				execute(valid_sub)
			# increases position to first non "]" char after
			pos += 1+len(valid_sub)

		pos +=1

if __name__=="__main__":
	execute('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.')