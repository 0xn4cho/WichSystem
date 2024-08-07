#!/usr/bin/python3
# coding: utf-8

import re
import sys
import subprocess
from art import text2art

def display_logo():
    logo = text2art("WHSYSTEM")
    print(logo)
    print("by 0xn4cho\n") 

def get_ttl(ip_address, is_windows):
    try:
        
        ping_arg = "-n" if is_windows else "-c"
        result = subprocess.run(["ping", ping_arg, "1", ip_address], capture_output=True, text=True, check=True)
        output = result.stdout

        
        ttl_match = re.search(r"TTL=(\d+)", output, re.IGNORECASE)
        if ttl_match:
            return int(ttl_match.group(1))
        else:
            print("[!] No se pudo encontrar el TTL en la salida de ping.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error ejecutando ping: {e}")
        sys.exit(1)

def get_os(ttl):
    if ttl <= 64:
        return "Linux"
    elif ttl <= 128:
        return "Windows"
    else:
        return "Not Found"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"\n[!] Uso: python {sys.argv[0]} <direccion-ip>\n")
        sys.exit(1)

    
    display_logo()

    
    os_choice = input("¿Está ejecutando este script en Windows o Linux? (w/l): ").strip().lower()
    if os_choice not in ('w', 'l'):
        print("[!] Opción no válida. Por favor, elija 'w' para Windows o 'l' para Linux.")
        sys.exit(1)

    is_windows = os_choice == 'w'

    ip_address = sys.argv[1]
    ttl = get_ttl(ip_address, is_windows)
    os_name = get_os(ttl)

    print(f"{ip_address} (ttl -> {ttl}): {os_name}")

