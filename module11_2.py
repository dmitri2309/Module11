# Домашнее задание по теме "ИНТРОСПЕКЦИЯ"

from PIL import Image
import inspect


class Folder:
    def __init__(self, name):
        self.name = name

    def image_show(self):
        with Image.open(self.name) as img:
            img.load()


image1 = Folder(r"Design2\crop_replicated_image3.png")


def introspection_info(obj):
    res = {}
    res['type'] = type(obj)
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        res['attributes:'] = attr
    methods_ = [m[0] for m in inspect.getmembers(obj, predicate=inspect.ismethod)]
    res['methods:'] = methods_
    res['module:'] = inspect.getmodule(obj)
    return res


info = introspection_info(image1)
print(info)
