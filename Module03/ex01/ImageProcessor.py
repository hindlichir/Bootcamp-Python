import numpy as np
from PIL import Image


class ImageProcessor:

    def load(self, path):
        array = None
        try:
            open(path, 'r')
        except FileNotFoundError:
            print(FileNotFoundError("No such file or directory"))
        except OSError:
            print(OSError("None"))
        except Exception:
            print(Exception("Something went wrong"))
        else:
            img = Image.open(path, 'r')
            w, h = img.size
            print(f"Loading image of dimensions {w} x {h}")
            array = np.array(img, dtype=np.float32) / 255
        finally:
            return array

    def display(self, array):
        if not type(array).__module__ == np.__name__:
            return
        arr = (array * 255 / np.max(array)).astype('uint8')
        img = Image.fromarray(arr)
        img.show()
