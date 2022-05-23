import spreadsheets
import tkinter
from tkinter import ttk
import threading

gs = spreadsheets.GSheets()


def odswiez():
    start = 1 if e_start.get() == "" else int(e_start.get())
    gs.update_data(start)

    data = [x for x in gs.ekipa]

    score = [pkt[2] for pkt in data]

    for element in display:
        index = score.index(max(score))

        element[0].config(bg="orange" if data[index][1] else "green")
        element[1].config(text=data[index][0])
        element[2].config(text=data[index][2])
        score.pop(index)
        data.pop(index)

    threading.Timer(10, odswiez).start()


screen = tkinter.Tk()
screen.geometry("200x235")
screen.grid_columnconfigure(0, weight=1)
screen.grid_columnconfigure(1, weight=1)
screen.grid_columnconfigure(2, weight=1)
screen.resizable(False, False)
screen.title("Pilna Pomoc")
screen.attributes("-topmost", True)

e_start = ttk.Entry()
e_start.grid(row=0, column=0, columnspan=3, sticky=tkinter.NSEW)

b_odswiez = ttk.Button(text="Odśwież", command=odswiez)
b_odswiez.grid(row=10, column=0, columnspan=3, sticky=tkinter.NSEW)

l_1 = tkinter.Label(screen, text="Mateusz Godlewski", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_1.grid(row=1, column=1, sticky="ew")
l_1_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_1_pkt.grid(row=1, column=2, sticky="ew")

l_2 = tkinter.Label(screen, text="Patryk Włodarczyk", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_2.grid(row=2, column=1, sticky="ew")
l_2_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_2_pkt.grid(row=2, column=2, sticky="ew")

l_3 = tkinter.Label(screen, text="Jakub Błoch", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_3.grid(row=3, column=1, sticky="ew")
l_3_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_3_pkt.grid(row=3, column=2, sticky="ew")

l_4 = tkinter.Label(screen, text="Przemysław Klucha", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_4.grid(row=4, column=1, sticky="ew")
l_4_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_4_pkt.grid(row=4, column=2, sticky="ew")

l_5 = tkinter.Label(screen, text="Mikołaj Ogłaza", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_5.grid(row=5, column=1, sticky="ew")
l_5_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_5_pkt.grid(row=5, column=2, sticky="ew")

l_6 = tkinter.Label(screen, text="Nikola Malinowska", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_6.grid(row=6, column=1, sticky="ew")
l_6_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_6_pkt.grid(row=6, column=2, sticky="ew")

l_7 = tkinter.Label(screen, text="Krzysztof Dębski", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_7.grid(row=7, column=1, sticky="ew")
l_7_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_7_pkt.grid(row=7, column=2, sticky="ew")

l_8 = tkinter.Label(screen, text="Jakub Trzmielewski", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_8.grid(row=8, column=1, sticky="ew")
l_8_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_8_pkt.grid(row=8, column=2, sticky="ew")

l_9 = tkinter.Label(screen, text="Mateusz Gręda", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_9.grid(row=9, column=1, sticky="ew")
l_9_pkt = tkinter.Label(screen, text="0", bg="white", relief=tkinter.GROOVE, borderwidth=2)
l_9_pkt.grid(row=9, column=2, sticky="ew")

l_1x = tkinter.Label(screen, text="1", bg="green", relief=tkinter.GROOVE, borderwidth=2)
l_1x.grid(row=1, column=0, sticky="ew")

l_2x = tkinter.Label(screen, text="2", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_2x.grid(row=2, column=0, sticky="ew")

l_3x = tkinter.Label(screen, text="3", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_3x.grid(row=3, column=0, sticky="ew")

l_4x = tkinter.Label(screen, text="4", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_4x.grid(row=4, column=0, sticky="ew")

l_5x = tkinter.Label(screen, text="5", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_5x.grid(row=5, column=0, sticky="ew")

l_6x = tkinter.Label(screen, text="6", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_6x.grid(row=6, column=0, sticky="ew")

l_7x = tkinter.Label(screen, text="7", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_7x.grid(row=7, column=0, sticky="ew")

l_8x = tkinter.Label(screen, text="8", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_8x.grid(row=8, column=0, sticky="ew")

l_9x = tkinter.Label(screen, text="9", bg="orange", relief=tkinter.GROOVE, borderwidth=2)
l_9x.grid(row=9, column=0, sticky="ew")

display = [
    [l_1x, l_1, l_1_pkt],
    [l_2x, l_2, l_2_pkt],
    [l_3x, l_3, l_3_pkt],
    [l_4x, l_4, l_4_pkt],
    [l_5x, l_5, l_5_pkt],
    [l_6x, l_6, l_6_pkt],
    [l_7x, l_7, l_7_pkt],
    [l_8x, l_8, l_8_pkt],
    [l_9x, l_9, l_9_pkt],
]

odswiez()

screen.mainloop()
