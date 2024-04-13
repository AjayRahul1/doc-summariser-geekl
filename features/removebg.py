from rembg import remove
from PIL import Image

# Input_path = 'some_file_name.extension'
removebg_image = lambda input_image_path: remove(Image.open(input_image_path)) # input_image_path type: str
