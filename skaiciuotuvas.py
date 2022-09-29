def skaiciuoti():
    veiksmas = input("")

    sk1 = float(input("Iveskite pirma skaiciu: "))
    sk2 = float(input("Iveskite antra skaiciu: "))

    #sudetis
    if veiksmas == "+":
        print("{} + {} = ".format(sk1, sk2))
        print(sk1 + sk2)
    #atimtis
    if veiksmas == "-":
        print("{} - {} = ".format(sk1, sk2))
    #daugyba
    if veiksmas == "*":
        print