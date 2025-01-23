"""
IMPLEMENTA UNA CLASE PRODUCTO:

1.-UTILIZA @property PARA CONTROLAR EL EL ACCESO Y MODIFICACION DEL PRECIO 

2.-IMPLEMENTAA VALIDACION PARA ASEGURARSE DE QUE EL PRECIO Y EL STOCK NO PUEDAN SER NEGATIVOS 

3.-DEFINE UN METODO QUE CALCULE EL VALOR TOTAL EN INVENTARIO 

"""
class Producto:
    def __init__(self, precio, stock, stoc_cc):
        self._precio = precio
        self.stock = stock
        self.stoc_cc = stoc_cc

    @property
    def precio(self):
        return self._precio, 
        
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("NO HAY PRECIOS NEGATIVOS")
        self._precio = nuevo_precio

    @property
    def stock(self):
        return self.stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("NO HAY STOCK NEGATIVOS")
        self.stock = nuevo_stock
       
    @property
    def stock(self):
        return self.stoc_cc
    
    @stock.setter
    def cuenta_stock(self, stock_contado):
        stock_contado = self.stock + self.stoc_cc
        print('EL NUEVO STOCK ES '+ stock_contado )



precio_bom = Producto(1, 1, 10)
print(precio_bom.precio) 
print(precio_bom.cuenta_stock)


#-------





