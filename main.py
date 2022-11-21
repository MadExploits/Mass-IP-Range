#!/usr/bin/python3
from multiprocessing.dummy import Pool as ThreadPool
from os import system, name, mkdir
from os.path import exists as file_exists
from colorama import Fore, Style

# Create Folder
try:
    mkdir('Results')
except:
    pass

# Clear command line windows/linux
if name == "nt":
    system("cls")
else:
    system("clear")


def mass_range(input):
    ip = input.split(".")
    with open("Results/ip_range.txt", "a") as rnge:
        for x in range(0, 256):
            rnge.write(f"{ip[0]}.{ip[1]}.{ip[2]}.{x}")
            rnge.writelines("\n")


def main():
    print(f"""
.  .  ..__             
|\/| _|[__) _.._  _  _ 
|  |(_]|  \(_][ )(_](/,
                 ._|
 {Fore.GREEN + "Mass Range IP [ MrMad ]" + Style.RESET_ALL}
    """)
    value = input("LIST IP : ")
    threads = input("Threads : ")
    if file_exists(value):
        with open(value, "r") as r:
            read = r.read()
            D_ = read.split("\n")
            with ThreadPool(int(threads)) as Th:
                print(Fore.YELLOW + "\n[?] Rangging...." + Style.RESET_ALL)
                Th.map(mass_range, D_)
                Th.close()
                Th.join()
                print(Fore.GREEN + "[+] Done" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n[!] File Not Found!")


if __name__ == "__main__":
    main()
