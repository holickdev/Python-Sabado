# Cola (Queue) — FIFO
# Primero en entrar, primero en salir. Entra por rear, sale por front.


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Agregar al final (rear)
    def enqueue(self, data):
        nuevo_nodo = Nodo(data)
        if self.rear is None:
            self.front = nuevo_nodo
            self.rear = nuevo_nodo
            return
        self.rear.next = nuevo_nodo
        self.rear = nuevo_nodo

    # Eliminar del frente (front)
    def dequeue(self):
        if self.front is None:
            return None
        dato = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dato

    # Ver el frente sin eliminar
    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    # Cantidad de elementos
    def size(self):
        contador = 0
        actual = self.front
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador

    # Verificar si está vacía
    def is_empty(self):
        return self.front is None

    # Mostrar la cola (front -> rear)
    def display(self):
        actual = self.front
        resultado = "front -> "
        while actual is not None:
            resultado += f"[{actual.data}] -> "
            actual = actual.next
        resultado += "rear"
        print(resultado)


# --- Ejemplo de uso ---
mi_cola = Queue()
mi_cola.enqueue(10)
mi_cola.enqueue(20)
mi_cola.enqueue(30)
mi_cola.enqueue(40)
mi_cola.display()

print(f"Dequeue: {mi_cola.dequeue()}")
print(f"Dequeue: {mi_cola.dequeue()}")
mi_cola.display()
print(f"Peek: {mi_cola.peek()}")
print(f"Tamaño: {mi_cola.size()}")
