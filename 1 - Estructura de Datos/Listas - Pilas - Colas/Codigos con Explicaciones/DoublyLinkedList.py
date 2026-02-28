# =============================================================================
#              LISTA DOBLEMENTE ENLAZADA (Doubly Linked List)
# =============================================================================
#
# ¿Qué es una Lista Doblemente Enlazada?
# ---------------------------------------
# Es una lista enlazada donde cada nodo tiene DOS punteros:
#   1. next: apunta al SIGUIENTE nodo
#   2. prev: apunta al nodo ANTERIOR
#
# Esto permite recorrer la lista en AMBAS DIRECCIONES:
#   - De izquierda a derecha (hacia adelante)
#   - De derecha a izquierda (hacia atrás)
#
# Visualmente se ve así:
#
#   None <- [ data | prev | next ] <-> [ data | prev | next ] <-> [ data | prev | next ] -> None
#                (head)                     (nodo 2)                    (tail)
#
# Principio de funcionamiento:
# ----------------------------
# - Mantenemos dos referencias: head (primer nodo) y tail (último nodo).
# - Cada nodo conoce a su vecino anterior (prev) y al siguiente (next).
# - El prev del head es None (no hay nodo antes del primero).
# - El next del tail es None (no hay nodo después del último).
#
# Ventajas sobre la lista simple:
# - Se puede recorrer en ambas direcciones.
# - Eliminar el último nodo es O(1) gracias al puntero tail.
# - Eliminar un nodo cualquiera es más sencillo (no hay que buscar el anterior).
#
# Desventajas:
# - Usa más memoria (cada nodo tiene un puntero extra: prev).
# - Las inserciones y eliminaciones son un poco más complejas
#   porque hay que actualizar DOS punteros en vez de uno.
#
# Casos de uso comunes:
# - Historial de navegación (ir adelante y atrás).
# - Listas de reproducción de música (siguiente / anterior).
# - Editores de texto (cursor que se mueve en ambas direcciones).
#
# =============================================================================


# =============================================================================
# CLASE NODO
# =============================================================================
# El nodo de una lista doblemente enlazada tiene TRES atributos:
#   - data: el valor que almacena
#   - next: puntero al siguiente nodo
#   - prev: puntero al nodo anterior
# =============================================================================
class Nodo:
    def __init__(self, data):
        self.data = data    # El valor que almacena este nodo
        self.next = None    # Puntero al siguiente nodo
        self.prev = None    # Puntero al nodo anterior


