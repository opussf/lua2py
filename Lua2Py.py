"""
 * Lua2Py.py
 ****************************************
 * This script reads a file with Lua data structures
 * and loads them into a python data structure.
 *
"""


def printParseTree(children, text, depth=0):

	for child in children:
		print "\t"*depth,
		print child[0], "=",
		print text[child[1]:child[2]]
		if child[3]:
		  printParseTree(child[3],text,depth+1)


from simpleparse.common import numbers, strings, comments

declaration = r'''# note use of raw string when embedding in python code...
file           :=  [ \t\n]*, section+
section        :=  '[',identifier!,']'!, ts,'\n', body
body           :=  statement*
statement      :=  (ts,semicolon_comment)/equality/nullline
nullline       :=  ts,'\n'
equality       :=  ts, identifier,ts,'=',ts,identified,ts,'\n'
identifier     :=  [a-zA-Z], [a-zA-Z0-9_]*
identified     :=  string/number/identifier
ts             :=  [ \t]*
'''

#dictionary		:=  identifier/key, ts, '=', ts, '{', assignment/dictionary+ ,'}', ','*


declaration = r'''
file				:=  [ \t\n]*, dictionary+
dictionary		:=  '{', ts, dkv*, ts
assignment		:=  identifier/key, ts, '=', ts, '{', ts, dkv*, ts
dkv				:=  dictionary/key_value
key_value		:=  key, ts, '=', ts, identified, ts, ',', ts
key				:=  '[', identified, ']'
identifier		:=  [a-zA-Z], [a-zA-Z0-9_]*
identified		:=  string/number/identifier
ts					:=  [ \n\t]*
'''



from simpleparse.parser import Parser
parser = Parser(declaration, "file")


luaStr = file("C:\Program Files\World of Warcraft\WTF\Account\OPUSSF\SavedVariables\GuildBanker.lua","r").read()
#luaStr = """GUILDBANKER_STOCK = { ["Hyjal"] = { [1] = { [1] = "Hello", }} }\n"""
success, resultTrees, nextCharacter = parser.parse( luaStr )


print resultTrees
printParseTree(resultTrees, luaStr)




class Lua2Py(object):

	tokenVariable = ""

	def __init__(self,stringIn):
		self.luaStr=stringIn
		self.__parseString()

	def __parseString(self):
		pass
		#print self.luaStr


if __name__=="__main__":
	import unittest

	class testLua2Py(unittest.TestCase):

		def setUp(self):
			luaStr = file("C:\Program Files\World of Warcraft\WTF\Account\OPUSSF\SavedVariables\GuildBanker.lua","r").read()
			self.myTest = Lua2Py(luaStr)

		def testCreation_01(self):
			luaStr = file("C:\Program Files\World of Warcraft\WTF\Account\OPUSSF\SavedVariables\GuildBanker.lua","r").read()
			myCreation = Lua2Py(luaStr)
			self.failUnless(myCreation)

		def testCreation_02(self):
			luaStr = """GUILDBANKER_ROSTER = {
							["Hyjal"] = {
								[1] = {
									[1] = "Sistersally",
									[2] = 244000,
									[3] = "Miner / Gnomish Engineer",
								},
							},
						}
"""
			myCreation = Lua2Py("GuildBanker.lua")
			self.failUnless(myCreation)



	unittest.main()
