import tkinter as tk

root = tk.Tk()

result_var = tk.StringVar(value="")

def binary(base: int) -> str:
    bits = [0] * 8
    i = 7
    while base:
        bits[i] = base % 2
        base //= 2
        i -= 1
    return "".join(map(str, bits))

def convert(index: int) -> str:
    value = entry1.get().strip()

    if not value:
        return "Entrée vide"

    try:
        n = int(value)
    except ValueError:
        return "Valeur invalide"

    if index == 0:
        return binary(n)
    elif index == 1:
        return str(n)
    elif index == 2:
        return oct(n)[2:]
    elif index == 3:
        return hex(n)[2:].upper()

    return ""

def on_convert_click():
    sel = lb.curselection()
    if sel:
        index = sel[0]
        result_var.set(convert(index))
    else:
        result_var.set("Aucun élément sélectionné")

tk.Label(root, text="result:").grid(row=0, column=0)
tk.Label(root, text="base convert:").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

lb = tk.Listbox(root, width=20, height=4)
lb.insert(tk.END, "B2")
lb.insert(tk.END, "B10")
lb.insert(tk.END, "B8")
lb.insert(tk.END, "B16")
lb.grid(row=1, column=1)

tk.Label(root, textvariable=result_var).grid(row=3, column=1)

tk.Button(root, text="Convert", width=20, command=on_convert_click).grid(row=1, column=2)

root.mainloop()
