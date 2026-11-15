"""Simple offline GUI for the Illustrious tag converter."""
import tkinter as tk
from tkinter import ttk
from converter import prompt

def main():
    root = tk.Tk()
    root.title("Illustrious Tag Converter — MVP")
    root.geometry("760x480")
    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="自然語言描述（繁體中文或英文）").pack(anchor="w")
    source = tk.Text(frame, height=8, wrap="word")
    source.pack(fill="both", expand=True, pady=(6, 12))
    ttk.Label(frame, text="Danbooru-style Tags（候選標籤，未經線上驗證）").pack(anchor="w")
    result = tk.Text(frame, height=6, wrap="word")
    result.pack(fill="both", expand=True, pady=(6, 12))
    def run():
        result.delete("1.0", "end")
        result.insert("1.0", prompt(source.get("1.0", "end")))
    def copy():
        root.clipboard_clear()
        root.clipboard_append(result.get("1.0", "end").strip())
    actions = ttk.Frame(frame)
    actions.pack(anchor="e")
    ttk.Button(actions, text="轉換", command=run).pack(side="left", padx=5)
    ttk.Button(actions, text="複製結果", command=copy).pack(side="left")
    root.mainloop()

if __name__ == "__main__":
    main()
