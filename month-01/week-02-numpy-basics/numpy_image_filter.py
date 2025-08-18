import numpy as np

grayscale_image = [
    [10, 20, 30],
    [120, 130, 140],
    [210, 220, 230]
]

brightness_factor = 50
np_array_image = np.array(grayscale_image)
np_array_image = np_array_image + 50
np_array_image = np.clip(np_array_image, 0, 255)