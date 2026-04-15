import tkinter as tk
from tkinter import filedialog, messagebox

import os
import Indexer
import Retriever

DB_FILE = "ktqdmCptcsXM.json"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Doc Search Engine")

        if not os.path.exists(DB_FILE):
            self.show_init_screen()
        else:
            self.show_search_screen()
    #init
    def show_init_screen(self):
        self.clear()

        tk.Label(self.root, text="No database found. Initialize:").pack()

        tk.Button(self.root, text="Choose Folder", command=self.init_db).pack()

    def init_db(self):
        folder = filedialog.askdirectory()
        if folder:
            Indexer.createDB(folder)
            messagebox.showinfo("Done", "Database created!")
            self.show_search_screen()
    #search
    def show_search_screen(self):
        self.clear()

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        tk.Button(self.root, text="Search", command=self.do_search).pack()
        tk.Button(self.root, text="Rebuild DB", command=self.show_init_screen).pack()

        self.result = tk.Label(self.root, text="", wraplength=500)
        self.result.pack()

    def do_search(self):
        query = self.entry.get()
        name, text = Retriever.search(query, DB_FILE)

        self.result.config(
            text=f"The file found is: {name}\n\n{text}"
        )

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
