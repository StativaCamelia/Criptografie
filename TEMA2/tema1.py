import cx_Oracle
import pygubu
import tkinter as tk

def sort_desc_nr_mat():
    cursor2 = conn.cursor()
    data2 = cursor2.execute("Select * from Studenti order by NR_MATRICOL DESC")
    for index, data in enumerate(data2):
        tk.Label(win, text="            ").grid(row = index+2, column = 1)
        tk.Label(win, text=data[1]).grid(row = index+2, column = 1)


def sort_asc_nr_mat():
    cursor2 = conn.cursor()
    data2 = cursor2.execute("Select * from Studenti order by NR_MATRICOL")
    for index, data in enumerate(data2):
        tk.Label(win, text="            ").grid(row = index+2, column = 1)
        tk.Label(win, text=data[1]).grid(row = index+2, column = 1)


def sort_desc_nume():
    cursor2 = conn.cursor()
    data2 = cursor2.execute("Select * from Studenti order by NUME DESC")
    for index, data in enumerate(data2):
        tk.Label(win, text="            ").grid(row = index+2, column = 4)
        tk.Label(win, text=data[2]).grid(row = index+2, column = 4)


def sort_asc_nume():
    cursor2 = conn.cursor()
    data2 = cursor2.execute("Select * from Studenti order by NUME")
    for index, data in enumerate(data2):
        tk.Label(win, text="            ").grid(row = index+2, column = 4)
        tk.Label(win, text=data[2]).grid(row = index+2, column = 4)


def sort_desc_prenume():
    cursor2 = conn.cursor()
    data2 = cursor2.execute("Select * from Studenti order by PRENUME DESC")
    for index, data in enumerate(data2):
        tk.Label(win, text="            ").grid(row = index+2, column = 6)
        tk.Label(win, text=data[3]).grid(row = index+2, column = 6)

def sort_asc_prenume():
    cursor2 = conn.cursor()
    data2 = cursor2.execute("Select * from Studenti order by NUME DESC")
    for index, data in enumerate(data2):
        tk.Label(win, text="            ").grid(row = index+2, column = 6)
        tk.Label(win, text=data[3]).grid(row = index+2, column = 6)


if __name__ == '__main__':
    conn = cx_Oracle.connect('Student', 'STUDENT', 'localhost')
    cursor1 = conn.cursor()
    data = cursor1.execute("Select * from Studenti")

    win = tk.Tk()
    win.title('Text Editor')
    win.geometry('600x600')
    win.title('"Studenti de la Facultatea de Informatica"')

    Button1 = tk.Button(win, text ="DESC", command = sort_desc_nr_mat)
    Button1.grid(row = 0, column=0)

    Button2 = tk.Button(win, text ="ASC", command = sort_asc_nr_mat)
    Button2.grid(row = 1, column=0)

    Button3 = tk.Button(win, text="DESC", command = sort_desc_nume)
    Button3.grid(row=0, column=3)

    Button4 = tk.Button(win, text="ASC", command = sort_asc_nume)
    Button4.grid(row=1, column=3)

    Button5 = tk.Button(win, text="DESC", command = sort_desc_prenume)
    Button5.grid(row=0, column=5)

    Button6 = tk.Button(win, text="ASC", command = sort_asc_prenume)
    Button6.grid(row=1, column=5)

    label_nr_mat = tk.Label(win, text="NR_MATRICOL", width=20)
    label_nr_mat.grid(row=0, column=1)
    label_nume = tk.Label(win, text="NUME", width=20)
    label_nume.grid(row=0, column=4)
    label_prenume = tk.Label(win, text="PRENUME", width=20)
    label_prenume.grid(row=0, column=6)

    for index, dat in enumerate(data):
        tk.Label(win, text=dat[1]).grid(row=index + 2, column=1)
        tk.Label(win, text=dat[2]).grid(row=index + 2, column=4)
        tk.Label(win, text=dat[3]).grid(row=index + 2, column=6)
    win.mainloop()



# answer = input("ALL(Afisati toti STUDENTI), INSERT(inserati un Student nou), ALL_BURSA(Afisati toti Studenti care au bursa), END:")
#     if answer.upper() == 'ALL':
#         cursor.execute('Select Nume, Prenume,  from Studenti')
#         for result in cursor:
#             print(result)
#     if answer.upper() == 'END':
#         conn.close()
#         break;

