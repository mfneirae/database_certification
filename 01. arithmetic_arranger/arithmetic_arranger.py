def arithmetic_arranger(base, answer=False):
    if len(base) > 5:
        return "Error: Too many problems."    
    addend_top = []
    addent_bot = []
    operators = []

    for pieces in base:
        parts = pieces.split()
        addend_top.append(parts[0])
        operators.append(parts[1])
        addent_bot.append(parts[2])

    for item in operators:
        if item not in ('+','-'):
            return "Error: Operator must be '+' or '-'."

    for i in range(len(addend_top)):
        if not (addend_top[i].isdigit() and addent_bot[i].isdigit()):
            return "Error: Numbers must only contain digits."

    for i in range(len(addend_top)):
        if len(addend_top[i]) > 4 or len(addent_bot[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    top = []
    bot = []
    line = []
    result = []

    for i in range(len(addend_top)):
        if len(addend_top[i]) > len(addent_bot[i]):
            top.append(" "*2 + addend_top[i])
        else:
            top.append(" "*(len(addent_bot[i]) - len(addend_top[i]) + 2) + addend_top[i])

    for i in range(len(addent_bot)):
        if len(addent_bot[i]) > len(addend_top[i]):
            bot.append(operators[i] + " " + addent_bot[i])
        else:
            bot.append(operators[i] + " "*(len(addend_top[i]) - len(addent_bot[i]) + 1) + addent_bot[i])

    for i in range(len(addend_top)):
        line.append("-"*(max(len(addend_top[i]), len(addent_bot[i])) + 2))

    if answer:
        for i in range(len(addend_top)):
            if operators[i] == "+":
                ans = str(int(addend_top[i]) + int(addent_bot[i]))
            else:
                ans = str(int(addend_top[i]) - int(addent_bot[i]))

            if len(ans) > max(len(addend_top[i]), len(addent_bot[i])):
                result.append(" " + ans)
            else:
                result.append(" "*(max(len(addend_top[i]), len(addent_bot[i])) - len(ans) + 2) + ans)
        final_result = "    ".join(top) + "\n" + "    ".join(bot) + "\n" + "    ".join(line) + "\n" + "    ".join(result)
    else:
        final_result = "    ".join(top) + "\n" + "    ".join(bot) + "\n" + "    ".join(line)
    return final_result