import tkinter as tk
from tkinter import ttk

class ImGuiCheatGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ImGui-like Cheat GUI")
        self.geometry("500x200")
        self.configure(bg="#1E1E1E")  # Dark background

        style = ttk.Style()
        style.theme_use("clam")

        # Configure the style for the widgets
        style.configure("TLabel", background="#1E1E1E", foreground="#FF5555", font=("Consolas", 12))
        style.configure("TButton", background="#2D2D2D", foreground="#FF5555", font=("Consolas", 12),
                        borderwidth=0, focuscolor="none")
        style.map("TButton",
                  background=[("active", "#FF0000")])

        style.configure("TCheckbutton", background="#1E1E1E", foreground="#FF5555", font=("Consolas", 12),
                        indicatorcolor="#FF5555")
        style.map("TCheckbutton",
                  background=[("active", "#2D2D2D")])

        style.configure("Horizontal.TScale", background="#1E1E1E", troughcolor="#2D2D2D",
                        sliderlength=15, borderwidth=0, troughrelief='flat')
        style.configure("TFrame", background="#1E1E1E")

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=10, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        # Create a horizontal layout
        left_frame = ttk.Frame(frame, style="TFrame")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        right_frame = ttk.Frame(frame, style="TFrame")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left frame widgets
        label = ttk.Label(left_frame, text="Cheat Options", style="TLabel")
        label.pack(pady=5)

        self.var1 = tk.BooleanVar()
        checkbox1 = ttk.Checkbutton(left_frame, text="Enable Wallhack", variable=self.var1, style="TCheckbutton")
        checkbox1.pack(pady=5, anchor='w')

        self.var2 = tk.BooleanVar()
        checkbox2 = ttk.Checkbutton(left_frame, text="Enable Aimbot", variable=self.var2, style="TCheckbutton")
        checkbox2.pack(pady=5, anchor='w')

        # Right frame widgets
        slider_label_title = ttk.Label(right_frame, text="Aimbot Sensitivity", style="TLabel")
        slider_label_title.pack(pady=5)

        self.slider_var = tk.DoubleVar()
        slider = ttk.Scale(right_frame, from_=0, to=100, orient='horizontal', variable=self.slider_var, style="Horizontal.TScale")
        slider.pack(pady=5, fill=tk.X)

        slider_label = ttk.Label(right_frame, textvariable=self.slider_var, style="TLabel")
        slider_label.pack(pady=5)

        button = ttk.Button(right_frame, text="Apply", command=self.on_button_click, style="TButton")
        button.pack(pady=10)

    def on_button_click(self):
        print(f"Wallhack: {self.var1.get()}, Aimbot: {self.var2.get()}, Slider Value: {self.slider_var.get()}")

if __name__ == "__main__":
    app = ImGuiCheatGUI()
    app.mainloop()
