# -*- coding: utf-8 -*-
#
# Jonathan Salazar Santos
# 2019-08-09
# Haciendo merge de N imagenes en un gif animado.
# - - - - - - - - - - -

import imageio

images = []
filenames = [
	'./images/image1.png', 
	'./images/image2.png'
]

name = './images/new_image.gif'

for filename in filenames:
	images.append(imageio.imread(filename))
imageio.mimsave(name, images, duration=1.5)