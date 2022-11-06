
class Alumno():
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
    
  def __str__(self):
    return "{} ha sacado un {} en el exámen".format(self.nombre,self.nota)
    
  def calificacion(self):
    if self.nota < 5:
      print(f"{self.nombre} ha suspendido")
    else:
      print(f"{self.nombre} ha aprobado")
      
if __name__ == "__main__":
  Alumno1 = Alumno("Manuel",7)
  print(Alumno1)
  Alumno1.calificacion()
  Alumno2 = Alumno("Elena",4)
  print(Alumno2)
  Alumno2.calificacion()

