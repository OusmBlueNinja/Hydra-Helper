
import os, sys

class b:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\u001b[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\u001b[37m'

def help():
  print(f'{b.WHITE}==========HELP=========={b.ENDC}')
  print('')
  print(f'{b.WARNING}commands: {b.ENDC}')
  print(f'  {b.OKGREEN}-v {b.WHITE}-{b.OKCYAN} Verbos{b.ENDC}')
  print(f'  {b.OKGREEN}-h {b.WHITE}-{b.OKCYAN} Displayes this message{b.ENDC}')
  print('')
  print(f'{b.HEADER}Made By Gigabite-Studios') 
  print(f'{b.OKCYAN}[https://github.com/ousmblueninja]{b.ENDC}')
try:
  args = sys.argv
  args.remove(__file__)
except IndexError:
  Verbos=False
  pass
if args.__contains__('-v'):
    Verbos=True
else:
    Verbos=False
if args.__contains__('-h'):
  help()

if args.__contains__('-ip'):
  IP = 

if args.__contains__('-port'):
  PORT = 









def INFO(text):
  if Verbos:
    print(text)







