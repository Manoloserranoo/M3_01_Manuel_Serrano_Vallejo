#Creamos la clase alumno y nombramos dos atributos nombre y nota como nos pide el enunciado.
class Alumno():
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
    print(f"El alumno {self.nombre} ha quedado registrado")
    
#Creamos la funcion calificación para que nos diga si el alumno esta suspenso o aprobado.
  def calificacion(self):
    if self.nota < 5:
      print(f"{self.nombre} ha suspendido")
    else:
      print(f"{self.nombre} ha aprobado")
#Por ultimo comprobamos que se esta llamando desde el mismo archivo y no desde otro y definimos dos alumnos y sus respectivas notas.      
if __name__ == "__main__":
  Alumno1 = Alumno("Manuel",7)
  Alumno1.calificacion()
  Alumno2 = Alumno("Diego",4)
  Alumno2.calificacion()
  