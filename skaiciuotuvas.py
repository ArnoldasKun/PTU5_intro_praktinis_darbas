#naujas dublis ir pritaikytas gui
#sudetis, atimtis, daugyba, dalyba

def sudetis(x, y):
    return x + y

def atimtis(x, y):
    return x - y

def daugyba(x, y):
    return x * y

def dalyba(x, y):
    return x / y

print("Pasirinkite operacija")
print("1.Sudetis")
print("2.Atimtis")
print("3.Daugyba")
print("4.Dalyba")

while True:
    pasirinkimas = input("Iveskite pasirinkima(1/2/3/4): ")

    if pasirinkimas in ("1", "2", "3", "4"):
        sk1 = float(input("Iveskite pirma skaiciu: "))
        sk2 = float(input("Iveskite antra skaiciu: "))

        if pasirinkimas == "1":
            print(sk1, "+", sk2, "=", sudetis(sk1, sk2))

        elif pasirinkimas == "2":
            print(sk1, "-", sk2, "=", atimtis(sk1, sk2))

        elif pasirinkimas == "3":
            print(sk1, "*", sk2, "=", daugyba(sk1, sk2))

        elif pasirinkimas == "4":
            print(sk1, "/", sk2, "=", dalyba(sk1, sk2))

        kitas_skaiciavimas = input("Ar darom dar viena skaiciavima? (T/N): ")
        if kitas_skaiciavimas == "N":
            break

    else:
        print("Netinkamas pasirinkimas")




