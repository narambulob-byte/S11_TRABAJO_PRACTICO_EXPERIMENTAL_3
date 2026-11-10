from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")

        # ✍ TODO: opciones 3 a 9 con el patrón LEER → LLAMAR → MOSTRAR

        elif op == "3":
            pasajero = pila.desapilar()

            if pasajero is None:
                print(" Pila vacia")
            else:
                print(" ✓ Pasajero desapilado:", pasajero)
                tope = pila.ver_tope()

                if tope is not None:
                    print(" Nuevo tope:", tope)
        elif op == "4":
            pasajero = pila.ver_tope()

            if pasajero is None:
                print(" Pila vacia")
            else:
                print(" Tope de la pila:", pasajero)
        elif op == "5":
            numero = leer_entero(" Numero de pasajeros a buscar: ")
            posicion = pila.buscar(numero)

            if posicion == -1:
                print(" Pasajero no encontrado")
            else:
                print(f" Encontrado en [{posicion}]: {pila.datos[posicion]}")
        elif op == "6":
            numero = leer_entero("Numero del pasajero a modificar: ")
            destino = input("Nuevo destino: ").strip()
            asiento = input("Nuevo asiento: ").strip().upper()

            if pila.modificar(numero, destino, asiento):
                print(" ✓ Pasajero modificado correctamente")
            else:
                print(" Pasajero no encontrado")
        elif op == "7":
            numero = leer_entero(" Numero del pasajero a eliminar: ")

            if pila.eliminar_por_numero(numero):
                 print(" ✓ Pasajero eliminado")
            else:
                print(" Pasajero no encontrado")
        elif op == "8":
            copia = pila.copiar()
            print(" ✓ Copia de la pila: ")
            copia.listar()
        elif op == "9":
            print(" Longitud: ", pila.longitud())

            if pila.esta_vacia():
                print("La pila esta vacia")
            else:
                print("La pila no esta vacia")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba encolados")

        # ✍ TODO: opciones 3 a 9 con el patrón LEER → LLAMAR → MOSTRAR
        elif op == "3":
            pasajero = cola.desencolar()

            if pasajero is None:
                print( "Cola vacia")
            else:
                print( "✓ Pasajero desencolado: ", pasajero)
                frente = cola.ver_frente()

                if frente is not None:
                    print(" Nuevo frente: ", frente)
        elif op == "4":
            pasajero = cola.ver_frente()

            if pasajero is None:
                print(" Cola vacia")
            else:
                print(" Frente de la cola: ", pasajero)
        elif op == "5":
            numero = leer_entero(" Numero de pasajero a buscar: ")
            posicion = cola.buscar(numero)

            if posicion == -1:
                print(" Pasajero no encontrado")
            else:
                print(f" Encontrado en [{posicion}]: {cola.datos[posicion]}")
        elif op == "6":
            numero = leer_entero(" Numero del pasajero a modificar: ")
            destino = input(" Nuevo destino: ").strip()
            asiento = input(" Nuevo asiento: ").strip().upper()

            if cola.modificar(numero, destino, asiento):
                print(" ✓ Pasajero modificado correctamente")
            else:
                print(" Pasajero no encontrado")
        elif op == "7":
            numero = leer_entero(" Numero del pasajero a eliminar: ")

            if cola.eliminar_por_numero(numero):
                print(" ✓ Pasajero eliminado")
            else:
                print(" Pasajero no encontrado")
        elif op == "8":
            copia = cola.copiar()
            print(" ✓ Copia de la cola: ")
            copia.listar()
        elif op == "9":
            print(" Longitud: ", cola.longitud())

            if cola.esta_vacia():
                print(" La cola esta vacia")
            else:
                print(" La cola no esta vacia")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()