from functools import reduce
import operator
import os

os.system ("cls")

print ("\033[1;32m")

with open ("Hade.txt", "r") as file :

    lines = file.readlines ()

    contents = [line.strip () for line in lines if line.strip () and not line.strip ().startswith ("//") and not line.strip ().startswith ("/*") and not line.strip ().endswith ("*/")]

global variables
variables = {}

global memory
memory = []

global code

for code in contents :

    code = code.replace ("\n\n", "\n")
    code = code.replace ("\n\n\n", "\n")
    code = code.replace ("\n\n\n\n", "\n")
    code = code.replace ("\n\n\n\n\n", "\n")
    code = code.replace ("\n\n\n\n\n\n", "\n")
    code = code.replace ("\n\n\n\n\n\n\n", "\n")
    code = code.replace ("\n\n\n\n\n\n\n\n", "\n")
    code = code.replace ("\n\n\n\n\n\n\n\n\n", "\n")
    code = code.replace ("\n\n\n\n\n\n\n\n\n\n", "\n")

    if ("\\n" in code) :

        code = code.replace ("\\n", "\n").replace ("\"", "'''").replace ("'", "'''")

    if ("\\t" in code) :

        code = code.replace ("", "\t")
    
    if not code :

        pass
    
    if ("if" not in code) and (";" in code) :

        code = code.replace (";", "")

    if ("if" not in code) and ("print" not in code) and ("+" in code or "-" in code or "*" in code or "/" in code or "%" in code) and (code.replace ("(", "").replace (")", "").replace (" ", "").replace ("+", "").replace ("-", "").replace ("*", "").replace ("/", "").replace ("%", "").isdigit () == True) :

        if "/" in code :

            try :
                
                result = eval (code)
            
            except :

                # Zero_Division_Error ()
                2 == 2

        else :
            
            result = eval (code)
            print (result)
    
    if ("if" not in code) and ("print" in code) and ("+" in code or "-" in code or "*" in code or "/" in code or "%" in code) and (code.replace ("(", "").replace (")", "").replace (" ", "").replace ("+", "").replace ("-", "").replace ("*", "").replace ("/", "").replace ("%", "").replace ("print", "").isdigit () == True) :

        lol = code.replace ("print", "")
        result = eval (lol)
        print (result)
    
    if ("add" not in code) and ("sub" not in code) and ("mul" not in code) and ("div" not in code) and ("pow" not in code) and ("mod" not in code) and ("if" not in code) and ("print" in code) and ("{n}" not in code) and ("type_of" not in code) and ("eval" not in code) and (("\"" in code) or ("'" in code)) and ("{{" not in code) and (code.replace ("(", "").replace (")", "").replace (" ", "").replace ("+", "").replace ("-", "").replace ("*", "").replace ("/", "").replace ("%", "").isdigit () == False) :

        string = code.replace ("print", "").replace ("\"", "").replace ("'", "")
        print (str (string).rstrip ())

    if ("if" not in code) and ("=" in code) and ("let" in code) and ("scan" not in code) and ("{n}" not in code) :

        parts = code.split ("=")

        global variable_name
        variable_name = parts [0].replace (" ", "").replace ("let", "")
        global variable_value
        variable_value = parts [1].strip ()

        variables [variable_name] = eval (variable_value)
    
    if ("if" not in code) and ("print" in code) and ("{{" in code) and ("}}" in code) :

        words = code.split ()
        new_line = ""

        for word in words :

            if "{{" in word and "}}" in word :

                variable_name = word [word.find ("{{") + 2 : word.find ("}}")]

                if variable_name in variables :

                    word = str (variables [variable_name])

            new_line += word + " "

        print (new_line.replace ("print", "").lstrip ().replace ("\"", "").replace ("'", ""))
    
    if ("if" not in code) and ("scan" in code) and ("=" in code) and ("let" in code) :
       
        variable_name = code.split ("=") [0].strip ().replace ("let", "")
        
        user_input = input (code.split ("scan") [1].strip ().replace ("\"", "").replace ("'", ""))
        
        variables [variable_name.replace (" ", "")] = user_input
    
    if ("if" not in code) and ("print" in code) and ("{{" not in code) and ("+" not in code or "-" not in code or "*" not in code or "/" not in code or "%" not in code) :

        words = code.split ()

        for word in words :

            if word in variables :

                print (variables [word])

    if ("if" not in code) and ("print" in code) and ("type_of" in code) and ("(" in code) and (")" in code) :

        variable_name = code.replace (" ", "").split ("type_of(") [1].split (")")[0].strip ()
        
        if variable_name in variables :
            
            variable_type = type (variables[variable_name]).__name__
            
            if str (variable_type) == "str" :

                print ("String { str } Datatype")
            
            elif str (variable_type) == "int" :

                print ("Integer { int } Datatype")
            
            elif str (variable_type) == "list" :

                print ("List { list } Datatype")

            elif str (variable_type) == "dict" :

                print ("Dictionary { dict } Datatype")
            
            elif str (variable_type) == "float" :

                print ("Floating Point { float } Datatype")
            
            elif str (variable_type) == "bool" :

                print ("Boolean { bool } Datatype")
            
            else :

                print ("None { None } Datatype")
        
        else :
            
            if ("'" in variable_name) or ("\"" in variable_name) and (variable_name.startswith ("[") == False) and (variable_name.startswith ("{") == False) :

                print ("String { str } Datatype")
            
            elif variable_name.isdigit () == True :

                print ("Integer { int } Datatype")
            
            elif "[" in variable_name and "]" in variable_name and (variable_name.startswith ("[") == True) :

                print ("List { list } Datatype")

            elif "{" in variable_name and "}" in variable_name and (variable_name.startswith ("{") == True) :

                print ("Dictionary { dict } Datatype")
            
            elif ("." in variable_name) and (variable_name.replace (".", "").replace (" ", "").isnumeric () == True) :

                print ("Floating Point { float } Datatype")
            
            elif (variable_name == "True") or (variable_name == "False") :

                print ("Boolean { bool } Datatype")
            
            else :

                print ("None { None } Datatype")   

    if ("if" not in code) and ("console.color=" in code.replace (" ", "")) :

        color = str (code.replace (" ", "").replace ("console.color=", "").replace ("\"", "").replace ("'", "").lower ())

        if (color == "blue") :

            print ("\033[1;34m", end = "")
        
        elif (color == "s_blue") :

            print ("\033[0;34m", end = "")
        
        elif (color == "white") :

            print ("\033[0;m", end = "")
        
        elif (color == "green") :

            print ("\033[1;32m", end = "")
        
        elif (color == "s_green") :

            print ("\033[0;32m", end = "")
        
        elif (color == "red") :

            print ("\033[1;31m", end = "")
        
        elif (color == "s_red") :

            print ("\033[0;31m", end = "")
        
        elif (color == "black") :

            print ("\033[0;30m", end = "")
        
        elif (color == "brown") :

            print ("\033[1;33m", end = "")
        
        elif (color == "s_brown") :

            print ("\033[0;33m", end = "")        

        elif (color == "purple") :

            print ("\033[1;35m", end = "")
        
        elif (color == "s_purple") :

            print ("\033[0;35m", end = "")
        
        elif (color == "cyan") :

            print ("\033[1;36m", end = "")
        
        elif (color == "s_cyan") :

            print ("\033[0;36m", end = "")
        
        elif (color == "light_grey") :

            print ("\033[0;37m", end = "")
        
        elif (color == "dark_grey") :

            print ("\033[1;30m", end = "")
        
        elif (color == "yellow") :

            print ("\033[1;33m", end = "")
        
        elif (color == "s_yellow") :

            print ("\033[0;36m", end = "")
        
        elif (color == "bold_state") :

            print ("\033[1m", end = "")
    
    if ("if" not in code) and ("print" in code) and ("eval" in code) and (("\"" in code) or ("'" in code)) and ("+" in code or "-" in code or "*" in code or "/" in code or "%" in code) :

        expr = code.replace (" ", "").replace ("print", "").replace ("eval", "").replace ("(", "").replace (")", "").replace ("\"", "").replace ("'", "")
        
        try :

            result = eval (expr)
            print (result)
        
        except :

            # Zero_Division_Error ()
            2 == 2

    if (code.startswith ("if")) :

        print ("Bye")
    
    if ("print" in code) and ("add" in code) and ("(" in code) and (")" in code) and (code.replace (" ", "").replace ("print", "").replace (",", "").replace ("add", "").replace ("(", "").replace (")", "").isdigit () == True ) :

        bro = code.replace (" ", "").replace ("add", "").replace ("(", "").replace (")", "").replace ("print", "").split (",")

        for i in range (len (bro)) :

            bro [i] = int (bro [i])

        result = reduce (operator.add, bro)

        print (result)
    
    if ("print" in code) and ("sub" in code) and ("(" in code) and (")" in code) and (code.replace (" ", "").replace ("print", "").replace (",", "").replace ("sub", "").replace ("(", "").replace (")", "").isdigit () == True ) :

        bro = code.replace (" ", "").replace ("sub", "").replace ("(", "").replace (")", "").replace ("print", "").split (",")
        
        for i in range (len (bro)) :

            bro [i] = int (bro [i])

        result = reduce (operator.sub, bro)

        print (result)
    
    if ("print" in code) and ("mul" in code) and ("(" in code) and (")" in code) and (code.replace (" ", "").replace ("print", "").replace (",", "").replace ("mul", "").replace ("(", "").replace (")", "").isdigit () == True ) :

        bro = code.replace (" ", "").replace ("mul", "").replace ("(", "").replace (")", "").replace ("print", "").split (",")
        
        for i in range (len (bro)) :

            bro [i] = int (bro [i])

        result = reduce (operator.mul, bro)

        print (result)
    
    if ("print" in code) and ("div" in code) and ("(" in code) and (")" in code) and (code.replace (" ", "").replace ("print", "").replace (",", "").replace ("div", "").replace ("(", "").replace (")", "").isdigit () == True ) :

        bro = code.replace (" ", "").replace ("div", "").replace ("(", "").replace (")", "").replace ("print", "").split (",")
        
        for i in range (len (bro)) :

            bro [i] = int (bro [i])

        result = reduce (operator.truediv, bro)

        print (result)
    
    if ("print" in code) and ("mod" in code) and ("(" in code) and (")" in code) and (code.replace (" ", "").replace ("print", "").replace (",", "").replace ("mod", "").replace ("(", "").replace (")", "").isdigit () == True ) :

        bro = code.replace (" ", "").replace ("mod", "").replace ("(", "").replace (")", "").replace ("print", "").split (",")
        
        for i in range (len (bro)) :

            bro [i] = int (bro [i])

        result = reduce (operator.mod, bro)

        print (result)
    
    if ("print" in code) and ("pow" in code) and ("(" in code) and (")" in code) and (code.replace (" ", "").replace ("print", "").replace (",", "").replace ("pow", "").replace ("(", "").replace (")", "").isdigit () == True ) :

        bro = code.replace (" ", "").replace ("pow", "").replace ("(", "").replace (")", "").replace ("print", "").split (",")
        
        for i in range (len (bro)) :

            bro [i] = int (bro [i])

        result = reduce (operator.pow, bro)

        print (result)
    
    if ("assign_memory" in code) and ("(" in code) and (")" in code) :

        string = code.replace ("(", "").replace ("assign_memory", "").replace (")", "").replace ("\"", "").replace ("'", "").lstrip ().rstrip ().split ("&&")
        
        for strings in string : 

            memory.append (str (strings).lstrip ().rstrip ())
    
    if ("push" in code) and ("(" in code) and (")" in code) :

        for memories in memory :

            print (memories)
    
    if ("pop" in code) and ("(" in code) and (")" in code) :

        element = code.replace ("pop", "").replace ("(", "").replace (")", "").replace ("\"", "").replace ("'", "").rstrip ()
        memory = [i for i in memory if i != element.lstrip ()] 
    
    if ("free" in code) and ("(" in code) and (")" in code) :

        memory.clear ()

print ("\n")
