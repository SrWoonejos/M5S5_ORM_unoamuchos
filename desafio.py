from myproject.myapp.models import Empresa, Producto

# Crear una empresa
p_and_g = Empresa.objects.create(name="P&G")
colgate = Empresa.objects.create(name="Colgate")


# Crear un producto

Producto.objects.create(name="Pampers", empresa=p_and_g)
Producto.objects.create(name="Ariel", empresa=p_and_g)
Producto.objects.create(name="Crest", empresa=p_and_g)
Producto.objects.create(name="Protex", empresa=colgate)
Producto.objects.create(name="Speed Stick", empresa=colgate)
Producto.objects.create(name="Palmolive", empresa=colgate)