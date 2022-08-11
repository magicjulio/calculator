import tkinter as tk

color = "#f5f5f5"
label_color = "#25265E"
small_font = ("Arial", 16)
white = "#ffffff"
black = "#000"
LARGE_FONT = ("Arial", 40, "bold")
digit_font = ("Arial", 24, "bold")
default_font = ("Arial", 20)
off_white = "#F8FAFF"
light_blue = "#aecbfa"
purple = "#800080"
yellow = "#FFFF00"
orange = "#FF4500"
silver = "#C0C0C0"
aqua = "#E0FFFF"
blue = "#4169E1"
nice = "#6A5ACD"



class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(None, None)
        self.window.title("Calculator by Julio")
        self.window.iconbitmap("calc.ico")
        self.total_ex = ""
        self.current_ex = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2),
            ".": (4, 1)

        }

        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "-",
            "+": "+",

        }

        self.buttons_frame = self.create_button_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digits_buttons()
        self.create_ops_butons()
        self.create_special_btns()
        self.bind_key()

    def bind_key(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_ex(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_ope(operator))

    def create_special_btns(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_ex, anchor=tk.E, bg=color,
                               fg=label_color, padx=24, font=small_font)

        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_ex, anchor=tk.E, bg=color,
                         fg=label_color, padx=24, font=LARGE_FONT)

        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=color)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_ex(self, val):
        self.current_ex += str(val)
        self.update_label()

    def create_digits_buttons(self):
        for digit, value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                               bg=aqua, fg=label_color, font=digit_font,
                               borderwidth=0, command=lambda x=digit: self.add_to_ex(x))

            button.grid(row=value[0], column=value[1], sticky=tk.NSEW)

    def append_ope(self, ope):
        self.current_ex += ope
        self.total_ex += self.current_ex
        self.current_ex = ""
        self.update_total_label()
        self.update_label()

    def create_ops_butons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol,
                               bg="#FF5E0E", fg=black,
                               font=default_font, borderwidth=0,
                               command=lambda x=operator: self.append_ope(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_ex = ""
        self.total_ex = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C",
                           bg=blue, fg=black,
                           font=default_font, borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_ex = str(eval(f"{self.current_ex}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2",
                           bg=nice, fg=black,
                           font=default_font, borderwidth=0,
                           command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_ex = str(eval(f"{self.current_ex}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax",
                           bg=nice, fg=black,
                           font=default_font, borderwidth=0,
                           command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_ex += self.current_ex
        self.update_total_label()

        try:

            self.current_ex = str(eval(self.total_ex))

            self.total_ex = ""
        except Exception as e:
            self.current_ex = "Error"
        finally:
            self.update_label()


    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=",
                           bg=light_blue, fg=label_color,
                           font=default_font, borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        exp = self.total_ex
        for ope, sym in self.operations.items():
            exp = exp.replace(ope, f" {sym} ")

        self.total_label.config(text=exp)

    def update_label(self):
        self.label.config(text=self.current_ex[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    my_calc = Calculator()
    my_calc.run()