# =============================================================================
# CLASE DOUBLY LINKED LIST (Lista Doblemente Enlazada)
# =============================================================================
# Mantiene dos referencias:
#   - head: el primer nodo de la lista
#   - tail: el último nodo de la lista
# =============================================================================
class DoublyLinkedList:
    def __init__(self):
        self.head = None    # Al crear la lista, no hay head
        self.tail = None    # Al crear la lista, no hay tail

    # -------------------------------------------------------------------------
    # PUSH_FRONT: Insertar un nuevo nodo AL INICIO de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Crear un nuevo nodo
    #   2. Si la lista está vacía: el nuevo nodo es head Y tail
    #   3. Si no está vacía:
    #      a. El nuevo nodo apunta (next) al head actual
    #      b. El head actual apunta (prev) al nuevo nodo
    #      c. El head ahora es el nuevo nodo
    #
    # Antes:   head <-> [A] <-> [B] <-> [C] <-> tail
    # Después: head <-> [NUEVO] <-> [A] <-> [B] <-> [C] <-> tail
    # -------------------------------------------------------------------------
    def push_front(self, data):
        # Paso 1: Creamos un nuevo nodo
        nuevo_nodo = Nodo(data)

        # Paso 2: Si la lista está vacía, el nuevo nodo es head y tail
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            return

        # Paso 3a: El nuevo nodo apunta (next) al head actual
        nuevo_nodo.next = self.head

        # Paso 3b: El head actual apunta (prev) al nuevo nodo
        self.head.prev = nuevo_nodo

        # Paso 3c: Ahora el head es el nuevo nodo
        self.head = nuevo_nodo

    # -------------------------------------------------------------------------
    # PUSH_BACK: Insertar un nuevo nodo AL FINAL de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Crear un nuevo nodo
    #   2. Si la lista está vacía: el nuevo nodo es head Y tail
    #   3. Si no está vacía:
    #      a. El nuevo nodo apunta (prev) al tail actual
    #      b. El tail actual apunta (next) al nuevo nodo
    #      c. El tail ahora es el nuevo nodo
    #
    # Antes:   head <-> [A] <-> [B] <-> [C] <-> tail
    # Después: head <-> [A] <-> [B] <-> [C] <-> [NUEVO] <-> tail
    # -------------------------------------------------------------------------
    def push_back(self, data):
        # Paso 1: Creamos un nuevo nodo
        nuevo_nodo = Nodo(data)

        # Paso 2: Si la lista está vacía, el nuevo nodo es head y tail
        if self.tail is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            return

        # Paso 3a: El nuevo nodo apunta (prev) al tail actual
        nuevo_nodo.prev = self.tail

        # Paso 3b: El tail actual apunta (next) al nuevo nodo
        self.tail.next = nuevo_nodo

        # Paso 3c: Ahora el tail es el nuevo nodo
        self.tail = nuevo_nodo

    # -------------------------------------------------------------------------
    # POP_FRONT: Eliminar y devolver el PRIMER nodo de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Si la lista está vacía, no hay nada que eliminar
    #   2. Guardamos el dato del head actual
    #   3. Movemos el head al siguiente nodo
    #   4. Si la lista quedó vacía, tail también es None
    #   5. Si no quedó vacía, el nuevo head apunta (prev) a None
    #
    # Antes:   head <-> [A] <-> [B] <-> [C] <-> tail
    # Después: head <-> [B] <-> [C] <-> tail   (devuelve A)
    # -------------------------------------------------------------------------
    def pop_front(self):
        # Paso 1: Verificamos si la lista está vacía
        if self.head is None:
            print("¡Error! La lista está vacía, no se puede eliminar.")
            return None

        # Paso 2: Guardamos el dato del head
        dato_eliminado = self.head.data

        # Paso 3: Movemos el head al siguiente nodo
        self.head = self.head.next

        # Paso 4: Si la lista quedó vacía, tail también es None
        if self.head is None:
            self.tail = None
        else:
            # Paso 5: El nuevo head no tiene nodo anterior
            self.head.prev = None

        return dato_eliminado

    # -------------------------------------------------------------------------
    # POP_BACK: Eliminar y devolver el ÚLTIMO nodo de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Si la lista está vacía, no hay nada que eliminar
    #   2. Guardamos el dato del tail actual
    #   3. Movemos el tail al nodo anterior
    #   4. Si la lista quedó vacía, head también es None
    #   5. Si no quedó vacía, el nuevo tail apunta (next) a None
    #
    # Nota: ¡Esto es O(1) gracias al puntero prev!
    #       En la lista simple, teníamos que recorrer toda la lista.
    #
    # Antes:   head <-> [A] <-> [B] <-> [C] <-> tail
    # Después: head <-> [A] <-> [B] <-> tail   (devuelve C)
    # -------------------------------------------------------------------------
    def pop_back(self):
        # Paso 1: Verificamos si la lista está vacía
        if self.tail is None:
            print("¡Error! La lista está vacía, no se puede eliminar.")
            return None

        # Paso 2: Guardamos el dato del tail
        dato_eliminado = self.tail.data

        # Paso 3: Movemos el tail al nodo anterior
        self.tail = self.tail.prev

        # Paso 4: Si la lista quedó vacía, head también es None
        if self.tail is None:
            self.head = None
        else:
            # Paso 5: El nuevo tail no tiene nodo siguiente
            self.tail.next = None

        return dato_eliminado

    # -------------------------------------------------------------------------
    # PEEK_FRONT: Ver el dato del PRIMER nodo SIN eliminarlo
    # -------------------------------------------------------------------------
    def peek_front(self):
        if self.head is None:
            print("¡Error! La lista está vacía.")
            return None
        return self.head.data

    # -------------------------------------------------------------------------
    # PEEK_BACK: Ver el dato del ÚLTIMO nodo SIN eliminarlo
    # -------------------------------------------------------------------------
    # Nota: ¡Esto es O(1)! No necesitamos recorrer la lista
    #       porque tenemos el puntero tail.
    # -------------------------------------------------------------------------
    def peek_back(self):
        if self.tail is None:
            print("¡Error! La lista está vacía.")
            return None
        return self.tail.data

    # -------------------------------------------------------------------------
    # SEARCH: Buscar un dato en la lista
    # -------------------------------------------------------------------------
    # Recorre la lista de head a tail buscando el dato.
    # Devuelve la posición si lo encuentra, -1 si no.
    # -------------------------------------------------------------------------
    def search(self, data):
        actual = self.head
        posicion = 0

        while actual is not None:
            if actual.data == data:
                return posicion  # ¡Encontrado!
            actual = actual.next
            posicion += 1

        return -1  # No se encontró

    # -------------------------------------------------------------------------
    # DELETE: Eliminar la PRIMERA aparición de un dato específico
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Buscar el nodo que contiene el dato
    #   2. Si es el head, usamos pop_front
    #   3. Si es el tail, usamos pop_back
    #   4. Si está en el medio:
    #      a. El nodo anterior apunta (next) al nodo siguiente
    #      b. El nodo siguiente apunta (prev) al nodo anterior
    #      (básicamente "saltamos" el nodo que queremos eliminar)
    #
    # Antes:   [A] <-> [B] <-> [C] <-> [D]   (eliminar B)
    # Después: [A] <-> [C] <-> [D]
    #          (A.next ahora apunta a C, y C.prev ahora apunta a A)
    # -------------------------------------------------------------------------
    def delete(self, data):
        # Paso 1: Buscamos el nodo que contiene el dato
        actual = self.head
        while actual is not None:
            if actual.data == data:
                # Encontramos el nodo, ahora lo eliminamos

                # Paso 2: Si es el head
                if actual == self.head:
                    self.pop_front()
                    return

                # Paso 3: Si es el tail
                if actual == self.tail:
                    self.pop_back()
                    return

                # Paso 4: Está en el medio
                # 4a: El nodo anterior apunta al nodo siguiente
                actual.prev.next = actual.next

                # 4b: El nodo siguiente apunta al nodo anterior
                actual.next.prev = actual.prev
                return

            actual = actual.next

        # Si llegamos aquí, no se encontró el dato
        print(f"El dato '{data}' no se encontró en la lista.")

    # -------------------------------------------------------------------------
    # SIZE: Devuelve la cantidad de nodos en la lista
    # -------------------------------------------------------------------------
    def size(self):
        contador = 0
        actual = self.head

        while actual is not None:
            contador += 1
            actual = actual.next

        return contador

    # -------------------------------------------------------------------------
    # IS_EMPTY: Verifica si la lista está vacía
    # -------------------------------------------------------------------------
    def is_empty(self):
        return self.head is None

    # -------------------------------------------------------------------------
    # DISPLAY: Muestra la lista de IZQUIERDA a DERECHA (head -> tail)
    # -------------------------------------------------------------------------
    # Formato: None <-> [10] <-> [20] <-> [30] <-> None
    # -------------------------------------------------------------------------
    def display(self):
        if self.head is None:
            print("Lista vacía: None")
            return

        resultado = "None <-> "
        actual = self.head

        while actual is not None:
            resultado += f"[{actual.data}] <-> "
            actual = actual.next

        resultado += "None"
        print(resultado)

    # -------------------------------------------------------------------------
    # DISPLAY_REVERSE: Muestra la lista de DERECHA a IZQUIERDA (tail -> head)
    # -------------------------------------------------------------------------
    # Esto es posible gracias al puntero prev de cada nodo.
    # Empezamos desde el tail y recorremos hacia atrás.
    #
    # Formato: None <-> [30] <-> [20] <-> [10] <-> None
    # -------------------------------------------------------------------------
    def display_reverse(self):
        if self.tail is None:
            print("Lista vacía: None")
            return

        resultado = "None <-> "
        actual = self.tail

        # Recorremos desde el tail hacia el head usando prev
        while actual is not None:
            resultado += f"[{actual.data}] <-> "
            actual = actual.prev

        resultado += "None"
        print(resultado)


