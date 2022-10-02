import tkinter as tk

kalkuliatorius = ""

def skaiciuoti(simbolis):
    global kalkuliatorius
    kalkuliatorius += str(simbolis)
    skaiciu_langas.delete(1.0, "end")
    skaiciu_langas.insert(1.0, kalkuliatorius)

def apskaiciavimas():
    global kalkuliatorius
    try:
        kalkuliatorius = str(eval(kalkuliatorius))
        skaiciu_langas.delete(1.0, "end")
        skaiciu_langas.insert(1.0, kalkuliatorius)
    except:
        isvalymas()
        skaiciu_langas.insert(1.0, "Error")  

def isvalymas():
    global kalkuliatorius
    kalkuliatorius = ""
    skaiciu_langas.delete(1.0, "end")

langas = tk.Tk()
langas.geometry("300x250")
langas.title("KALKULIATORIUS")

mygtukas_1 = tk.Button(langas, text="1", bd=3, command=lambda: skaiciuoti(1), heigh=2, width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_1.grid(row=2, column=1)
mygtukas_2 = tk.Button(langas, text="2", bd=3, command=lambda: skaiciuoti(2), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_2.grid(row=2, column=2)
mygtukas_3 = tk.Button(langas, text="3", bd=3, command=lambda: skaiciuoti(3), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_3.grid(row=2, column=3)
mygtukas_4 = tk.Button(langas, text="4", bd=3, command=lambda: skaiciuoti(4), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_4.grid(row=3, column=1)
mygtukas_5 = tk.Button(langas, text="5", bd=3, command=lambda: skaiciuoti(5), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_5.grid(row=3, column=2)
mygtukas_6 = tk.Button(langas, text="6", bd=3, command=lambda: skaiciuoti(6), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_6.grid(row=3, column=3)
mygtukas_7 = tk.Button(langas, text="7", bd=3, command=lambda: skaiciuoti(7), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_7.grid(row=4, column=1)
mygtukas_8 = tk.Button(langas, text="8", bd=3, command=lambda: skaiciuoti(8), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_8.grid(row=4, column=2)
mygtukas_9 = tk.Button(langas, text="9", bd=3, command=lambda: skaiciuoti(9), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_9.grid(row=4, column=3)
mygtukas_0 = tk.Button(langas, text="0", bd=3, command=lambda: skaiciuoti(0), width=5, font=("New Roman", 14), bg="black", fg="white")
mygtukas_0.grid(row=5, column=2)
mygtukas_sudetis = tk.Button(langas, text="+", bd=3, command=lambda: skaiciuoti("+"), width=5, font=("New Roman", 14), bg="green", fg="white")
mygtukas_sudetis.grid(row=2, column=4)
mygtukas_atimtis = tk.Button(langas, text="-", bd=3, command=lambda: skaiciuoti("-"), width=5, font=("New Roman", 14), bg="green", fg="white")
mygtukas_atimtis.grid(row=3, column=4)
mygtukas_daugyba = tk.Button(langas, text="*", bd=3, command=lambda: skaiciuoti("*"), width=5, font=("New Roman", 14), bg="green", fg="white")
mygtukas_daugyba.grid(row=4, column=4)
mygtukas_dalyba = tk.Button(langas, text="/", bd=3, command=lambda: skaiciuoti("/"), width=5, font=("New Roman", 14), bg="green", fg="white")
mygtukas_dalyba.grid(row=5, column=4)
myg_atid_skliaustas = tk.Button(langas, text="(", bd=3, command=lambda: skaiciuoti("("), width=5, font=("New Roman", 14), bg="blue", fg="white")
myg_atid_skliaustas.grid(row=5, column=1)
myg_uzd_skliaustas = tk.Button(langas, text=")", bd=3, command=lambda: skaiciuoti(")"), width=5, font=("New Roman", 14), bg="blue", fg="white")
myg_uzd_skliaustas.grid(row=5, column=3)
mygtukas_lygybe = tk.Button(langas, text="=", bd=3, command=apskaiciavimas, width=11, font=("New Roman", 14), bg="green", fg="black")
mygtukas_lygybe.grid(row=6, column=1, columnspan=2)
mygtukas_clear = tk.Button(langas, text="Isvalyti", bd=3, command=isvalymas, width=11, font=("Times New Roman", 16), bg="dark red", fg="white")
mygtukas_clear.grid(row=6, column=3, columnspan=3)
skaiciu_langas = tk.Text(langas, height=1, width=16, font=("New Roman", 24))
skaiciu_langas.grid(row=1, columnspan=5)

langas.mainloop()