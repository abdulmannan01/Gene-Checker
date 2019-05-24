import re
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.geometry("400x150+600+300")
root.title("Fasta file")
flag = 1
i = -1
info = []
gene_sequence = []
length=[]
countOfA=[]
countOfC=[]
countOfG=[]
countOfT=[]
# def callback():
#     global name
#     name = filedialog.askopenfilename()
#     print(name)

# Reading the file and seperating the information and gene sequence
def read_file():
    name = filedialog.askopenfilename()
    global i, info, gene_sequence
    messagebox.showinfo("Confirmation message", "FILE UPLOADED SUCCESSFULLY")
    with open(name, "r") as f:
        for line in f:
            if line[0] == '>':
                line = line.rstrip('\n')
                info.append(line.strip('>'))
                i = i + 1
                gene_sequence.append("")
                length.append(0)
                countOfA.append(0)
                countOfC.append(0)
                countOfG.append(0)
                countOfT.append(0)
            elif (bool(re.match('^[AGCT]', line))):
                gene_sequence[i] = gene_sequence[i] + line.strip()
                length[i]=len(gene_sequence[i])
                countOfA[i]= gene_sequence[i].count('A')
                countOfC[i] = gene_sequence[i].count('C')
                countOfG[i] = gene_sequence[i].count('G')
                countOfT[i] = gene_sequence[i].count('T')
            else:
                flag = 0
                messagebox.showinfo("Error message", "This file is not in fasta format")
                sys.exit(1)




# Writing the output file in the speified format

def Msg_box():
    messagebox.showinfo("About", "This is a Software Engineering Mini Project developed by CSB16054, CSB1660, CSB16064 & CSB16053")

def msg_box():
    messagebox.showinfo("Read-Me", "Upload the fasta file and then Download the Output file")

def download_file():
    global i
    with open("Output.txt", "w") as fd:
        fd.write('{0:5}  {1:100}  {2}   {3} {4} {5} {6} {7}\n'.format("Sl. No.", "Info", "Gene","length","Count-A","Count-C","Count-G","Count-T"))

        for iter in range(0, i+1):
            fd.write('{0:5} {1:100} {2} {3} {4} {5} {6} {7}\n'.format(str(iter + 1), str(info[iter]), str(gene_sequence[iter]),str(length[iter]),str(countOfA[iter]),str(countOfC[iter]),str(countOfG[iter]),str(countOfT[iter])))



one = tk.Label(root, text="Software Engineering Project", bg="red", fg="black", width=1000, font=200)
one.pack()
Button(text = "Upload File", command = read_file, fg = "black", height = 2, width = 1).pack(fill = X)

if flag:

    Button(text = "Download File", command = download_file, fg = "black", height = 2, width = 1).pack(fill = X)
else:
    text = Text(Tk)
    text.insert(END, "Either gene sequence contains letters other than AGCT or specification takes more than one line.\nIncorrect Fasta file.\n")

menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label="Project", menu=submenu)
submenu.add_command(label="About", command=Msg_box)
submenu.add_separator()
submenu.add_command(label="Exit", command=quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Read-Me", command=msg_box)

root.mainloop()