# Código modificado usando como base el publicado en el siguiente enlace: https://stackoverflow.com/a/50737983

import win32print # Librería necesaria para interactuar con las impresoras de Windows.

def abrirCaja (impresora) :
	impresoraHandler = win32print.OpenPrinter (impresora) # Iniciamos el punto a través del cual nos comunicaremos con la impresora.
	comandoAbrirCaja = chr (27) + chr (112) + chr (0) + chr (25) + chr (250) # Variable con serie de carácteres que la impresora interpreta como comando para abrir la caja conectada a ella.
	win32print.StartDocPrinter (impresoraHandler, 1, ('Abrir caja.', None, 'RAW')) # Iniciamos una petición de impresión con datos básico y descripcion del trabajo.
	win32print.WritePrinter (impresoraHandler, comandoAbrirCaja.encode ("utf-8")) # Pasamos el comando para abrir caja a la petición de impresión.
	win32print.EndDocPrinter (impresoraHandler) # Finalizamos la petición de impresión.
	win32print.ClosePrinter (impresoraHandler) # Cerramos la petición de impresión.

abrirCaja ("Tickets") # Llamamos a la función.
