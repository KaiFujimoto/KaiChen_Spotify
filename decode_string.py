def decodeString(string):
    """
    sample input: "5[s]5[o]4[b]3[z]"
    sample output: "sssssooooobbbbzzz"
    assumption(s) => 1. There won't be an imput like 3a or 2[3]
    2. All brackets will close itself (because I'm assuming no mean people) like "3[4".
    3. Numbers are positive.
    4. Overall, the goodwill of the person running my code that they will be nice. (have mercy plox)
    5. Person running my code likes notes. If not, then apologies QQ.

    """
    stack = [["", 1]] # my accumulator
    current_digit = "" # tracking the amount of times I have to repeat a letter
    for char in string: # iterating through each character in the string
        if char.isdigit(): # check if the character is a number
            current_digit += char # if the character is a number, I will set it to current_digit
        elif char == "[": # check if character is a bracket
            stack.append(["", int(current_digit)]) # if it is, the bracket signifies a new beginning/accumulator, so I will create a new accumulator with the current digit.
            current_digit = "" # will set the current digit back to null so we don't use it again
        elif char == "]": # check if we are at the end of an accumulation/bracket
            save_stack = stack.pop() # if we are at the end, we pop of the last stack/accumulation
            character = save_stack[0] # the character in the last stack
            number_to_print = save_stack[1] # the number of times to repeat that character
            stack[-1][0] += character * number_to_print # push that solution into the previous stack/accumulator (I previously pushed it to my first accumulator, but that didn't work because it took the end result of the stack and threw it at the first one. Made me sad. But I found the bug~~~)
        else:
            stack[-1][0] += char # if it is a letter, nice and boringly put it into the latest stack/accumulator
    return stack[0][0] # assuming all the brackets have been sealed and things, we should have our answer at homebase aka at [0][0]

print(decodeString("5[s]5[o]4[b]3[z]")) #woooo~ testing things because its fun~
