class Paciente:
    def __init__(self, id, genero, nombre, edad, triaje):
        self.id = id
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.triaje = triaje

    def __lt__(self, other):
        return self.triaje < other.triaje

    def __str__(self):
        return f"Paciente #{self.id}: {self.nombre}, "f"{self.edad} años, Género: {self.genero}, Triaje: {self.triaje}"