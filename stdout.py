import sys
with open("sys_help.txt","w") as f:
    prev_stdout = sys.stdout
    sys.stdout = f
    help(sys)
    sys.stdout = prev_stdout

