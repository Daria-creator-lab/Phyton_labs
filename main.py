import re
with open("text.txt", "r") as myFile:
    result = myFile.read()
count = 0
allowSymbol = r"[A-Za-z]"
result = re.findall(allowSymbol, result)
c = {}
for i in result:
    c[i] = c.get(i, 0)+1
    count = count + 1
with open("resultText.txt", "w") as myFile:
    myFile.write(str(c))
print(result)
print(count)
print(c)
