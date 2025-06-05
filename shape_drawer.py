import tkinter as tk
from tkinter import colorchooser, ttk

class ShapeDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        # Shape selection
        self.shape_label = ttk.Label(root, text="Choose a shape:")
        self.shape_label.pack()
        
        self.shape_var = tk.StringVar(value="Circle")
        self.shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var, values=["Circle", "Square", "Triangle"])
        self.shape_dropdown.pack()

        # Color selection
        self.color_button = ttk.Button(root, text="Pick a Color", command=self.choose_color)
        self.color_button.pack()

        self.selected_color = "#000000"
        self.color_display = tk.Label(root, bg=self.selected_color, width=20, height=2)
        self.color_display.pack(pady=5)

        # Size input
        self.size_label = ttk.Label(root, text="Enter size (in pixels):")
        self.size_label.pack()
        self.size_entry = ttk.Entry(root)
        self.size_entry.pack()

        # Draw button
        self.draw_button = ttk.Button(root, text="Draw Shape", command=self.draw_shape)
        self.draw_button.pack(pady=10)

        # Canvas
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.selected_color = color
            self.color_display.config(bg=self.selected_color)

    def draw_shape(self):
        shape = self.shape_var.get()
        size = self.size_entry.get()
        try:
            size = int(size)
        except ValueError:
            size = 100  # default size

        self.canvas.delete("all")
        center_x, center_y = 200, 200  # center of canvas

        if shape == "Circle":
            self.canvas.create_oval(center_x - size/2, center_y - size/2,
                                    center_x + size/2, center_y + size/2,
                                    fill=self.selected_color)

        elif shape == "Square":
            self.canvas.create_rectangle(center_x - size/2, center_y - size/2,
                                         center_x + size/2, center_y + size/2,
                                         fill=self.selected_color)

        elif shape == "Triangle":
            points = [
                center_x, center_y - size/2,
                center_x - size/2, center_y + size/2,
                center_x + size/2, center_y + size/2
            ]
            self.canvas.create_polygon(points, fill=self.selected_color)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawerApp(root)
    root.mainloop()
