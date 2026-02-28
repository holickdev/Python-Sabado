# =============================================================================
#                    LISTA ENLAZADA SIMPLE (Linked List)
# =============================================================================
#
# ¿Qué es una Lista Enlazada?
# ----------------------------
# Una lista enlazada es una estructura de datos lineal donde los elementos
# NO están almacenados en posiciones consecutivas de memoria (como los arrays).
#
# En su lugar, cada elemento (llamado "nodo") contiene:
#   1. Un DATO (el valor que queremos guardar)
#   2. Un PUNTERO (una referencia al siguiente nodo de la lista)
#
# Visualmente se ve así:
#
#   [ data | next ] -> [ data | next ] -> [ data | next ] -> None
#       (head)            (nodo 2)           (nodo 3)
#
# Principio de funcionamiento:
# ----------------------------
# - El primer nodo se llama "head" (cabeza).
# - El último nodo apunta a None (no hay nodo siguiente).
# - Para acceder a un elemento, debemos recorrer la lista desde el head.
# - Podemos insertar y eliminar elementos en cualquier posición.
#
# Ventajas:
# - Tamaño dinámico (crece y decrece según se necesite).
# - Insertar/eliminar al inicio es muy rápido (O(1)).
#
# Desventajas:
# - No se puede acceder directamente a un elemento por índice.
# - Hay que recorrer la lista para buscar un elemento.
#
# =============================================================================


# =============================================================================
# CLASE NODO
# =============================================================================
# El nodo es el "bloque" básico de la lista enlazada.
# Cada nodo guarda un dato y una referencia al siguiente nodo.
# =============================================================================
class Nodo:
    def __init__(self, data):
        self.data = data    # El valor que almacena este nodo
        self.next = None    # Puntero al siguiente nodo (inicialmente no apunta a nada)


