# coding: utf-8

from Tkinter import Entry, Label, StringVar, Tk , Button, END
from tkFileDialog import askopenfilename, asksaveasfile
from individu import Individu


def get_fields():
    """retrieves the fields from tkinter to store them"""
    firstname = widgets_entry["firstname"].get()
    firstname = Individu(widgets_entry["name"].get(),
    widgets_entry["firstname"].get(),
    widgets_entry["phone"].get(),
    widgets_entry["adress"].get(),
    widgets_entry["city"].get())
    if firstname not in individuals:
        individuals.append(firstname)


def clear_text():
    """remove text from all the fields"""
    for idi in ids:
        widgets_entry[idi].delete(0, END)

def research():
    """researches a name with firstname field"""
    firstname = widgets_entry["firstname"].get()

    for person in individuals:
        if person.firstname == firstname:
            clear_text()
            widgets_entry["name"].insert(0, person.name)
            widgets_entry["firstname"].insert(0, person.firstname)
            widgets_entry["phone"].insert(0, person.phone)
            widgets_entry["adress"].insert(0, person.adress)
            widgets_entry["city"].insert(0, person.city)

def openfile():
    """opens a file and stores the elements in order to be accessed later"""
    filename = askopenfilename(parent=root)
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        persons = line.split(":")


        for person in persons:
            if person == '':
                break

            characteristics = person.split(",")
            characteristics[1] = Individu(characteristics[0], characteristics[1], characteristics[2], characteristics[3], characteristics[4])

            if characteristics[1] not in individuals:
                individuals.append(characteristics[1])

def save_file():
    """saves the file in a particular format to be parsed if opened"""
    file = asksaveasfile(mode='w',defaultextension=".txt")
    for person in individuals:
        file.write(str(person.name+ "," + person.firstname + "," + person.phone + "," + person.adress + "," + person.city+ ":"))

individuals = []

root = Tk()
root.title('Annuaire')

ids = ["name", "firstname", "phone", "adress", "city"]
bouton = ["chercher", "inserer", "effacer", "ouvrir", "sauvegarder"]

widgets_labs = {}
widgets_entry = {}
widgets_button = {}

i, j = 0, 0

for idi in ids:
    lab = Label(root, text=idi)
    widgets_labs[idi] = lab
    lab.grid(row=i,column=0)

    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[idi] = entry
    entry.grid(row=i,column=1, columnspan = len(bouton) - 1 )

    i += 1

for idi in bouton:
    button = Button(root, text = idi)
    widgets_button[idi] = button
    button.grid(row=i+1,column=j)

    j += 1

widgets_button["inserer"].config(command = get_fields)
widgets_button["chercher"].config(command = research)
widgets_button["effacer"].config(command = clear_text)
widgets_button["sauvegarder"].config(command = save_file)
widgets_button["ouvrir"].config(command = openfile)
root.mainloop()
