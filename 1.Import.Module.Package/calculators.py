import tkinter as tk
import tkinter.ttk as ttk


class SumApp:
    def __init__(self, root):
        self.root = root
        root.geometry("400x300")
        self.root.title("Сумма чисел в диапазоне:")

        self.start_spinbox = ttk.Spinbox(root, from_=0, to=100, increment=1)
        self.end_spinbox = ttk.Spinbox(root, from_=0, to=100, increment=1)
        self.sum_label = tk.Label(root, text="")
        self.calc_button = tk.Button(root, text="Вычислить сумму", command=self.calculate_sum)
        self.start_spinbox.pack(pady=10)
        self.end_spinbox.pack(pady=10)
        self.sum_label.pack(pady=10)
        self.calc_button.pack(pady=10)

    def calculate_sum(self):
        start = int(self.start_spinbox.get())
        end = int(self.end_spinbox.get())
        sum_ = sum(range(start, end + 1))
        self.sum_label.configure(text=f"Сумма чисел в диапазоне от {start} до {end}: {sum_}")


root = tk.Tk()
app = SumApp(root)
root.mainloop()
