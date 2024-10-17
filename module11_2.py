from PIL import Image


class Folder:
    def __init__(self, name):
        self.name = name

    def image_show(self):
        with Image.open(self.name) as img:
            img.show()

image1 = Folder("Design2\crop_replicated_image3.png")
image1.image_show()