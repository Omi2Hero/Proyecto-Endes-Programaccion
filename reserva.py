from datetime import datetime

class Reserva:
    def __init__(self, numero_reserva, fecha, cliente, cancha, costo):
        self.numero_reserva = numero_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
        self.costo = costo

    def __str__(self):
        return f"Reserva {self.numero_reserva} - {self.fecha} - Cliente: {self.cliente.nombre} - Cancha: {self.cancha.nombre}"

class SistemaReservas:
    def __init__(self):
        self.reservas = []
        self.clientes = {}
        self.canchas = {}

    def agregar_cliente(self, cliente):
        self.clientes[cliente.id_cliente] = cliente

    def agregar_cancha(self, cancha):
        self.canchas[cancha.id_cancha] = cancha

    def crear_reserva(self, numero_reserva, fecha, id_cliente, id_cancha, costo):
        cliente = self.clientes.get(id_cliente)
        cancha = self.canchas.get(id_cancha)

        if not cliente or not cliente.habilitado:
            print("El cliente no está habilitado.")
            return False

        if cliente.saldo < -2000:
            print("El cliente tiene un saldo negativo menor a -2000.")
            return False

        if not cancha or not cancha.habilitada:
            print("La cancha no está habilitada.")
            return False

        for reserva in cancha.reservas:
            if reserva.fecha == fecha:
                print("La cancha está ocupada en ese horario.")
                return False

        reserva = Reserva(numero_reserva, fecha, cliente, cancha, costo)
        self.reservas.append(reserva)
        cancha.reservas.append(reserva)
        cliente.agregar_movimiento(-costo)
        print("Reserva creada con éxito.")
        return True

    def listar_reservas_cancha(self, id_cancha):
        cancha = self.canchas.get(id_cancha)
        if not cancha:
            print("Cancha no encontrada.")
            return
        for reserva in cancha.reservas:
            print(reserva)

    def listar_reservas_cliente(self, id_cliente):
        cliente = self.clientes.get(id_cliente)
        if not cliente:
            print("Cliente no encontrado.")
            return
        for reserva in self.reservas:
            if reserva.cliente.id_cliente == id_cliente:
                print(reserva)

    def registrar_pago(self, id_cliente, monto):
        cliente = self.clientes.get(id_cliente)
        if not cliente:
            print("Cliente no encontrado.")
            return
        cliente.agregar_movimiento(monto)
        print(f"Pago registrado para el cliente {cliente.nombre}. Nuevo saldo: {cliente.saldo}")

    def mostrar_saldo_cliente(self, id_cliente):
        cliente = self.clientes.get(id_cliente)
        if not cliente:
            print("Cliente no encontrado.")
            return
        print(f"Saldo del cliente {cliente.nombre}: {cliente.saldo}")

