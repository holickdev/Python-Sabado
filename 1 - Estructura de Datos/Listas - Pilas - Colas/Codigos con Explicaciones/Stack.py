# =============================================================================
#                           PILA (Stack) — LIFO
# =============================================================================
#
# ¿Qué es una Pila (Stack)?
# -------------------------
# Una pila es una estructura de datos lineal que sigue el principio LIFO:
#   LIFO = Last In, First Out (Último en entrar, Primero en salir)
#
# Analogía del mundo real:
# - Imagina una PILA DE PLATOS: el último plato que pones encima
#   es el primero que sacas.
# - También como una pila de libros: el que está arriba es el primero
#   que puedes tomar.
#
# Visualmente se ve así (la parte de arriba es el "top"):
#
#      ┌──────┐
#      │  30  │  <- top (último que entró, primero que sale)
#      ├──────┤
#      │  20  │
#      ├──────┤
#      │  10  │  <- fondo (primero que entró, último que sale)
#      └──────┘
#
# Principio de funcionamiento:
# ----------------------------
# - Solo se puede insertar y eliminar por la parte superior (top).
# - PUSH: Agregar un elemento en el top.
# - POP: Eliminar y devolver el elemento del top.
# - PEEK: Ver el elemento del top sin eliminarlo.
#
# Casos de uso comunes:
# - Función "deshacer" (Ctrl+Z) en editores de texto.
# - Historial de navegación en el navegador (botón "atrás").
# - Evaluación de expresiones matemáticas.
# - Manejo de llamadas a funciones en los lenguajes de programación.
#
# Implementación:
# ---------------
# Usamos una lista enlazada internamente. El "top" de la pila es el
# head de la lista enlazada. Así, push y pop son O(1) (muy rápidos).
#
# =============================================================================


# =============================================================================
# CLASE NODO
# =============================================================================
# El nodo es el "bloque" básico de la pila.
# Cada nodo guarda un dato y una referencia al nodo de abajo.
# =============================================================================
class Nodo:
    def __init__(self, data):
        self.data = data    # El valor que almacena este nodo
        self.next = None    # Puntero al nodo de abajo (siguiente en la pila)


# =============================================================================
# CLASE STACK (Pila)
# =============================================================================
# La pila mantiene una referencia al nodo superior (top).
# Todas las operaciones se realizan desde el top.
# =============================================================================
class Stack:
    def __init__(self):
        self.top = None     # Al crear la pila, está vacía (no hay top)

    # -------------------------------------------------------------------------
    # PUSH: Agregar un elemento en la parte superior de la pila
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Crear un nuevo nodo con el dato recibido
    #   2. El nuevo nodo apunta al top actual (queda encima)
    #   3. El top ahora es el nuevo nodo
    #
    # Antes:      top -> [B] -> [A] -> None
    # Después:    top -> [NUEVO] -> [B] -> [A] -> None
    # -------------------------------------------------------------------------
    def push(self, data):
        # Paso 1: Creamos un nuevo nodo con el dato
        nuevo_nodo = Nodo(data)

        # Paso 2: El nuevo nodo apunta al top actual
        nuevo_nodo.next = self.top

        # Paso 3: Ahora el top es el nuevo nodo
        self.top = nuevo_nodo

        print(f"  PUSH: Se agregó '{data}' al top de la pila.")

    # -------------------------------------------------------------------------
    # POP: Eliminar y devolver el elemento del top de la pila
    # -------------------------------------------------------------------------
    # Pasos:
    #   1. Verificar que la pila no esté vacía
    #   2. Guardar el dato del top actual
    #   3. Mover el top al siguiente nodo
    #   4. Devolver el dato guardado
    #
    # Antes:      top -> [C] -> [B] -> [A] -> None
    # Después:    top -> [B] -> [A] -> None   (devuelve C)
    # -------------------------------------------------------------------------
    def pop(self):
        # Paso 1: Verificamos si la pila está vacía
        if self.top is None:
            print("  ¡Error! La pila está vacía, no se puede hacer pop.")
            return None

        # Paso 2: Guardamos el dato del nodo que vamos a eliminar
        dato_eliminado = self.top.data

        # Paso 3: Movemos el top al siguiente nodo
        self.top = self.top.next

        # Paso 4: Devolvemos el dato del nodo eliminado
        print(f"  POP: Se eliminó '{dato_eliminado}' del top de la pila.")
        return dato_eliminado

    # -------------------------------------------------------------------------
    # PEEK: Ver el dato del top SIN eliminarlo
    # -------------------------------------------------------------------------
    # Es útil cuando queremos saber qué hay en el top sin modificar la pila.
    # -------------------------------------------------------------------------
    def peek(self):
        if self.top is None:
            print("  ¡Error! La pila está vacía, no hay nada que ver.")
            return None
        return self.top.data

    # -------------------------------------------------------------------------
    # SIZE: Devuelve la cantidad de elementos en la pila
    # -------------------------------------------------------------------------
    def size(self):
        contador = 0
        actual = self.top

        # Recorremos toda la pila contando nodos
        while actual is not None:
            contador += 1
            actual = actual.next

        return contador

    # -------------------------------------------------------------------------
    # IS_EMPTY: Verifica si la pila está vacía
    # -------------------------------------------------------------------------
    def is_empty(self):
        return self.top is None

    # -------------------------------------------------------------------------
    # DISPLAY: Muestra todos los elementos de la pila
    # -------------------------------------------------------------------------
    # Se muestra de arriba (top) hacia abajo, como una pila real.
    #
    #   | 30 |  <- top
    #   | 20 |
    #   | 10 |
    #   +----+
    # -------------------------------------------------------------------------
    def display(self):
        if self.top is None:
            print("  Pila vacía")
            return

        print("  --- Top de la pila ---")
        actual = self.top

        # Recorremos la pila desde el top hacia abajo
        while actual is not None:
            print(f"  | {actual.data} |")
            actual = actual.next

        print("  --- Fondo de la pila ---")


# =============================================================================
#                         EJEMPLO DE USO
# =============================================================================
# A continuación se muestra cómo usar la pila paso a paso.
# =============================================================================

print("=" * 50)
print("   DEMOSTRACIÓN - PILA (STACK) — LIFO")
print("=" * 50)

# Creamos una pila vacía
mi_pila = Stack()

# --- Agregamos elementos a la pila (PUSH) ---
print("\n--- Haciendo PUSH de: 10, 20, 30 ---")
mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)

# --- Mostramos el estado actual de la pila ---
print("\n--- Estado actual de la pila ---")
mi_pila.display()

# --- Consultamos información ---
print(f"\n--- Información de la pila ---")
print(f"  Tamaño: {mi_pila.size()}")
print(f"  Elemento en el top (peek): {mi_pila.peek()}")
print(f"  ¿Está vacía? {mi_pila.is_empty()}")

# --- Eliminamos el elemento del top (POP) ---
print("\n--- Haciendo POP ---")
mi_pila.pop()

print("\n--- Estado después del POP ---")
mi_pila.display()

# --- Hacemos más POP para vaciar la pila ---
print("\n--- Vaciando la pila con POP ---")
mi_pila.pop()
mi_pila.pop()

print(f"\n--- ¿La pila está vacía? {mi_pila.is_empty()} ---")

# --- Intentamos hacer POP en una pila vacía ---
print("\n--- Intentando POP en pila vacía ---")
mi_pila.pop()
