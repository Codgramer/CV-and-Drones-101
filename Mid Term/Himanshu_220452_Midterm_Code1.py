from PIL import Image, ImageEnhance

def ig_filter(image_path):
    original_image = Image.open(image_path)

    brightness = ImageEnhance.Brightness(original_image)
    darkened_image = brightness.enhance(0.5)

    contrast = ImageEnhance.Contrast(darkened_image)
    high_contrast_image = contrast.enhance(1.5)

    saturation = ImageEnhance.Color(high_contrast_image)
    final_image = saturation.enhance(1.5)

    original_image.show()
    final_image.show() 

image_path = r"C:\Users\Himanshu\Downloads\7894418522_c15f958d54_b.jpg"
ig_filter(image_path)
