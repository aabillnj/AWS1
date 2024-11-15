# import os
# os.system("ls")
# os.system("ls -l")
# os.system("ls -l README.md")

import subprocess
# subprocess.run(["ls"])
# subprocess.run(["ls","-l"])
# subprocess.run(["ls","-l","README.md"])
# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument]) # subprocess.run(["uname","-a"])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument]) # subprocess.run(["ps","-x"])


