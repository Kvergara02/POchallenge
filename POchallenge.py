x =list(input("Please input numbers: "))
for i in range(len(x)):
    i = i**3
    print(i)
if i == x:
    print(sorted(x)[-2])


print("New Problem")


y = ["1ab1231da"]
count = 0
for i in y:
    if i == "":
     count = count + 1
     print(sum(str(count)))
