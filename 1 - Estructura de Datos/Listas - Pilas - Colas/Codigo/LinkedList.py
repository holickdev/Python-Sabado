# Lista Enlazada Simple (Linked List)
# Estructura lineal donde cada nodo apunta al siguiente.


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insertar al inicio
    def push_front(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    # Insertar al final
    def push_back(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None:
            self.head = nuevo_nodo
            return
        actual = self.head
        while actual.next is not None:
            actual = actual.next
        actual.next = nuevo_nodo

    # Eliminar el primero
    def pop_front(self):
        if self.head is None:
            return None
        dato = self.head.data
        self.head = self.head.next
        return dato

    # Eliminar el último
    def pop_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            dato = self.head.data
            self.head = None
            return dato
        actual = self.head
        while actual.next.next is not None:
            actual = actual.next
        dato = actual.next.data
        actual.next = None
        return dato

    # Ver el primero
    def peek_front(self):
        if self.head is None:
            return None
        return self.head.data

    # Ver el último
    def peek_back(self):
        if self.head is None:
            return None
        actual = self.head
        while actual.next is not None:
            actual = actual.next
        return actual.data

    # Buscar dato, devuelve posición o -1
    def search(self, data):
        actual = self.head
        posicion = 0
        while actual is not None:
            if actual.data == data:
                return posicion
            actual = actual.next
            posicion += 1
        return -1

    # Eliminar primera aparición de un dato
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        actual = self.head
        while actual.next is not None:
            if actual.next.data == data:
                actual.next = actual.next.next
                return
            actual = actual.next

    # Cantidad de elementos
    def size(self):
        contador = 0
        actual = self.head
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador

    # Verificar si está vacía
    def is_empty(self):
        return self.head is None

    # Mostrar la lista
    def display(self):
        actual = self.head
        resultado = ""
        while actual is not None:
            resultado += f"[{actual.data}] -> "
            actual = actual.next
        resultado += "None"
        print(resultado)


# --- Ejemplo de uso ---
mi_lista = LinkedList()
mi_lista.push_back(10)
mi_lista.push_back(20)
mi_lista.push_back(30)
mi_lista.push_front(5)
mi_lista.display()

mi_lista.delete(20)
mi_lista.display()

print(f"Pop front: {mi_lista.pop_front()}")
print(f"Pop back: {mi_lista.pop_back()}")
mi_lista.display()
print(f"Tamaño: {mi_lista.size()}")