# =============================================================================
#                         EJEMPLO DE USO
# =============================================================================
# A continuación se muestra cómo usar la lista doblemente enlazada paso a paso.
# =============================================================================

print("=" * 60)
print("   DEMOSTRACIÓN - LISTA DOBLEMENTE ENLAZADA")
print("=" * 60)

# Creamos una lista doblemente enlazada vacía
mi_lista = DoublyLinkedList()

# --- Insertamos elementos al final ---
print("\n--- Insertando al final (push_back): 10, 20, 30 ---")
mi_lista.push_back(10)
mi_lista.push_back(20)
mi_lista.push_back(30)
print("Hacia adelante: ", end="")
mi_lista.display()  # None <-> [10] <-> [20] <-> [30] <-> None

# --- Insertamos al inicio ---
print("\n--- Insertando al inicio (push_front): 5 ---")
mi_lista.push_front(5)
print("Hacia adelante: ", end="")
mi_lista.display()  # None <-> [5] <-> [10] <-> [20] <-> [30] <-> None

# --- Mostramos la lista en ambas direcciones ---
print("\n--- Mostrando en ambas direcciones ---")
print("Hacia adelante:  ", end="")
mi_lista.display()
print("Hacia atrás:     ", end="")
mi_lista.display_reverse()

# --- Consultamos información ---
print(f"\n--- Información de la lista ---")
print(f"Tamaño: {mi_lista.size()}")
print(f"Primer elemento (peek_front): {mi_lista.peek_front()}")
print(f"Último elemento (peek_back): {mi_lista.peek_back()}")
print(f"¿Está vacía? {mi_lista.is_empty()}")

