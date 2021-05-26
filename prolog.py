from pyswip import Prolog
prolog = Prolog()
prolog.consult("khanfamily.pl")
TGREEN =  '\033[32m' # Green Text
print (TGREEN + "")
menu = """
Which Relation You Want to Find......?
Press :
                                        1  for baap     11 for bahu
                                        2  for maa      12 for damad
                                        4  for beti     14 for poti
                                        3  for beta     13 for pota
                                        5  for dada     15 for nawasa1
                                        6  for dadi     16 for nawasi
                                        7  for nana     17 for sussar
                                        8  for nani     18 for chachataya
                                        9  for sala     19 for khala 
                                        10 for sali     20 for baap dada     
                                
"""
display_menu="Y"
while display_menu!="E":
    print(menu)
    choice = int(input("Enter Your Choice From Menu (1-20) : "))
    if choice < 1 or choice > 20:
        print("Invalid Choice.......")
    elif(choice == 1):
        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"baap(X,{name})"):
                print(soln["X"], "is the father of", name,)
                
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is father of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"baap(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
            print("         Invalid Choice........")        


    elif(choice == 2):

            choice2 = input("""
            Enter 'a' for simple query
            Enter 'b' for validating query
            """).lower().replace(" ", "")
            if choice2 == "a":
                name = input("Enter Name: ").lower().replace(" ", "")
                if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                    print("Relation Doesnot Exist")
                for soln in prolog.query(f"maa(X,{name})"):
                    print(soln["X"], "is the mother of", name)
            elif choice2 == "b":
                fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is mother of : ").lower().replace(" ", "")
                if len(list(prolog.query(f"maa(X,{fact2})"))) == 0:
                    print("false")
                else:
                    for soln in prolog.query(f"maa(X,{fact2})"):
                        if(soln["X"] == fact1):
                            istrue = True
                            break
                        else:
                            istrue = False
                    print(istrue)
            else:
                print("         Invalid Choice........")          


    elif(choice == 3):

            choice2 = input("""
            Enter 'a' for simple query
            Enter 'b' for validating query
            """).lower().replace(" ", "")
            if choice2 == "a":
                name = input("Enter Name: ").lower().replace(" ", "")
                if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                    print("Relation Doesnot Exist")
                for soln in prolog.query(f"beta(X,{name})"):
                    print(soln["X"], "is the son of", name)
            elif choice2 == "b":
                fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is son of : ").lower().replace(" ", "")
                if len(list(prolog.query(f"beta(X,{fact2})"))) == 0:
                    print("false")
                else:
                    for soln in prolog.query(f"beta(X,{fact2})"):
                        if(soln["X"] == fact1):
                            istrue = True
                            break
                        else:
                            istrue = False
                    print(istrue)
            else:
                print("         Invalid Choice........")         

    elif(choice == 4):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"beti(X,{name})"):
                print(soln["X"], "is the daughter of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is daughter of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"beti(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"beti(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
            print("         Invalid Choice........")         
    elif(choice == 5):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"dada(X,{name})"):
                print(soln["X"], "is the dada of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is dada of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"dada(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"dada(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 6):
            name = input("Enter Name: ").lower().replace(" ", "")
            for soln in prolog.query(f"dadi(X,{name})"):
                print(soln["X"], "is the dadi of", name)
            choice2 = input("""
            Enter 'a' for simple query
            Enter 'b' for validating query
            """).lower().replace(" ", "")
            if choice2 == "a":
                name = input("Enter Name: ").lower().replace(" ", "")
                if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                    print("Relation Doesnot Exist")
                for soln in prolog.query(f"dadi(X,{name})"):
                    print(soln["X"], "is the dadi of", name)
            elif choice2 == "b":
                fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is dadi of : ").lower().replace(" ", "")
                if len(list(prolog.query(f"dadi(X,{fact2})"))) == 0:
                    print("false")
                else:
                    for soln in prolog.query(f"dadi(X,{fact2})"):
                        if(soln["X"] == fact1):
                            istrue = True
                            break
                        else:
                            istrue = False
                    print(istrue)
            else:
                print("         Invalid Choice........")         

    elif(choice == 7):

            choice2 = input("""
            Enter 'a' for simple query
            Enter 'b' for validating query
            """).lower().replace(" ", "")
            if choice2 == "a":
                name = input("Enter Name: ").lower().replace(" ", "")
                if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                    print("Relation Doesnot Exist")
                for soln in prolog.query(f"nana(X,{name})"):
                    print(soln["X"], "is the nana of", name)
            elif choice2 == "b":
                fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is nana of : ").lower().replace(" ", "")
                if len(list(prolog.query(f"nana(X,{fact2})"))) == 0:
                    print("false")
                else:
                    for soln in prolog.query(f"nana(X,{fact2})"):
                        if(soln["X"] == fact1):
                            istrue = True
                            break
                        else:
                            istrue = False
                    print(istrue)
            else:
                print("         Invalid Choice........")         
    elif(choice == 8):

            choice2 = input("""
            Enter 'a' for simple query
            Enter 'b' for validating query
            """).lower().replace(" ", "")
            if choice2 == "a":
                name = input("Enter Name: ").lower().replace(" ", "")
                if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                    print("Relation Doesnot Exist")
                for soln in prolog.query(f"nani(X,{name})"):
                    print(soln["X"], "is the nani of", name)
            elif choice2 == "b":
                fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is nani of : ").lower().replace(" ", "")
                if len(list(prolog.query(f"nani(X,{fact2})"))) == 0:
                    print("false")
                else:
                    for soln in prolog.query(f"nani(X,{fact2})"):
                        if(soln["X"] == fact1):
                            istrue = True
                            break
                        else:
                            istrue = False
                    print(istrue)
            else:
                print("         Invalid Choice........")         
    elif(choice == 9):

            choice2 = input("""
            Enter 'a' for simple query
            Enter 'b' for validating query
            """).lower().replace(" ", "")
            if choice2 == "a":
                name = input("Enter Name: ").lower().replace(" ", "")
                if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                    print("Relation Doesnot Exist")
                for soln in prolog.query(f"sala(X,{name})"):
                    print(soln["X"], "is the sala of", name)
            elif choice2 == "b":
                fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is sala of : ").lower().replace(" ", "")
                if len(list(prolog.query(f"sala(X,{fact2})"))) == 0:
                    print("false")
                else:
                    for soln in prolog.query(f"sala(X,{fact2})"):
                        if(soln["X"] == fact1):
                            istrue = True
                            break
                        else:
                            istrue = False
                    print(istrue)
            else:
                print("         Invalid Choice........")         

    elif(choice == 10):

            choice2 = input("""
            Enter 'a' for simple query
            Enter 'b' for validating query
            """).lower().replace(" ", "")
            if choice2 == "a":
                name = input("Enter Name: ").lower().replace(" ", "")
                if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                    print("Relation Doesnot Exist")
                for soln in prolog.query(f"sali(X,{name})"):
                    print(soln["X"], "is the sali of", name)
            elif choice2 == "b":
                fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is sali of : ").lower().replace(" ", "")
                if len(list(prolog.query(f"sali(X,{fact2})"))) == 0:
                    print("false")
                else:
                    for soln in prolog.query(f"sali(X,{fact2})"):
                        if(soln["X"] == fact1):
                            istrue = True
                            break
                        else:
                            istrue = False
                    print(istrue)
            else:
                print("         Invalid Choice........")         
    elif(choice == 11):
        name = input("Enter Name: ").lower().replace(" ", "")
        for soln in prolog.query(f"bahu(X,{name})"):
            print(soln["X"], "is the bahu of", name)
        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"bahu(X,{name})"):
                print(soln["X"], "is the bahu of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is bahu of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"bahu(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"bahu(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         


    elif(choice == 12):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"damad(X,{name})"):
                print(soln["X"], "is the damad of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is damad of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"damad(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"damad(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
            print("         Invalid Choice........") 

    elif(choice == 13):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"pota(X,{name})"):
                print(soln["X"], "is the pota of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is pota of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"pota(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"pota(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 14):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"poti(X,{name})"):
                print(soln["X"], "is the poti of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is poti of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"poti(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"poti(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 15):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"nawasa(X,{name})"):
                print(soln["X"], "is the nawasa of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is nawasa of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"nawasa(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"nawasa(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 16):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"nawasi(X,{name})"):
                print(soln["X"], "is the nawasi of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is nawasi of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"nawasi(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"nawasi(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 17):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"sassur(X,{name})"):
                print(soln["X"], "is the sassur of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is sassur of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"sassur(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"sassur(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 18):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"chachataya(X,{name})"):
                print(soln["X"], "is the chachataya of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is chachataya of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"chachataya(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"chachataya(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 19):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"khala(X,{name})"):
                print(soln["X"], "is the khala of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is khala of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"khala(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"khala(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")         
    elif(choice == 20):

        choice2 = input("""
        Enter 'a' for simple query
        Enter 'b' for validating query
        """).lower().replace(" ", "")
        if choice2 == "a":
            name = input("Enter Name: ").lower().replace(" ", "")
            if len(list(prolog.query(f"baap(X,{name})"))) == 0:
                print("Relation Doesnot Exist")
            for soln in prolog.query(f"baapdada(X,{name})"):
                print(soln["X"], "is the baapdada of", name)
        elif choice2 == "b":
            fact1, fact2 = input("fact 1 : ").lower().replace(" ", ""), input("is baapdada of : ").lower().replace(" ", "")
            if len(list(prolog.query(f"baapdada(X,{fact2})"))) == 0:
                print("false")
            else:
                for soln in prolog.query(f"baapdada(X,{fact2})"):
                    if(soln["X"] == fact1):
                        istrue = True
                        break
                    else:
                        istrue = False
                print(istrue)
        else:
                print("         Invalid Choice........")      
                
    display_menu=input("Press any key to continue or E to Exit : ").upper()              
       
