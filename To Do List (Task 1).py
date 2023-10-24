import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def on_add_button_hover(event):
    add_button.config(fg='white', bg='blue')  # Change text color to white and background color to blue on hover

def on_add_button_leave(event):
    add_button.config(fg='black', bg='lightgray')  # Restore text color to black and background color to light gray

def main():
    global entry, listbox, add_button

    root = tk.Tk()
    root.title("To-Do List")

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    add_button = tk.Button(root, text="Add Task", command=add_task, fg='black', bg='lightgray', font=('Arial', 14))  # Customize text color, background color, and font
    add_button.pack(pady=5)
    add_button.bind("<Enter>", on_add_button_hover)  # Handle hover event
    add_button.bind("<Leave>", on_add_button_leave)  # Handle leaving hover

    remove_button = tk.Button(root, text="Remove Task", command=remove_task, fg='white', bg='red', font=('Arial', 14))  # Customize text color, background color, and font
    remove_button.pack(pady=5)

    listbox = tk.Listbox(root, width=50, font=('Arial', 12))  # Customize font for the listbox
    listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
