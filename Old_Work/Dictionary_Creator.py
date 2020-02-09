import os
import platform


def dictionary_creator(partition, labels, rel_path):
    img_dir = os.listdir(rel_path + "ASL_Combined_Dataset")
    partition.write("{'train': [")
    triggered = False

    for f in img_dir:
        if not int(f[4]) == 5 and not triggered:
            triggered = True
            partition.write("'" + f + "'")
        elif not int(f[4]) == 5 and triggered:
            partition.write(", '" + f + "'")

    partition.write("], 'validation': [")

    triggered = False

    for f in img_dir:
        if int(f[4]) == 5 and not triggered:
            triggered = True
            partition.write("'" + f + "'")
        elif int(f[4]) == 5 and triggered:
            partition.write(", '" + f + "'")

    partition.write("]}")
    partition.close()

    labels.write("{")
    triggered = False

    for f in img_dir:
        if not triggered:
            triggered = True
            labels.write("'" + f + "': '" + f[6] + "'")
        elif triggered:
            labels.write(", '" + f + "': '" + f[6] + "'")
    labels.write("}")
    labels.close()


# Place the ABSOLUTE FILE PATH TO YOUR Jupyter-Notebook Directory HERE
# For Windows It Will Have a Format Similar to "C:\\Home\\Jupyter_Notebook\\"
# For Linux & Mac it Will Have a Format Similar to "home/user/Jupyter_Notebook/
jupyter_notebook_folder = "/home/yvillia/Jupyter Notebook"

current_dir = os.getcwd()
relative_path = os.path.relpath(jupyter_notebook_folder, current_dir)
operating_system = platform.system()

if not operating_system == "Windows":
    part = open(relative_path + "/files/partition.txt", "w+")
    label = open(relative_path + "/files/labels.txt", "w+")
    relative_path = relative_path + "/"
else:
    part = open(relative_path + "\\files\\partition.txt", "w+")
    label = open(relative_path + "\\files\\partition.txt", "w+")
    relative_path = relative_path + "\\"

dictionary_creator(part, label, relative_path)
