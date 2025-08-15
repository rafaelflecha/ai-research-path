# A simple 3x3 grayscale image
grayscale_image = [
    [10, 20, 30],
    [120, 130, 140],
    [210, 220, 230]
]

def brighten_image(image, factor):
    brightened_image = []
    for arr in image:
        brightened_image_value = []
        for value in arr:
            # OLD
            # if value + factor >= 255:
            #     brightened_image_value.append(255)
            # else:
            #     brightened_image_value.append(value + factor)
            # BETTER
            brightened_image_value.append(min(value + factor, 255))
        brightened_image.append(brightened_image_value)
    return brightened_image
            

if __name__ == "__main__":
    factor = 50
    brightened_image = brighten_image(grayscale_image, factor)
    
    print("# Original Image:")
    print(grayscale_image)
    print("\n")
    print(f"# Brightened Image (after adding {factor}):")
    print(brightened_image)