# --- Buscamos un elemento ---
print(f"\n--- Buscando el dato 20 ---")
posicion = mi_lista.search(20)
if posicion != -1:
    print(f"El dato 20 se encontró en la posición {posicion}")

# --- Eliminamos un nodo del medio ---
print("\n--- Eliminando el nodo con dato 20 (delete) ---")
mi_lista.delete(20)
print("Hacia adelante: ", end="")
mi_lista.display()  # None <-> [5] <-> [10] <-> [30] <-> None

# --- Eliminamos el primer nodo ---
print("\n--- Eliminando el primer nodo (pop_front) ---")
eliminado = mi_lista.pop_front()
print(f"Nodo eliminado: {eliminado}")
print("Hacia adelante: ", end="")
mi_lista.display()  # None <-> [10] <-> [30] <-> None

# --- Eliminamos el último nodo ---
print("\n--- Eliminando el último nodo (pop_back) ---")
eliminado = mi_lista.pop_back()
print(f"Nodo eliminado: {eliminado}")
print("Hacia adelante: ", end="")
mi_lista.display()  # None <-> [10] <-> None

# --- Estado final ---
print(f"\nTamaño final: {mi_lista.size()}")
print("Hacia adelante:  ", end="")
mi_lista.display()
print("Hacia atrás:     ", end="")
mi_lista.display_reverse()
