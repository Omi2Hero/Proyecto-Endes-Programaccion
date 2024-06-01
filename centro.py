from cancha import Cancha
from personas import Cliente, Empleado
from reserva import Reserva

class Centro:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = []
        self.lista_clientes = []
        self.lista_empleados = []
        self.lista_reservas = []

    def mostrar_menu_principal(self):
        while True:
            print("--- Menú Principal ---")
            print("1. Gestión de Canchas")
            print("2. Gestión de Clientes")
            print("3. Gestión de Reservas")
            print("4. Gestión de Empleados")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.mostrar_menu_canchas()

            elif opcion == "2":
                self.mostrar_menu_clientes()

            elif opcion == "3":
                self.mostrar_menu_reservas()

            elif opcion == "4":
                self.mostrar_menu_empleados()

            elif opcion == "5":
                print("Gracias por usar nuestro servicio. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def mostrar_menu_canchas(self):
        while True:
            print("--- Gestión de Canchas ---")
            print("1. Agregar Cancha")
            print("2. Listar Canchas por Deporte")
            print("3. Quitar Cancha")
            print("4. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cancha = Cancha.crear_cancha()
                if cancha:
                    cancha.agregar_cancha(self.lista_canchas)

            elif opcion == "2":
                deporte = input("Ingrese el deporte para listar las canchas: ")
                canchas = Cancha.listar_canchas_por_deporte(self.lista_canchas, deporte)
                if canchas:
                    for cancha in canchas:
                        print(f"Número: {cancha.numero}, Deporte: {cancha.deporte}, Precio: {cancha.precio}, Habilitada: {'Sí' if cancha.habilitada else 'No'}")
                else:
                    print(f"No hay canchas registradas para el deporte {deporte}.")

            elif opcion == "3":
                numero_cancha = int(input("Ingrese el número de la cancha a quitar: "))
                cancha = next((c for c in self.lista_canchas if c.numero == numero_cancha), None)
                if cancha:
                    cancha.quitar_cancha(self.lista_canchas)
                else:
                    print(f"No se encontró una cancha con número {numero_cancha}.")

            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def mostrar_menu_clientes(self):
        while True:
            print("--- Gestión de Clientes ---")
            print("1. Agregar Cliente")
            print("2. Listar Clientes")
            print("3. Listar Clientes Morosos")
            print("4. Quitar Cliente")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cliente = Cliente.crear_cliente()
                if cliente:
                    cliente.agregar_cliente(self.lista_clientes)

            elif opcion == "2":
                for cliente in self.lista_clientes:
                    print(f"ID: {cliente.identificador}, Nombre: {cliente.nombre} {cliente.apellido}, Teléfono: {cliente.telefono}, Saldo: {cliente.saldo}")

            elif opcion == "3":
                clientes_morosos = Cliente.listar_clientes_morosos(self.lista_clientes)
                if clientes_morosos:
                    for cliente in clientes_morosos:
                        print(f"ID: {cliente.identificador}, Nombre: {cliente.nombre} {cliente.apellido}, Saldo: {cliente.saldo}")
                else:
                    print("No hay clientes morosos.")

            elif opcion == "4":
                identificador = input("Ingrese el identificador del cliente a quitar: ")
                cliente = next((c for c in self.lista_clientes if c.identificador == identificador), None)
                if cliente:
                    cliente.quitar_cliente(self.lista_clientes)
                else:
                    print(f"No se encontró un cliente con identificador {identificador}.")

            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def mostrar_menu_reservas(self):
        while True:
            print("--- Gestión de Reservas ---")
            print("1. Crear Reserva")
            print("2. Listar Reservas por Cancha")
            print("3. Listar Reservas por Cliente")
            print("4. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                if not self.lista_canchas:
                    print("No hay canchas registradas. Debe agregar al menos una cancha antes de crear una reserva.")
                else:
                    reserva = Reserva.crear_reserva(self.lista_clientes, self.lista_canchas)
                    if reserva:
                        reserva.registrar_reserva(self.lista_reservas)

            elif opcion == "2":
                if not self.lista_canchas:
                    print("No hay canchas registradas.")
                else:
                    numero_cancha = int(input("Ingrese el número de la cancha para listar las reservas: "))
                    Reserva.listar_reservas_por_cancha(self.lista_reservas, numero_cancha)

            elif opcion == "3":
                if not self.lista_clientes:
                    print("No hay clientes registrados.")
                else:
                    identificador_cliente = input("Ingrese el identificador del cliente para listar las reservas: ")
                    Reserva.listar_reservas_por_cliente(self.lista_reservas, identificador_cliente)

            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def mostrar_menu_empleados(self):
        while True:
            print("--- Gestión de Empleados ---")
            print("1. Registrar Empleado")
            print("2. Asignar Tarea a Empleado")
            print("3. Listar Empleados Desocupados")
            print("4. Quitar Empleado de Cancha")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                empleado = Empleado.crear_empleado()
                if empleado:
                    empleado.registrar_empleado(self.lista_empleados)

            elif opcion == "2":
                if not self.lista_empleados:
                    print("No hay empleados registrados.")
                else:
                    print("Empleados disponibles:")
                    for i, empleado in enumerate(self.lista_empleados):
                        print(f"{i + 1}. Nombre: {empleado.nombre} {empleado.apellido}")

                    try:
                        indice_empleado = int(input("Ingrese el índice del empleado al que desea asignar tarea: ")) - 1
                        empleado_seleccionado = self.lista_empleados[indice_empleado]
                        tarea = input("Ingrese la tarea que desea asignar: ")

                        print("Canchas disponibles:")
                        for i, cancha in enumerate(self.lista_canchas):
                            print(f"{i + 1}. Número: {cancha.numero}, Deporte: {cancha.deporte}")

                        indice_cancha = int(input("Ingrese el índice de la cancha que desea asignar al empleado: ")) - 1
                        cancha_seleccionada = self.lista_canchas[indice_cancha]

                        empleado_seleccionado.asignar_tarea(tarea, cancha_seleccionada)
                        print(f"Tarea '{tarea}' asignada exitosamente a {empleado_seleccionado.nombre} {empleado_seleccionado.apellido}.")
                    except (ValueError, IndexError):
                        print("Entrada no válida.")

            elif opcion == "3":
                empleados_desocupados = Empleado.listar_empleados_desocupados(self.lista_empleados)
                if empleados_desocupados:
                    for empleado in empleados_desocupados:
                        print(f"Nombre: {empleado.nombre} {empleado.apellido}")
                else:
                    print("No hay empleados desocupados.")

            elif opcion == "4":
                if not self.lista_empleados:
                    print("No hay empleados registrados.")
                else:
                    print("Empleados registrados:")
                    for i, empleado in enumerate(self.lista_empleados):
                        print(f"{i + 1}. Nombre: {empleado.nombre} {empleado.apellido}")

                    try:
                        indice_empleado = int(input("Ingrese el índice del empleado que desea quitar de la cancha: ")) - 1
                        empleado_seleccionado = self.lista_empleados[indice_empleado]

                        print("Tareas asignadas al empleado:")
                        for i, tarea in enumerate(empleado_seleccionado.tareas):
                            print(f"{i + 1}. Tarea: {tarea}")

                        indice_tarea = int(input("Ingrese el índice de la tarea que desea quitar al empleado: ")) - 1
                        tarea_seleccionada = empleado_seleccionado.tareas[indice_tarea]

                        empleado_seleccionado.quitar_tarea(tarea_seleccionada)
                        print(f"Tarea '{tarea_seleccionada}' quitada exitosamente del empleado {empleado_seleccionado.nombre} {empleado_seleccionado.apellido}.")
                    except (ValueError, IndexError):
                        print("Entrada no válida.")

            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

def main():
    nombre = input("Introduce el nombre del centro: ")
    direccion = input("Introduce la direccion del centro: ")
    centro = Centro(nombre, direccion)
    centro.mostrar_menu_principal()

if __name__ == "__main__":
    main()
