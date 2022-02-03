import os
import subprocess
import sys

from termcolor import colored

while True:
    cmd = input(colored("RPS >> ","cyan"))
    cmdln = cmd.split(' ')

    if cmdln[0]=='help':
        list = os.listdir(".")
        for i in list:
            if not i.endswith('.py'):
                list.remove(i)

        list.remove('Command Prompt.py')

        for i in list:
            print(i.replace('.py',''))

    elif os.path.isfile(f'{cmdln[0]}.py'):
        prompt = [sys.executable,cmdln[0]+".py"]
        for i in cmdln[1:]:
            prompt.append(i)
        subprocess.call(prompt)
    elif cmdln[0]=='':
        continue
    elif cmdln[0]==' ':
        continue
    elif cmdln[0]=='exit':
        sys.exit(0)
    else:
        print(colored(f'{cmdln[0]}: Command not found','red'))