
import os
import os.path

def walk(cwd, txt):
    for el in os.scandir(cwd):
        if el.is_file() and txt in el.name:
            new_path = el.path.replace(txt, "")
            os.rename(el.path, new_path)
        elif el.is_dir():
            walk(el, txt)


if __name__ == '__main__':
    cwd = os.getcwd()
    txt = input()
    walk(cwd, txt)
