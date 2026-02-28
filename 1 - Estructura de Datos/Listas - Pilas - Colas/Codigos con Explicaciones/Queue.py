# =============================================================================
#                          COLA (Queue) — FIFO
# =============================================================================
#
# ¿Qué es una Cola (Queue)?
# -------------------------
# Una cola es una estructura de datos lineal que sigue el principio FIFO:
#   FIFO = First In, First Out (Primero en entrar, Primero en salir)
#
# Analogía del mundo real:
# - Imagina una FILA EN EL SUPERMERCADO: la primera persona que llega
#   es la primera que es atendida.
# - También como una fila para comprar entradas: el primero que llegó
#   es el primero que compra.
#
# Visualmente se ve así:
#
#   ENQUEUE (entran)                         DEQUEUE (salen)
#       |                                        |
#       v                                        v
#   [ 40 ] -> [ 30 ] -> [ 20 ] -> [ 10 ] ->  SALE
#    rear                           front
#   (final)                       (frente)
#
# Principio de funcionamiento:
# ----------------------------
# - Los elementos entran por la parte trasera (rear) y salen por el frente (front).
# - ENQUEUE: Agregar un elemento al final de la cola (rear).
# - DEQUEUE: Eliminar y devolver el elemento del frente (front).
# - PEEK: Ver el elemento del frente sin eliminarlo.
#
# Casos de uso comunes:
# - Cola de impresión (se imprimen en el orden que se envían).
# - Atención de clientes en un banco.
# - Manejo de tareas en un sistema operativo.
# - Mensajes en un chat (se procesan en orden de llegada).
#
# Implementación:
# ---------------
# Usamos una lista enlazada con dos punteros:
#   - front: apunta al primer elemento (el que sale primero).
#   - rear: apunta al último elemento (el más reciente).
# Esto hace que enqueue y dequeue sean O(1) (muy rápidos).
#
# =============================================================================


# =============================================================================
# CLASE NODO
# =============================================================================
# El nodo es el "bloque" básico de la cola.
# Cada nodo guarda un dato y una referencia al siguiente nodo.
# =============================================================================
class Nodo:
    def __init__(self, data):
        self.data = data    # El valor que almacena este nodo
        self.next = None    # Puntero al siguiente nodo en la cola


