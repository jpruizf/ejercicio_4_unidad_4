from clase_aplicacion import Aplicacion
from functools import partial

def poner_nro(num):
    print(num)
def test_app():
    poner_nro(0)
    function_partial = partial(poner_nro,0)
    function_partial()
    otra_funcion_partial = partial(poner_nro,1)
    otra_funcion_partial()
if __name__ == '__main__':
    test_app()