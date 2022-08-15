import os
os.remove("./learnpythonwork/demofile.txt")

import os
if os.path.exists("./learnpythonwork/demofile.txt"):
  os.remove("./learnpythonwork/demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")


