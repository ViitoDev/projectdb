import tkinter as tk
import orm
from tkinter import messagebox

def add_movie():
    name = entry_name.get()
    year = entry_year.get()
    note = entry_note.get()
    orm.film_add(name, year, note)
    messagebox.showinfo("Success!", "The film has been added to the list.")

def update_movie():
    id = entry_id.get()
    name = entry_name.get()
    year = entry_year.get()
    note = entry_note.get()
    orm.film_atualize(id, name, year, note)
    messagebox.showinfo("Success!", "The film has been updated to the list.")

def remove_movie():
    id = entry_id.get()
    orm.film_delete(id)
    messagebox.showinfo("Success!", "The film has been updated to the list.")

root = tk.Tk()
root.title("Movie manager")

label_id = tk.Label(root, text="ID: ")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_name = tk.Label(root, text="Name: ")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(root, width=50)
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_year = tk.Label(root, text="Year: ")
label_year.grid(row=2, column=0)
entry_year = tk.Entry(root, width=50)
entry_year.grid(row=2, column=1, padx=10, pady=5)

label_note = tk.Label(root, text="Note: ")
label_note.grid(row=3, column=0)
entry_note = tk.Entry(root, width=50)
entry_note.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add movie", command=add_movie)
add_button.grid(row=4, column=0, columnspan=2, pady=5)

update_button = tk.Button(root, text="Update movie", command=add_movie)
update_button.grid(row=5, column=0, columnspan=2, pady=5)

delete_button = tk.Button(root, text="Delete movie", command=add_movie)
delete_button.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()