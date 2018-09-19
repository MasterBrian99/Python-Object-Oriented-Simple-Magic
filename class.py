
print("     ")
print("     ")
print("\033[1;35m  /\/\   __ _ ___| |_ ___ _ __    / __\_ __(_) __ _ _ __\033[1;m  ")
print("\033[1;35m /    \ / _` / __| __/ _ \ '__|  /__\// '__| |/ _` | '_ \ \033[1;m ")
print("\033[1;35m/ /\/\ \ (_| \__ \ ||  __/ |    / \/  \ |  | | (_| | | | |\033[1;m")
print("\033[1;35m\/    \/\__,_|___/\__\___|_|    \_____/_|  |_|\__,_|_| |_|\033[1;m")
print("     ")
print("     ")
print("\033[1;37mPython Object Oriented Simple Magic\033[1;m")
print("     ")
print("     ")
print("\033[1;33mCoded By Pasindu P Konghawaththa(Master Brian)\033[1;m")
print("     ")
print("     ")

a=input("Enter First Word : ")
b=input("Enter Last Word : ")

class SpecialString:
    def __init__(pro, case):
        pro.case = case

    def __gt__(pro, loose):
        for index in range(len(loose.case)+1):
            result = loose.case[:index] + " " + pro.case
            result += " " + loose.case[index:]
            print(result)

first = SpecialString(a)
last = SpecialString(b)
first > last 