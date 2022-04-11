import os, sys, ctypes, getpass, json
from colorama import Fore

pc_usuario = getpass.getuser()

def banner():
    print(f"""
                               {Fore.RED}Dev By Tahg{Fore.RESET}
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░░░░░░░██████╗░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║█████╗╚█████╗░███████║╚██╗░██╔╝█████╗░░██████╔╝
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║╚════╝░╚═══██╗██╔══██║░╚████╔╝░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░░░░██████╔╝██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
            {Fore.RED}GitHub: {Fore.BLUE}https://github.com/T4hg/ {Fore.RESET}
""")

def saver():
    directorio = rf"C:\Users\{pc_usuario}\Documents\PasswordSaver-APP"
    try:
        os.mkdir(directorio)
    except:
        pass

    prefix = f"{Fore.RED}Password {Fore.BLUE}Saver {Fore.GREEN}· {Fore.WHITE}"
    system_prefix = f"{Fore.RED}$ {Fore.GREEN}"

    opt1 = input(prefix + "Gmail (EXAMPLE: example10@example.es): ")
    opt1_split = opt1.split("@")
    opt1_x = opt1_split[0]
    opt1_y = opt1_split[1]
    file_name = f"{opt1_x}-{opt1_y}"
    if os.path.exists(rf"{directorio}\{file_name}.json"):
        pass
    else:
        file1 = open(rf"{directorio}\{file_name}.json", "w+")
        file1.close()

    opt2 = input(f"\n{Fore.RED}[{Fore.WHITE}1{Fore.RED}] {Fore.WHITE}Save {Fore.RED}[{Fore.WHITE}2{Fore.RED}] {Fore.WHITE}View : ")
    if opt2 == "1":
        save = input("\n" + prefix + "Program (EXAMPLE: Chrome): ")
        save_password = input(prefix + "Password (EXAMPLE: 123): ")
        file_save = open(rf"{directorio}\{file_name}.json", "a")
        file_save.write("{\n" + f'    "{save}": "{save_password}"' + "\n}\n")
        file_save.close()
        print(system_prefix + "Password Saved Complete...\n")
        input(system_prefix + "ENTER TO BACK\n\n")
        saver()

    if opt2 == "2":
        save = input("\n" + prefix + "Program (EXAMPLE: Chrome): ")
        file_save = open(rf"{directorio}\{file_name}.json", "r")
        viewer = json.load(file_save)
        password_view = viewer.get(f'{save}')

        print(system_prefix + f"The password is {Fore.WHITE}{password_view}\n")
        input(system_prefix + "ENTER TO BACK\n\n")
        saver()
    else:
        print("\n" + system_prefix + "Choose a correct option...")
        saver()


if __name__ == '__main__':
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f'PasswordSaver | Developed by Tahg - GitHub: https://github.com/T4hg/')
    banner()
    saver()