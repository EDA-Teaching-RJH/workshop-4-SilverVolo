camel = input("Input camelsss: ")
index = 0
for i in camel:
    if i == i.upper() and index != 0:
        camel = camel[:index] + "_" + camel[index:]
        index += 1
        
    index += 1

print(camel)