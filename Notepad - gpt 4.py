import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.textarea = tk.Text(self.root)
        self.textarea.pack(fill=tk.BOTH, expand=1)
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        self.new_file()
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path == "":
            return
        with open(file_path, "r") as file_data:
            text = file_data.read()
            self.textarea.insert(tk.INSERT, text)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path == "":
            return
        text = self.textarea.get(1.0, tk.END)
        with open(file_path, "w") as file_data:
            file_data.write(text)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Text Editor")
    root.geometry("500x500")
    TextEditor(root)
    root.mainloop()