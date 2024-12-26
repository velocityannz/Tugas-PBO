import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Data Mahasiswa")
window.geometry('440x540')
window.configure(bg='#0339fc')

def Mhs():
    nim = "23100712"
    nama = "Muhammad Ryansyah"
    prodi = "Teknik Informatika"
    semester = "Tiga"
    ipksemester1 = "3,91"
    ipksemester2 = "3,78"
    if nim_entry.get()==nim and nama_entry.get()==nama:
        messagebox.showinfo(title="Berhasil disimpan", message="You successfully save.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#0339fc')

# Creating widgets
mhs_label = tkinter.Label(
    frame, text="Data Mahasiswa", bg='#333333', fg="#FF3399", font=("Arial", 30))
nim_label = tkinter.Label(
    frame, text="NIM", bg='#fcf003', fg="#000000", font=("Arial", 16))
nim_entry = tkinter.Entry(frame, font=("Arial", 16))
nama_entry = tkinter.Entry(frame, font=("Arial", 16))
nama_label = tkinter.Label(
    frame, text="NAMA", bg='#fcf003', fg="#000000", font=("Arial", 16))
prodi_entry = tkinter.Entry(frame, font=("Arial", 16))
prodi_label = tkinter.Label(
    frame, text="PRODI", bg='#fcf003', fg="#000000", font=("Arial", 16))
semester_entry = tkinter.Entry(frame, font=("Arial", 16))
semester_label = tkinter.Label(
    frame, text="SEMESTER", bg='#fcf003', fg="#000000", font=("Arial", 16))
ipksemester1_entry = tkinter.Entry(frame, font=("Arial", 16))
ipksemester1_label = tkinter.Label(
    frame, text="IPK SEMESTER 1", bg='#fcf003', fg="#000000", font=("Arial", 16))
ipksemester2_entry = tkinter.Entry(frame, font=("Arial", 16))
ipksemester2_label = tkinter.Label(
    frame, text="IPK SEMESTER 2", bg='#fcf003', fg="#000000", font=("Arial", 16))
Mhs_button = tkinter.Button(
    frame, text="Simpan", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Mhs)

# Placing widgets on the screen
mhs_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
nim_label.grid(row=1, column=0)
nim_entry.grid(row=1, column=1, pady=20)
nama_label.grid(row=2, column=0)
nama_entry.grid(row=2, column=1, pady=20)
prodi_label.grid(row=3, column=0)
prodi_entry.grid(row=3, column=1, pady=20)
semester_label.grid(row=4, column=0)
semester_entry.grid(row=4, column=1, pady=20)
ipksemester1_label.grid(row=5, column=0)
ipksemester1_entry.grid(row=5, column=1, pady=20)
ipksemester2_label.grid(row=6, column=0)
ipksemester2_entry.grid(row=6, column=1, pady=20)
Mhs_button.grid(row=7, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
