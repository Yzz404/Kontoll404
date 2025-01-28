import os
import subprocess
import time

# Warna
yellow = "\033[93m"
cyan = "\033[96m"
blue = "\033[94m"
green = "\033[92m"
red = "\033[91m"

def clear():
    os.system("clear")

def menu():
    clear()
    print(f"{blue}======================================")
    print(f"{yellow}=         BY : Thonxyzz404           =")
    print(f"{blue}======================================")
    print(f"{green}1. Masuk Lagi Ke Toolsv8!! 😁😁")
    print(f"{red}2. Keluar")
    print(f"{blue}======================================")
    print(f"{green}Otak Atik Toolsv8 Tau Rasa Koe 😹 😹      ")
    print(f"{blue}======================================")

    pilihan = input(f"{cyan}Pilih menu: ")

    if pilihan == "1":
        clone_toolsv8()
    elif pilihan == "2":
        print(f"{green}Terimakasih Telah Mengunjungii Toolsv8!!")
        exit()
    else:
        print(f"{red}Pilihan Anda Tidak Ada Di Menu!!")
        time.sleep(5)
        menu()

def clone_toolsv8():
    url_repo = "https://github.com/Zero556723/Toolsv8.git"
    direktori = "Toolsv8"

    subprocess.run(["git", "clone", url_repo])
    os.chdir(direktori)
    subprocess.run(["unzip", "Run.zip"])

menu()