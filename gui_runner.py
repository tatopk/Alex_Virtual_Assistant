import tkinter as tk
import assist

f = open("readme.md", "r")
tmp = 1

root = tk.Tk()
root.geometry("500x600")
root.title("Alex - Virtual Assistant")

T = tk.Text(root, heigh=20, width=42)
bt = tk.Button(root, text="Talk", height="2", width="20", fg="white", bg="grey", font = "time 15 bold", command=assist.runn)
bt.place(relx=0.19, rely=0.8)
T.place(relx=0.08, rely=0.04)

for x in f:
    tmp += 1
    if 4 < tmp < 23:
        T.insert(tk.END, x)


assist.startTalk()
f.close()
root.mainloop()