# =============================================================================
# CLASE QUEUE (Cola)
# =============================================================================
# La cola mantiene dos referencias:
#   - front: el nodo del frente (el primero en salir)
#   - rear: el nodo del final (el último que entró)
# =============================================================================
class Queue:
    def __init__(self):
        self.front = None   # Al crear la cola, no hay frente
        self.rear = None    # Al crear la cola, no hay final

    # -------------------------------------------------------------------------
    # ENQUEUE: Agregar un elemento AL FINAL de la cola
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Crear un nuevo nodo con el dato recibido
    #   2. Si la cola está vacía, el nuevo nodo es front Y rear
    #   3. Si no, el rear actual apunta al nuevo nodo
    #   4. Actualizamos rear al nuevo nodo
    #
    # Antes:   front -> [10] -> [20] -> [30] (rear)
    # Después: front -> [10] -> [20] -> [30] -> [NUEVO] (rear)
    # -------------------------------------------------------------------------
    def enqueue(self, data):
        # Paso 1: Creamos un nuevo nodo con el dato
        nuevo_nodo = Nodo(data)

        # Paso 2: Si la cola está vacía, el nuevo nodo es front y rear
        if self.rear is None:
            self.front = nuevo_nodo
            self.rear = nuevo_nodo
            print(f"  ENQUEUE: Se agregó '{data}' (la cola estaba vacía).")
            return

        # Paso 3: El rear actual apunta al nuevo nodo
        self.rear.next = nuevo_nodo

        # Paso 4: Actualizamos rear al nuevo nodo
        self.rear = nuevo_nodo

        print(f"  ENQUEUE: Se agregó '{data}' al final de la cola.")

    # -------------------------------------------------------------------------
    # DEQUEUE: Eliminar y devolver el elemento del FRENTE de la cola
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Verificar que la cola no esté vacía
    #   2. Guardar el dato del front actual
    #   3. Mover el front al siguiente nodo
    #   4. Si la cola quedó vacía, rear también es None
    #   5. Devolver el dato guardado
    #
    # Antes:   front -> [10] -> [20] -> [30] (rear)
    # Después: front -> [20] -> [30] (rear)   (devuelve 10)
    # -------------------------------------------------------------------------
    def dequeue(self):
        # Paso 1: Verificamos si la cola está vacía
        if self.front is None:
            print("  ¡Error! La cola está vacía, no se puede hacer dequeue.")
            return None

        # Paso 2: Guardamos el dato del nodo que vamos a eliminar
        dato_eliminado = self.front.data

        # Paso 3: Movemos el front al siguiente nodo
        self.front = self.front.next

        # Paso 4: Si la cola quedó vacía, rear también es None
        if self.front is None:
            self.rear = None

        # Paso 5: Devolvemos el dato del nodo eliminado
        print(f"  DEQUEUE: Se eliminó '{dato_eliminado}' del frente de la cola.")
        return dato_eliminado

    # -------------------------------------------------------------------------
    # PEEK: Ver el dato del frente SIN eliminarlo
    # -------------------------------------------------------------------------
    # Es útil cuando queremos saber quién es el siguiente en salir
    # sin modificar la cola.
    # -------------------------------------------------------------------------
    def peek(self):
        if self.front is None:
            print("  ¡Error! La cola está vacía, no hay nada que ver.")
            return None
        return self.front.data

    # -------------------------------------------------------------------------
    # SIZE: Devuelve la cantidad de elementos en la cola
    # -------------------------------------------------------------------------
    def size(self):
        contador = 0
        actual = self.front

        # Recorremos toda la cola contando nodos
        while actual is not None:
            contador += 1
            actual = actual.next

        return contador

    # -------------------------------------------------------------------------
    # IS_EMPTY: Verifica si la cola está vacía
    # -------------------------------------------------------------------------
    def is_empty(self):
        return self.front is None

    # -------------------------------------------------------------------------
    # DISPLAY: Muestra todos los elementos de la cola
    # -------------------------------------------------------------------------
    # Formato: front -> [10] -> [20] -> [30] -> rear
    # -------------------------------------------------------------------------
    def display(self):
        if self.front is None:
            print("  Cola vacía")
            return

        resultado = "  front -> "
        actual = self.front

        # Recorremos toda la cola construyendo la representación visual
        while actual is not None:
            resultado += f"[{actual.data}] -> "
            actual = actual.next

        resultado += "rear"
        print(resultado)


# =============================================================================
#                         EJEMPLO DE USO
# =============================================================================
# A continuación se muestra cómo usar la cola paso a paso.
# =============================================================================

print("=" * 50)
print("   DEMOSTRACIÓN - COLA (QUEUE) — FIFO")
print("=" * 50)

# Creamos una cola vacía
mi_cola = Queue()

# --- Agregamos elementos a la cola (ENQUEUE) ---
print("\n--- Haciendo ENQUEUE de: 10, 20, 30, 40 ---")
mi_cola.enqueue(10)
mi_cola.enqueue(20)
mi_cola.enqueue(30)
mi_cola.enqueue(40)

# --- Mostramos el estado actual de la cola ---
print("\n--- Estado actual de la cola ---")
mi_cola.display()

# --- Consultamos información ---
print(f"\n--- Información de la cola ---")
print(f"  Tamaño: {mi_cola.size()}")
print(f"  Elemento en el frente (peek): {mi_cola.peek()}")
print(f"  ¿Está vacía? {mi_cola.is_empty()}")

# --- Eliminamos el elemento del frente (DEQUEUE) ---
print("\n--- Haciendo DEQUEUE ---")
mi_cola.dequeue()

print("\n--- Estado después del DEQUEUE ---")
mi_cola.display()

# --- Hacemos otro DEQUEUE ---
print("\n--- Haciendo otro DEQUEUE ---")
mi_cola.dequeue()

print("\n--- Estado actual ---")
mi_cola.display()
print(f"  Tamaño: {mi_cola.size()}")

# --- Vaciamos la cola ---
print("\n--- Vaciando la cola ---")
mi_cola.dequeue()
mi_cola.dequeue()
print(f"  ¿La cola está vacía? {mi_cola.is_empty()}")

# --- Intentamos hacer DEQUEUE en una cola vacía ---
print("\n--- Intentando DEQUEUE en cola vacía ---")
mi_cola.dequeue()
