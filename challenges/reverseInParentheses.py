def reverseInParentheses(inputString):
    for i in range(inputString.count("(")):
        start = inputString.rfind('(')
        end = inputString.find(')', start)
        print(f'reverse printed {inputString[end-1:start: -1]}')
        inputString = inputString[:start] + inputString[end-1:start: -1] + inputString[end+1:]
    return inputString



print(reverseInParentheses("asd(bar)fwe"))

b = "Hello, World!"
print(b[5:2:-1])