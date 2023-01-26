import os


def new_directory(directory, filename):
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    os.chdir(directory)
    with open(filename, "x") as file:
        pass
    os.chdir("..")
    return os.listdir(directory)


if __name__ == '__main__':
    print(new_directory("PythonPrograms", "script.py"))
