
class Lexer():
    A = 1
    B = 2
    C = 3
    EOF = 99
    Error = -1

    inputString = ""
    currentPos = 0
    lookahead = ''

    def __init__(self):
        self.inputString = input("Por favor entrar una frase sin espacios ")


    def nextToken(self):
        ret = self.Error
        if (self.currentPos==len(self.inputString)):
            return self.EOF
        lookahead = self.inputString[self.currentPos]
        currentPos +=1

        if(lookahead == 'a'):
            return self.A
        elif (lookahead=='b'):
            return self.B
        elif (lookahead=='c'):
            return self.C
        else:
            print("Error lexico en el simbolo",lookahead,"no es valido")
        return ret

class Parser():
    Lexer = Lexer()
    nextToken = 0

    def __init__(self,lexer):
        self.Lexer = lexer
        self.nextToken = self.Lexer.nextToken()

