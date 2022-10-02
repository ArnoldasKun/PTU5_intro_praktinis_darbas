import math as m

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

def kv_saknis(x):
    return x

print("Pasirinkite operacija")
print("1.Sudetis")
print("2.Atimtis")
print("3.Daugyba")
print("4.Dalyba")
print("5.Kvadratine saknis")

while True:
    pasirinkimas = input("Iveskite pasirinkima(1/2/3/4/5): ")

    if pasirinkimas in ("1", "2", "3", "4", "5"):
        sk1 = float(input("Iveskite pirma skaiciu: "))

        if not pasirinkimas == "5":
            sk2 = float(input("Iveskite antra skaiciu: "))

        if pasirinkimas == "1":
            print(sk1, "+", sk2, "=", sudetis(sk1, sk2))

        elif pasirinkimas == "2":
            print(sk1, "-", sk2, "=", atimtis(sk1, sk2))

        elif pasirinkimas == "3":
            print(sk1, "*", sk2, "=", daugyba(sk1, sk2))

        elif pasirinkimas == "4":
            print(sk1, "/", sk2, "=", dalyba(sk1, sk2))

        elif pasirinkimas == "5":
            print(m.sqrt(sk1))

        kitas_skaiciavimas = input("Ar darom dar viena skaiciavima? (t/n): ")
        if kitas_skaiciavimas == "n":
            break

    else:
        print("Netinkamas pasirinkimas")
