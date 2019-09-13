import os
def get_imlist(path, ext):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(ext)]
