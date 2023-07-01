from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import matplotlib.pyplot as plt
import os
import numpy as np

def add_date_to_photo(
        photo_path,
        date_to_photo,
        output_path
    ):

    image = Image.open(photo_path)

    watermark_image = image.copy()

    draw = ImageDraw.Draw(watermark_image)

    w, h = image.size

    fontsize = 70
    font = ImageFont.truetype("consola.ttf", fontsize)

    date = date_to_photo
    text_color = (255, 255, 255) # white
    # text_color = (0, 0, 0) # black


    draw.text((w * 0.98, h * 0.98), date, fill=text_color, font=font, anchor='rd')

    photo_path_spl = photo_path.split('/')
    
    photo_name = photo_path_spl[-1]

    new_photo_path = '/'.join(photo_path_spl[:-1]) + f'/{output_path}'


    if not os.path.isdir(new_photo_path):
        os.mkdir(new_photo_path)

    watermark_image.save(new_photo_path + f'/{photo_name}', format='JPEG')
    return 0