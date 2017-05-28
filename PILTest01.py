from PIL import Image  
pil_im =Image.open("test.jpg").convert('L')  
pil_im.show()