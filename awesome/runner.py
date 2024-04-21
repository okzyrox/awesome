from . import lex

def fromFile(inputFile):
    Lexer = lex.Lexer()

    with open(inputFile) as data:
        data = data.readlines()
    #print(data)

    Lexer.parseStr(data)