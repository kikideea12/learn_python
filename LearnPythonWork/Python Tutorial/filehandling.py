f = open("./learnpythonwork/demofile.txt", "r")
a = f.read(5)

print(a)

f = open("./learnpythonwork/demofile.txt", "r")
a = f.readline()

print(a)
print(a)

f = open("./learnpythonwork/demofile.txt", "r")
for x in f:
  print(x)

f = open("./learnpythonwork/demofile.txt", "r")
print(f.readline())
f.close()







