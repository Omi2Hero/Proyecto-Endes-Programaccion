class Reserva:
    def __init__(self, numero_reserva, fecha, cliente, cancha):
        self.numero_reserva = numero_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha

    @staticmethod
    def crear_reserva(lista_clientes, lista_canchas):
        try:
            numero_reserva = int(input("Ingrese el número de reserva: "))
            fecha = input("Ingrese la fecha de la reserva (DD-MM-AAAA): ")
            identificador_cliente = input("Ingrese el identificador del cliente: ")
            numero_cancha = int(input("Ingrese el número de cancha: "))

            cliente = next((cl for cl in lista_clientes if cl.identificador == identificador_cliente), None)
            cancha = next((ca for ca in lista_canchas if ca.numero == numero_cancha), None)

            if not cliente:
                print(f"No se encontró un cliente con ID {identificador_cliente}.")
                return None
            if not cancha:
                print(f"No se encontró una cancha con número {numero_cancha}.")
                return None
        except ValueError as error:
            print("Error:", error)
            return None

        return Reserva(numero_reserva, fecha, cliente, cancha)

    def registrar_reserva(self, lista_reservas):
        if not self.cancha.habilitada:
            print(f"La cancha {self.cancha.numero} no está habilitada.")
            return
        if self.cliente.saldo < -2000:
            print(f"El cliente {self.cliente.identificador} no puede reservar por saldo negativo.")
            return
        for reserva in lista_reservas:
            if reserva.fecha == self.fecha and reserva.cancha.numero == self.cancha.numero:
                print(f"La cancha {self.cancha.numero} ya está reservada para esa fecha.")
                return
        lista_reservas.append(self)
        self.cliente.reservas.append(self)
        self.cancha.reservas.append(self)
        self.cliente.saldo -= self.cancha.precio
        print(f"Reserva creada exitosamente para la cancha {self.cancha.numero} el {self.fecha}.")

    @staticmethod
    def registrar_pago(cliente, monto):
        cliente.saldo += monto
        print(f"Pago de {monto} registrado para el cliente {cliente.identificador}.")

    @staticmethod
    def mostrar_saldo(cliente):
        print(f"El saldo actual del cliente {cliente.identificador} es: {cliente.saldo}")

    @staticmethod
    def listar_reservas_por_cancha(lista_reservas, numero_cancha):
        reservas_cancha = [reserva for reserva in lista_reservas if reserva.cancha.numero == numero_cancha]
        if reservas_cancha:
            print(f"Reservas para la cancha {numero_cancha}:")
            for reserva in reservas_cancha:
                print(f"Número de reserva: {reserva.numero_reserva}, Fecha: {reserva.fecha}, Cliente: {reserva.cliente.identificador}")
        else:
            print(f"No hay reservas para la cancha {numero_cancha}.")

    @staticmethod
    def listar_reservas_por_cliente(lista_reservas, identificador_cliente):
        reservas_cliente = [reserva for reserva in lista_reservas if reserva.cliente.identificador == identificador_cliente]
        if reservas_cliente:
            print(f"Reservas para el cliente {identificador_cliente}:")
            for reserva in reservas_cliente:
                print(f"Número de reserva: {reserva.numero_reserva}, Fecha: {reserva.fecha}, Cancha: {reserva.cancha.numero}")
        else:
            print(f"No hay reservas para el cliente {identificador_cliente}.")
