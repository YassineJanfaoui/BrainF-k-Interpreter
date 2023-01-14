band = [0]*3000
code = input("write your code here:\n")
pointer = 0
loopPointer = 0
i = 0
while i < len(code):
    if code[i] == '>':
        if pointer < 3000:
            pointer += 1
        else:
            print("Error: pointer points to undefined area,Above limit no loop")
            break
    elif code[i] == '<':
        if pointer != 0:
            pointer -= 1
        else:
            print("Error: pointer points to undefined area, below limit no loop")
            break
    elif code[i] == "+":
        band[pointer] += 1
    elif code[i] == "-":
        band[pointer] -= 1
    elif code[i] == "[":
        loopPointer = pointer
        j = i +1
        LoopCounter = 0
        LoopCharacter = 1
        while band[loopPointer] != 0:
            if code[j] == '>':
                if pointer < 3000:
                    pointer += 1
                    if LoopCounter == 0:
                        LoopCharacter += 1
                else:
                    print("Error: pointer points to undefined area, Above limit")
                    break
            elif code[j] == '<':
                if pointer != 0:
                    pointer -= 1
                    if LoopCounter == 0:
                        LoopCharacter += 1
                else:
                    print("Error: pointer points to undefined area, Below limit")
                    break
            elif code[j] == "+":
                band[pointer] += 1
                if LoopCounter == 0:
                        LoopCharacter += 1
            elif code[j] == "-":
                if code[j+1] != "]":
                    band[pointer] -= 1
                    if LoopCounter == 0:
                        LoopCharacter += 1
                else:
                    j = i 
                    band[loopPointer] -= 1
                    LoopCounter = 1
            j += 1
        i = j + LoopCharacter
    elif code[i] == ".":
        print(chr(band[pointer]),end="")
    i += 1
        
            




   


