import tkinter as tk

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

class TreeVisualizer:
    def __init__(self, tree):
        self.tree = tree
        self.window = tk.Tk()
        self.window.title("Árbol Binario de Jesús")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="white")
        self.canvas.pack()

    def draw_tree(self, node, x, y, x_offset, y_offset):
        if node:
            if node.left:
                self.canvas.create_line(x, y, x - x_offset, y + y_offset, fill="black")
                self.draw_tree(node.left, x - x_offset, y + y_offset, x_offset // 2, y_offset)
            if node.right:
                self.canvas.create_line(x, y, x + x_offset, y + y_offset, fill="black")
                self.draw_tree(node.right, x + x_offset, y + y_offset, x_offset // 2, y_offset)
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightblue", outline="black")
            self.canvas.create_text(x, y, text=str(node.value), font=("Arial", 12), fill="black")

    def run(self):
        if self.tree.root:
            self.draw_tree(self.tree.root, 400, 50, 200, 75)
        self.window.mainloop()

# Crear el árbol y agregar algunos valores
tree = BinaryTree()
values = [50, 30, 70, 20, 40, 60, 80]  # Puedes cambiar estos valores si quieres
for value in values:
    tree.insert(value)

# Visualizar el árbol
visualizer = TreeVisualizer(tree)
visualizer.run()
