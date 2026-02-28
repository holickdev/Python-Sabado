# Lista Doblemente Enlazada (Doubly Linked List)
# Cada nodo apunta al siguiente (next) y al anterior (prev).


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insertar al inicio
    def push_front(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            return
        nuevo_nodo.next = self.head
        self.head.prev = nuevo_nodo
        self.head = nuevo_nodo

    # Insertar al final
    def push_back(self, data):
        nuevo_nodo = Nodo(data)
        if self.tail is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            return
        nuevo_nodo.prev = self.tail
        self.tail.next = nuevo_nodo
        self.tail = nuevo_nodo

    # Eliminar el primero
    def pop_front(self):
        if self.head is None:
            return None
        dato = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return dato

    # Eliminar el último
    def pop_back(self):
        if self.tail is None:
            return None
        dato = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return dato

    # Ver el primero
    def peek_front(self):
        if self.head is None:
            return None
        return self.head.data

    # Ver el último
    def peek_back(self):
        if self.tail is None:
            return None
        return self.tail.data

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
        actual = self.head
        while actual is not None:
            if actual.data == data:
                if actual == self.head:
                    self.pop_front()
                    return
                if actual == self.tail:
                    self.pop_back()
                    return
                actual.prev.next = actual.next
                actual.next.prev = actual.prev
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

    # Mostrar hacia adelante (head -> tail)
    def display(self):
        actual = self.head
        resultado = "None <-> "
        while actual is not None:
            resultado += f"[{actual.data}] <-> "
            actual = actual.next
        resultado += "None"
        print(resultado)

    # Mostrar hacia atrás (tail -> head)
    def display_reverse(self):
        actual = self.tail
        resultado = "None <-> "
        while actual is not None:
            resultado += f"[{actual.data}] <-> "
            actual = actual.prev
        resultado += "None"
        print(resultado)


# --- Ejemplo de uso ---
mi_lista = DoublyLinkedList()
mi_lista.push_back(10)
mi_lista.push_back(20)
mi_lista.push_back(30)
mi_lista.push_front(5)

print("Adelante:")
mi_lista.display()
print("Atrás:")
mi_lista.display_reverse()

mi_lista.delete(20)
mi_lista.display()

print(f"Pop front: {mi_lista.pop_front()}")
print(f"Pop back: {mi_lista.pop_back()}")
mi_lista.display()
print(f"Tamaño: {mi_lista.size()}")
