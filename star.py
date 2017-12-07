import os
import sys

functions = []

for f in dir(Functions):
    if not f.startswith("_"):
        functions.append(Function)

def main(file):
    invoker = Functions()
    if os.path.exists(file):
        file = open(file)
        for line in file.read_lines():
            cmd = line.split(" ")[0]
            args = line.split(" ").remove(cmd)
            
            if cmd in functions:
                getattr(invoker, cmd)(args)
            else:
                print("Syntax Error")
                break
            
            
class Functions:
    def say(self, args):
        print(' '.join(args))
        return True
