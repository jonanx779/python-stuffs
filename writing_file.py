# -*- coding: utf-8 -*-
#
# Jonathan Salazar Santos
# 2019-08-09
# Escribiendo datos en un arhivo en HD con Python
# - - - - - - - - - - -

params = {
	"foo": "This is a string",
	"bar": 200
}

filename = 'texto_python.txt'
file_to_write = open(filename,'w')
file_to_write.write('El contenido del archivo es: {0} y esto un número {1} \n'.format(params["foo"], params["bar"]))
file_to_write.write('Más texto.')
file_to_write.close()