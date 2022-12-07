import os 
import sys 
import consts 

def run(): 
    if len(sys.argv) < 2: 
        print("Usage: python controller.py [command|command]") 
        return

    if sys.argv[1] == "command": 
        print("command") 
        return

if __name__ == "__main__": 
    run()