from PIL import Image
import inspect



class Folder:
    def __init__(self, name):
        self.name = name

    def image_show(self):
        with Image.open(self.name) as img:
            img.load()

image1 = Folder(r"Design2\crop_replicated_image3.png")
image1.image_show()

res = {}
res['type'] = type(image1)
for attr_name in dir(image1):
    attr = getattr(image1, attr_name)
    res['attributes:'] = attr
methods_ = [m[0] for m in inspect.getmembers(image1, predicate=inspect.ismethod)]
res['methods:'] = methods_
res['module:'] = inspect.getmodule(image1)
print(res)