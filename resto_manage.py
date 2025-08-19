import tkinter as tk
from tkinter import messagebox

item_prices = {
    'Pizza': 100,
    'Pasta': 80,
    'Burger': 80,
    'Dabeli': 40,
    'Vadapav': 40,
    'Sandwich': 120,
    'MaskaBan':50,
    'Tea':20,
    'Coffee':40
}

total = 0
selected_items = []

def add_item():
    global total
    selected_item = item_var.get()
    if selected_item in item_prices:
        selected_items.append(selected_item)
        total += item_prices[selected_item]
        order_list.insert(tk.END, f"{selected_item} - Rs {item_prices[selected_item]}")
        bill_label.config(text=f"Current Total: Rs {total}")
    else:
        messagebox.showerror("Error", "Item not available!")

def finish_order():
    if selected_items:
        messagebox.showinfo("Final Bill", f"Items Ordered:\n{', '.join(selected_items)}\n\nTotal Bill: Rs {total}")
    else:
        messagebox.showinfo("No Order", "You didn't order anything!")


root = tk.Tk()
root.title("Restaurant Order System")
root.geometry("500x400")
root.config(bg="lightyellow")

tk.Label(root, text="Welcome to Our Restaurant!", font=("Arial", 16, 'bold'), bg="lightyellow").pack(pady=10)

tk.Label(root, text="Select an Item:", font=("Arial", 12), bg="lightyellow").pack()

item_var = tk.StringVar()
item_menu = tk.OptionMenu(root, item_var, *item_prices.keys())
item_menu.pack()

tk.Button(root, text="Add to Order", command=add_item, bg="lightgreen").pack(pady=5)

order_list = tk.Listbox(root, height=6)
order_list.pack(pady=10)

bill_label = tk.Label(root, text="Current TotalBill: Rs 0", font=("Arial", 12), bg="lightyellow")
bill_label.pack()

tk.Button(root, text="Submit Order", command=finish_order, bg="orange").pack(pady=10)

root.mainloop()