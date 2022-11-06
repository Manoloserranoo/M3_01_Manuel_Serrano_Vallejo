
class Alumno():
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
    
  def constructor(self):
    print(f"Nombre:{self.nombre}")
    print(f"Nota:{self.nota}")
    
  def calificacion(self):
    if self.nota < 5:
      print(f"{self.nombre} ha suspendido")
    else:
      print(f"{self.nombre} ha aprobado")
      
if __name__ == "__main__":
  Alumno1 = Alumno("Manuel",7)
  Alumno2 = Alumno("Elena",4)
  Alumno1.constructor()
  Alumno1.calificacion()
  Alumno2.constructor()
  Alumno2.calificacion()
  