from producto import Producto
from cliente import Cliente
from restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante Sabor Casero")

# Crear productos
producto1 = Producto(1, "Pizza", 12.50, True)
producto2 = Producto(2, "Hamburguesa", 8.75, True)
producto3 = Producto(3, "Jugo Natural", 3.50, False)

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Crear clientes
cliente1 = Cliente("1723456789", "Juan Pérez", "0991234567")
cliente2 = Cliente("1712345678", "María López", "0987654321")

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("===== SISTEMA DE GESTIÓN DE RESTAURANTE =====")
print(f"Nombre del restaurante: {restaurante.nombre}")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()