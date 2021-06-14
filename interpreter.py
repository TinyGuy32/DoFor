import time
data = {"OUTPUT":"",
        "INPUT":""}
on = 0
file = open(input("Code file:"),"r")
code = file.read()

while on < len(code):
    if code[on] == "D" and code[on+1] == "O":
        on += 3
        action = ""
        while code[on] != " ":
            action += code[on]
            on += 1
        on += 1
        Type = ""
        setTo = ""
        saveTo = ""
        while code[on] != " ":
            Type += code[on]
            on += 1
        on += 1
        while code[on] != "_":
            setTo += code[on]
            on += 1
        on += 1
        if code[on] == "F" and code[on+1] == "O" and code[on+2] == "R":
            on += 4
            while code[on] != ";":
                saveTo += code[on]
                on += 1
        if action == "SET":
            if setTo == "INPUT":
                if Type == "STR":
                    data[saveTo] = str(input())
                if Type == "INT":
                    data[saveTo] = int(input())
                if Type == "VAR":
                    data[saveTo] = data[setTo]
            elif Type == "STR":
                data[saveTo] = str(setTo)
            elif Type == "INT":
                data[saveTo] = int(setTo)
            elif Type == "VAR":
                data[saveTo] = data[setTo]
            elif Type == "CON":
                checkOn = 0
                check1=""
                check2=""
                comparison = ""
                while setTo[checkOn] != "<" and setTo[checkOn] != "=":
                    check1 += setTo[checkOn]
                    checkOn += 1
                comparison = setTo[checkOn]
                checkOn += 1
                while checkOn < len(setTo):
                    check2 += setTo[checkOn]
                    checkOn += 1
                if comparison == "<":
                    data[saveTo] = data[check1] < data[check2]
                elif comparison == "=":
                    data[saveTo] = data[check1] == data[check2]
        elif action == "ADD":
            if setTo == "INPUT":
                if Type == "STR":
                    data[saveTo] += str(input())
                if Type == "INT":
                    data[saveTo] += int(input())
                if Type == "VAR":
                    data[saveTo] += data[setTo]
            elif Type == "STR":
                data[saveTo] += str(setTo)
            elif Type == "INT":
                data[saveTo] += int(setTo)
            elif Type == "VAR":
                data[saveTo] += data[setTo]
    if code[on] == "I" and code[on+1] == "F":
        on += 2
        if code[on] == "(":
            on += 1
            CheckVar = ""
            while code[on] != ")":
                CheckVar += code[on]
                on += 1
            on += 1
            if code[on] == "{":
                ifs=1
                on += 1
                if data[CheckVar] == False:
                    while ifs > 0:
                        if code[on] == "{":
                            ifs += 1
                        if code[on] == "}":
                            ifs -= 1
                        on += 1
    if code[on] == "L" and code[on+1] == "A" and code[on+2] == "B" and code[on+3] == "E" and code[on+4] == "L":
        on += 6
        label = ""
        while code[on] != ";":
            label += code[on]
            on += 1
        data[label] = on
    if code[on] == "G" and code[on+1] == "O" and code[on+2] == "T" and code[on+3] == "O":
        on += 5
        label = ""
        while code[on] != ";":
            label += code[on]
            on += 1
        on = data[label]
    if data["OUTPUT"] != "":
        print(data["OUTPUT"])
        data["OUTPUT"] = ""
            
            
                
    on += 1
time.sleep(100)
