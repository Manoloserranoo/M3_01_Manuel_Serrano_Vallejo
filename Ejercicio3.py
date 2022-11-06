#EL procedimiento de este ejrcicio es muy similar al del ejrcicio 2 pero utilizamos más atributos que en el 1 .
class producto():
  def __init__(self,codigo,nombre,precio,tipo):
    self.codigo = codigo
    self.nombre = nombre
    self.precio = precio
    self.tipo = tipo
    print(f"{self.nombre} ha quedado registrado")
  def __str__(self):
    return "El código de {} es {},su precio es {} y pertece al grupo de {}".format(self.nombre, self.codigo, self.precio, self.tipo)

if __name__ == "__main__":
  producto1 = producto(1131,"macarrones",1.99,"pasta")
  print(producto1)
  producto2 = producto(1152,"garbanzos",3.55,"legumbres")
  print(producto2)
  producto3 = producto(1173,"jamón",4.5,"embutidos")
  print(producto3)
  producto4 = producto(1274,"helado",1.99,"postres")
  print(producto4)