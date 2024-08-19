import tkinter as tk
def evaluate(event):
    result_label.config(text=str(eval(entry.get())))
root = tk.Tk()
root.title("Calculadora Simples") 
entry = tk.Entry(root) 
entry.bind("<Return>")
result_label = tk.label(root, text="")
result_label.pack()
root.geometry("280x100")
root.mainloop()  