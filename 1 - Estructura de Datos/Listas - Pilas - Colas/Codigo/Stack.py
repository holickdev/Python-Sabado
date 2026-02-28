# Pila (Stack) — LIFO
# Último en entrar, primero en salir. Solo se opera desde el top.


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Agregar al top
    def push(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.next = self.top
        self.top = nuevo_nodo

    # Eliminar y devolver el top
    def pop(self):
        if self.top is None:
            return None
        dato = self.top.data
        self.top = self.top.next
        return dato

    # Ver el top sin eliminar
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    # Cantidad de elementos
    def size(self):
        contador = 0
        actual = self.top
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador

    # Verificar si está vacía
    def is_empty(self):
        return self.top is None

    # Mostrar la pila (top -> fondo)
    def display(self):
        actual = self.top
        while actual is not None:
            print(f"  | {actual.data} |")
            actual = actual.next
        print("  +------+")


# --- Ejemplo de uso ---
mi_pila = Stack()
mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)
mi_pila.display()

print(f"Pop: {mi_pila.pop()}")
mi_pila.display()
print(f"Peek: {mi_pila.peek()}")
print(f"Tamaño: {mi_pila.size()}")
