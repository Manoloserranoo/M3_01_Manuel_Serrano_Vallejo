class producto():
  def __init__(self,codigo,nombre,precio,tipo)
    self.codigo = codigo
    self.nombre = nombre
    self.precio = precio
    self.tipo = tipo
    print(f"{self.nombre} ha quedado registrado")
  def __str__(self):
    return "El código de {} es {},su precio es {} y es un{}".fotmat(self.codigo,self.nombre,self.precio,self.tipo)