# =============================================================================
# CLASE LINKED LIST (Lista Enlazada Simple)
# =============================================================================
# La lista enlazada mantiene una referencia al primer nodo (head).
# Desde el head, podemos recorrer toda la lista siguiendo los punteros "next".
# =============================================================================
class LinkedList:
    def __init__(self):
        self.head = None    # Al crear la lista, está vacía (no hay head)

    # -------------------------------------------------------------------------
    # PUSH_FRONT: Insertar un nuevo nodo AL INICIO de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Crear un nuevo nodo con el dato recibido
    #   2. El nuevo nodo apunta al head actual
    #   3. El head ahora es el nuevo nodo
    #
    # Antes:  head -> [A] -> [B] -> [C] -> None
    # Después: head -> [NUEVO] -> [A] -> [B] -> [C] -> None
    # -------------------------------------------------------------------------
    def push_front(self, data):
        # Paso 1: Creamos un nuevo nodo con el dato
        nuevo_nodo = Nodo(data)

        # Paso 2: El nuevo nodo apunta al head actual
        nuevo_nodo.next = self.head

        # Paso 3: Ahora el head es el nuevo nodo
        self.head = nuevo_nodo

    # -------------------------------------------------------------------------
    # PUSH_BACK: Insertar un nuevo nodo AL FINAL de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Crear un nuevo nodo con el dato recibido
    #   2. Si la lista está vacía, el nuevo nodo es el head
    #   3. Si no, recorrer la lista hasta el último nodo
    #   4. El último nodo ahora apunta al nuevo nodo
    #
    # Antes:  head -> [A] -> [B] -> [C] -> None
    # Después: head -> [A] -> [B] -> [C] -> [NUEVO] -> None
    # -------------------------------------------------------------------------
    def push_back(self, data):
        # Paso 1: Creamos un nuevo nodo con el dato
        nuevo_nodo = Nodo(data)

        # Paso 2: Si la lista está vacía, el nuevo nodo es el head
        if self.head is None:
            self.head = nuevo_nodo
            return  # Terminamos aquí, no hay nada más que hacer

        # Paso 3: Recorremos la lista hasta encontrar el último nodo
        actual = self.head
        while actual.next is not None:
            actual = actual.next  # Avanzamos al siguiente nodo

        # Paso 4: El último nodo ahora apunta al nuevo nodo
        actual.next = nuevo_nodo

    # -------------------------------------------------------------------------
    # POP_FRONT: Eliminar y devolver el PRIMER nodo de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Si la lista está vacía, no hay nada que eliminar
    #   2. Guardamos el dato del head actual
    #   3. El head ahora es el siguiente nodo
    #   4. Devolvemos el dato guardado
    #
    # Antes:  head -> [A] -> [B] -> [C] -> None
    # Después: head -> [B] -> [C] -> None  (devuelve A)
    # -------------------------------------------------------------------------
    def pop_front(self):
        # Paso 1: Verificamos si la lista está vacía
        if self.head is None:
            print("¡Error! La lista está vacía, no se puede eliminar.")
            return None

        # Paso 2: Guardamos el dato del nodo que vamos a eliminar
        dato_eliminado = self.head.data

        # Paso 3: Movemos el head al siguiente nodo
        self.head = self.head.next

        # Paso 4: Devolvemos el dato del nodo eliminado
        return dato_eliminado

    # -------------------------------------------------------------------------
    # POP_BACK: Eliminar y devolver el ÚLTIMO nodo de la lista
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Si la lista está vacía, no hay nada que eliminar
    #   2. Si solo hay un nodo, eliminamos el head
    #   3. Si hay más, recorremos hasta el penúltimo nodo
    #   4. Guardamos el dato del último, y el penúltimo apunta a None
    #
    # Antes:  head -> [A] -> [B] -> [C] -> None
    # Después: head -> [A] -> [B] -> None  (devuelve C)
    # -------------------------------------------------------------------------
    def pop_back(self):
        # Paso 1: Verificamos si la lista está vacía
        if self.head is None:
            print("¡Error! La lista está vacía, no se puede eliminar.")
            return None

        # Paso 2: Si solo hay un nodo, eliminamos el head
        if self.head.next is None:
            dato_eliminado = self.head.data
            self.head = None
            return dato_eliminado

        # Paso 3: Recorremos hasta el PENÚLTIMO nodo
        actual = self.head
        while actual.next.next is not None:
            actual = actual.next  # Avanzamos al siguiente nodo

        # Paso 4: Guardamos el dato del último nodo y cortamos la conexión
        dato_eliminado = actual.next.data
        actual.next = None  # El penúltimo nodo ahora es el último

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
    def peek_back(self):
        if self.head is None:
            print("¡Error! La lista está vacía.")
            return None

        # Recorremos hasta el último nodo
        actual = self.head
        while actual.next is not None:
            actual = actual.next
        return actual.data

    # -------------------------------------------------------------------------
    # SEARCH: Buscar un dato en la lista
    # -------------------------------------------------------------------------
    # Recorre la lista nodo por nodo.
    # Si encuentra el dato, devuelve la posición (índice).
    # Si no lo encuentra, devuelve -1.
    # -------------------------------------------------------------------------
    def search(self, data):
        actual = self.head
        posicion = 0

        # Recorremos la lista buscando el dato
        while actual is not None:
            if actual.data == data:
                return posicion  # ¡Encontrado! Devolvemos la posición
            actual = actual.next
            posicion += 1

        return -1  # No se encontró el dato

    # -------------------------------------------------------------------------
    # DELETE: Eliminar la PRIMERA aparición de un dato específico
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Si la lista está vacía, no hay nada que eliminar
    #   2. Si el head tiene el dato, eliminamos el head
    #   3. Si no, recorremos buscando el nodo anterior al que tiene el dato
    #   4. Saltamos el nodo que queremos eliminar
    #
    # Antes:  head -> [A] -> [B] -> [C] -> None   (eliminar B)
    # Después: head -> [A] -> [C] -> None
    # -------------------------------------------------------------------------
    def delete(self, data):
        # Paso 1: Si la lista está vacía, no hay nada que hacer
        if self.head is None:
            print("¡Error! La lista está vacía, no se puede eliminar.")
            return

        # Paso 2: Si el dato está en el head, eliminamos el head
        if self.head.data == data:
            self.head = self.head.next
            return

        # Paso 3: Recorremos la lista buscando el nodo ANTERIOR al que tiene el dato
        actual = self.head
        while actual.next is not None:
            if actual.next.data == data:
                # Paso 4: Saltamos el nodo que queremos eliminar
                # actual -> [nodo a eliminar] -> [siguiente]
                # actual -> [siguiente]  (saltamos el nodo del medio)
                actual.next = actual.next.next
                return
            actual = actual.next

        # Si llegamos aquí, el dato no se encontró
        print(f"El dato '{data}' no se encontró en la lista.")

    # -------------------------------------------------------------------------
    # SIZE: Devuelve la cantidad de nodos en la lista
    # -------------------------------------------------------------------------
    def size(self):
        contador = 0
        actual = self.head

        # Recorremos toda la lista contando nodos
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
    # DISPLAY: Muestra todos los elementos de la lista
    # -------------------------------------------------------------------------
    # Formato de salida: [10] -> [20] -> [30] -> None
    # -------------------------------------------------------------------------
    def display(self):
        if self.head is None:
            print("Lista vacía: None")
            return

        actual = self.head
        resultado = ""

        # Recorremos todos los nodos construyendo la representación visual
        while actual is not None:
            resultado += f"[{actual.data}] -> "
            actual = actual.next

        resultado += "None"  # Marcamos el final de la lista
        print(resultado)


# =============================================================================
#                         EJEMPLO DE USO
# =============================================================================
# A continuación se muestra cómo usar la lista enlazada paso a paso.
# =============================================================================

print("=" * 50)
print("   DEMOSTRACIÓN - LISTA ENLAZADA SIMPLE")
print("=" * 50)

# Creamos una lista enlazada vacía
mi_lista = LinkedList()

# --- Insertamos elementos al final ---
print("\n--- Insertando al final: 10, 20, 30 ---")
mi_lista.push_back(10)
mi_lista.push_back(20)
mi_lista.push_back(30)
mi_lista.display()  # [10] -> [20] -> [30] -> None

# --- Insertamos elementos al inicio ---
print("\n--- Insertando al inicio: 5 ---")
mi_lista.push_front(5)
mi_lista.display()  # [5] -> [10] -> [20] -> [30] -> None

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
else:
    print("El dato 20 no se encontró")

# --- Eliminamos un nodo específico ---
print("\n--- Eliminando el nodo con dato 20 ---")
mi_lista.delete(20)
mi_lista.display()  # [5] -> [10] -> [30] -> None

# --- Eliminamos el primer nodo ---
print("\n--- Eliminando el primer nodo (pop_front) ---")
eliminado = mi_lista.pop_front()
print(f"Nodo eliminado: {eliminado}")
mi_lista.display()  # [10] -> [30] -> None

# --- Eliminamos el último nodo ---
print("\n--- Eliminando el último nodo (pop_back) ---")
eliminado = mi_lista.pop_back()
print(f"Nodo eliminado: {eliminado}")
mi_lista.display()  # [10] -> None

print(f"\nTamaño final: {mi_lista.size()}")
