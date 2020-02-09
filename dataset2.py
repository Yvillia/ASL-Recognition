import os
import shutil
import getpass


def order_data(holder):
    user = getpass.getuser()
    folder = holder
    relative_path = os.path.relpath("/home/" + user + "/" + folder + "/fingerspelling5/dataset5/", os.getcwd())
    send_to = "/home/" + user + "/" + folder + "/" + "Combined_Dataset2/"
    if not os.path.exists(send_to):
        os.mkdir(send_to)
        os.mkdir(send_to + "Training_Data/")
        os.mkdir(send_to + "Testing_Data/")
    (_, folders, _) = next(os.walk(relative_path))
    counter = 0
    for data in folders:
        (_, labels, _) = next(os.walk(relative_path + "/" + str(data)))
        for label in labels:
            (_, _, files) = next(os.walk(relative_path + "/" + str(data) + "/" + str(label)))
            if not os.path.exists(send_to + "Training_Data/" + str(label)):
                os.mkdir(send_to + "Training_Data/" + str(label))
            if not os.path.exists(send_to + "Testing_Data/" + str(label)):
                os.mkdir(send_to + "Testing_Data/" + str(label))
            for file in files:
                if file[0] == 'c':
                    counter = counter + 1
                    if counter % 5 == 0:
                        shutil.copy(relative_path + "/" + str(data) + "/" + str(label) + "/" + str(file), send_to + "Testing_Data/" + str(label))
                    else:
                        shutil.copy(relative_path + "/" + str(data) + "/" + str(label) + "/" + str(file), send_to + "Training_Data/" + str(label))


# Input the Path to the Directory for order_data's parameter (Should Work on Mac? and Definitely Linux)
# If you have windows and are genuinely interested in using the data contact me


order_data("CS196/ASL_Dataset2")

