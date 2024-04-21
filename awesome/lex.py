# lexer


CONSTANTS = [
    'let',

    'string',
    'int',
    'bool',
    'true',
    'false',
    'null',

    'print'
]

def unpack(lis):
    x = lis

class Lexer():
    def __init__(self) -> None:
        self.functions = {}
        self.variables = {}
        self.calls = {}
        self.builtins = {
            "true": True,
            "false": False,
            "null": None,
        }
    
    def getTrueType(self, string):
        x = {
            'string':str,
            'int':int,
            'bool':bool,
        }
        return x[string]

    def getTypeOf(self, val, as_string = False):
        try:
            int(val)
            if as_string:
                return "int"
            return int
        except:
            pass
        
        print(val)
    
    def val(self, index):
        return self.variables[index][1]

    def math(self, num1, num2, operator):
        match operator:
            case "+": return int(num1) + int(num2)
            case "-": return int(num1) - int(num2)
            case "*": return int(num1) * int(num2)
            case "/": return int(num1) / int(num2)
            case "=": return int(num2)
        
    
    def run(self):
        print("Executing")

    def parseStr(self, input: list[str]):
        # part 1
        data = input
        full = ""
        lines:list[str] = []
        for line in data:
            full += line

        for val in full:
            val = val.replace("\n", ";")

        lines = full.split("\n")
        
        # interpet

        for line in lines:
            count = 0
            sep = line.split(' ')
            print("1", sep)

            try:
                if sep[0] == "let":
                    line_type = sep[1]
                    line_variable = sep[2]
                    line_operator = sep[3]
                    line_value = sep[4]
                    print("yes")
                    if line_operator == '=':
                        print("yesyesy")
                        if line_type == "string":
                            if line_value.startswith("\"") and line_value.endswith("\""):

                                self.variables[line_variable] = (self.getTrueType(line_type), line_value)
                            else:
                                raise Exception(f"Type mismatch!, Line {count}: \ncannot asign {line_value} of type {self.getTypeOf(line_value, True)} to variable of type {line_type}")
                        elif line_type == "int":
                            print("yesyesyes")
                            print(line_variable)
                            print(self.variables)
                            # just stops running here???
                            self.variables.get(line_variable)
                            if self.variables[line_variable] == None:
                                print("hello????????")
                                self.variables[line_variable] = (self.getTrueType(line_type), line_value)
                            else:
                                print("hi????????")
                                decl = self.variables[line_variable]

                                decl_type = decl[0]
                else:
                    
                    declare = sep[0]
                    if sep[0] not in CONSTANTS:
                        x = self.variables[declare]
                        if not sep[2].startswith("("):
                            ## if the types are the same
                            var_type = self.getTypeOf(sep[4])
                            if var_type == x[0]:
                                self.variables[declare] = (var_type, self.math(x[1], sep[4], sep[3]))
                            else:

                                
                                raise Exception(
                                    f""" Type mismatch!
                                        {x[1]} of type {x[0]} cannot become type {var_type}
                                    """
                                )
                count += 1
            except Exception as runtimeError:
                print(runtimeError)
                exit(-1)

        print(self.val('x'))


