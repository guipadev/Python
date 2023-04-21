"""
En relaci�n con la secci�n anterior, puede haber ocasiones en que se quiera usar el car�cter \ pero sin ser utilizado como car�cter de escape. Para ello, se puede hacer uso de las raw strings. Una cadena de este tipo comienza anteponiendo el car�cter r a las comillas (simples o dobles).
"""

# Aqu�, \n es interpretado como nueva l�nea
>>> s = 'C:\python\noticias'
>>> print(s)
C:\python
oticias

# En una raw string no se interpreta el car�cter \
>>> s = r'C:\python\noticias'
>>> print(s)
C:\python\noticias