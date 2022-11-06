
class Alumno():
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
    print(f"El alumno {self.nombre} ha quedado registrado")
  
  def calificacion(self):
    if self.nota < 5:
      print(f"{self.nombre} ha suspendido")
    else:
      print(f"{self.nombre} ha aprobado")
      
if __name__ == "__main__":
  Alumno1 = Alumno("Manuel",7)
  Alumno1.calificacion()
  Alumno2 = Alumno("Diego",4)
  Alumno2.calificacion()
  