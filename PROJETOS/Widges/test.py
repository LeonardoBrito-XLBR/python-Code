import tkinter as tk

root = tk.Tk()
# 1. Remove a barra de título e bordas
root.overrideredirect(True) 

# 2. Define a transparência (0.0 a 1.0)
root.attributes("-alpha", 0.8)

# 3. Mantém o widget sempre no topo (opcional)
root.wm_attributes("-topmost", True)

label = tk.Label(root, text="Meu Widget 2026", font=("Arial", 20), bg="black", fg="white")
label.pack()

root.mainloop()
