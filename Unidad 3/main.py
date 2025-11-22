from cliente import Cliente
from producto import Producto
from venta import Venta
from tienda import Tienda

cliente1 = Cliente("Luis", "luis@gmail.com", 1000)
p1 = Producto("Teclado", 250)
p2 = Producto("Mouse", 150)

venta1 = Venta(cliente1)
venta1.agregar_producto(p1)
venta1.agregar_producto(p2)

tienda = Tienda("Tech Store")
tienda.registrar_venta(venta1)

print(cliente1.mostrar_info())
print(f"Total de la venta: $ {venta1.total():.2f}")
print(f"Ventas registradas: {len(tienda.ventas)}")  

