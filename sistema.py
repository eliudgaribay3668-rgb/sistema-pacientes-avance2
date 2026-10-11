# Sistema de registro de pacientes: ampliación del Avance 1.
# Permite consultar información, actualizar diagnósticos, hospitalizar y dar alta.
# Avance 2: encapsulamiento de la edad, herencia y polimorfismo.
# Los datos utilizados en las pruebas son ficticios.


# Creación de la clase base
class Paciente:
    def __init__(self, nombre, edad, diagnostico, numero_expediente):
        self.nombre = nombre
        self.set_edad(edad)
        self.diagnostico = diagnostico
        self.numero_expediente = numero_expediente
        self.hospitalizado = False

    # Aplicación de Encapsulamiento: edad privada y acceso controlado
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        # También se valida al crear el objeto desde el constructor.
        if isinstance(edad, bool) or not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero no negativo.")
        self.__edad = edad

    # Métodos operativos de la clase base
    def mostrar_informacion(self):
        print(f"Paciente: {self.nombre}")
        print(f"Edad: {self.get_edad()} años")
        print(f"Diagnóstico: {self.diagnostico}")
        print(f"Expediente: {self.numero_expediente}")
        print(f"Hospitalizado: {self.hospitalizado}")

    def actualizar_diagnostico(self, nuevo_diagnostico):
        if not isinstance(nuevo_diagnostico, str) or not nuevo_diagnostico.strip():
            raise ValueError("El diagnóstico no puede estar vacío.")
        self.diagnostico = nuevo_diagnostico.strip()
        print(f"Diagnóstico de {self.nombre} actualizado: {self.diagnostico}.")

    def hospitalizar(self):
        self.hospitalizado = True
        print(f"El paciente {self.nombre} ha sido hospitalizado.")

    def dar_alta(self):
        self.hospitalizado = False
        print(f"El paciente {self.nombre} ha recibido el alta.")


# Uso de super() y Herencia: la subclase reutiliza el constructor de Paciente
class PacienteHospitalizado(Paciente):
    def __init__(self, nombre, edad, diagnostico, numero_expediente,
                 habitacion, medico_responsable):
        super().__init__(nombre, edad, diagnostico, numero_expediente)
        # Dos atributos nuevos propios de la subclase
        self.habitacion = habitacion
        self.medico_responsable = medico_responsable
        self.hospitalizado = True

    # Sobrescritura de métodos (Polimorfismo)
    def mostrar_informacion(self):
        # Extiende la información del padre con los datos de hospitalización.
        super().mostrar_informacion()
        print(f"Habitación registrada: {self.habitacion}")
        print(f"Médico responsable: {self.medico_responsable}")

    # Método operativo propio de la subclase
    def cambiar_habitacion(self, nueva_habitacion):
        if not self.hospitalizado:
            raise ValueError("Solo se cambia la habitación de un paciente hospitalizado.")
        if not isinstance(nueva_habitacion, str) or not nueva_habitacion.strip():
            raise ValueError("La habitación no puede estar vacía.")
        self.habitacion = nueva_habitacion.strip()
        print(f"El paciente {self.nombre} fue trasladado a la habitación {self.habitacion}.")


# Instanciación y pruebas: un objeto base y dos de la subclase
if __name__ == "__main__":
    paciente1 = Paciente("Ana López", 25, "Consulta de seguimiento", "EXP001")
    paciente2 = PacienteHospitalizado(
        "Luis Pérez", 40, "Observación", "EXP002", "201", "Dra. García"
    )
    paciente3 = PacienteHospitalizado(
        "María Ruiz", 32, "Recuperación", "EXP003", "202", "Dr. Torres"
    )

    print("=== Información inicial y polimorfismo ===")
    # La misma llamada ejecuta el método de la clase correspondiente.
    for paciente in (paciente1, paciente2, paciente3):
        paciente.mostrar_informacion()
        print("-" * 40)

    print("=== Encapsulamiento: getter y setter ===")
    print(f"Edad inicial de {paciente2.nombre}: {paciente2.get_edad()} años.")
    paciente2.set_edad(41)
    print(f"Edad actualizada: {paciente2.get_edad()} años.")
    try:
        paciente2.set_edad(-5)
    except ValueError as error:
        print(f"Cambio rechazado: {error}")
    print(f"Edad conservada después del intento: {paciente2.get_edad()} años.")

    print("=== Métodos heredados y propios ===")
    paciente1.hospitalizar()
    paciente1.dar_alta()
    paciente2.actualizar_diagnostico("Observación y seguimiento")
    paciente2.cambiar_habitacion("205")
    paciente3.dar_alta()

    print("=== Independencia de las instancias (self) ===")
    # Cambiar al paciente2 no modifica la edad, diagnóstico o habitación del paciente3.
    for paciente in (paciente1, paciente2, paciente3):
        paciente.mostrar_informacion()
        print("-" * 40)
