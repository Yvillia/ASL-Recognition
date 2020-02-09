# ASL-Recognition
### American Sign Language - Machine Learning Project Using Pytorch and Flask

This project was part of a Gitlab Group Project for a CS 196-25 Honors course that was an open-ended project of choice regarding a topic in AI. I ended up doing most of the project when the other group members got too busy, so I am sharing the work that I did on the project on my personal account.

Original Project Link: https://gitlab.engr.illinois.edu/noahrr2/asl-recognition

Unless otherwise explicitly stated the work used is entirely my own code.


# How to Setup
## First Go to the Directory that Will Hold Your Jupyter-Notebook Projects. For simplicity I will refer to this directory as the `JN_Dir`
### Follow the Checklist Below to setup the DataLoader

1. [ ] Download all 5 Massey Datasets from https://www.massey.ac.nz/~albarcza/gesture_dataset2012.html and store all 5 of them in a folder named `ASL_Combined_Dataset`

2. [ ] Place the `ASL_Combined_Dataset` into your `JN_Dir`

3. [ ] Next Download dataset A from https://empslocal.ex.ac.uk/people/staff/np331/index.php?section=FingerSpellingDataset and place it
        in whatever folder you like, I used `CS196/ASL_Dataset2` as my path

4. [ ] Download the `dataset2.py` file and edit the `order_data(PATH)`
        to have `PATH`=the location where you put the dataset named "fingerspelling5"

5. [ ] Run the Code, Contact me for any errors, it will probably not work on Windows (you just have to change the slashes)
        and it MIGHT work for mac. It definitely works for Linux.

6. [ ] Copy the new folder that was created in your PATH and place it inside of your JN_Dir

7. [ ] Open Jupyter Notebook in your JN_Dir and run the most current model cells

8. [ ] All Set to Train


### Current Best Testing Results:
    Test Accuracy: 93.60321384425217%
    
## How to Setup Website

1. [ ] Download ASL_Website from this Github and Place it in a Directory of Your Choosing

2. [ ] Follow the Instructions For the Virtual Environment (`venv`) Setup From https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
        and make sure it is setup in the same directory as the flask code (This is also a really good tutorial for flask if anyone is interested)

3. [ ] Like given in the instructions make sure that you call `source venv/bin/activate` (or windows equivalent) and then you can call Flask run

4. [ ] Open a Web browser to `localhost:5000/` and the webpage will load up. Feel free to edit or mess around with the website.

5. [ ] To Send pictures to the model from the website open jupyter-notebook from the same directory and run `Camera_Script.py.ipynb`
        (You may have to Download opencv prereqs). Press space to take a picture.

