# Import Modules
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtGui import QPixmap

#

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(900, 700)

# Objects/Widgets
btn_folder = QPushButton("Folder")
file_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpen")
gray = QPushButton("B/W")
saturation = QPushButton("Color")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

# Button styles:

btn_folder.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
file_list.setStyleSheet("QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }")
btn_left.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
btn_right.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
mirror.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
sharpness.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
gray.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
saturation.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
contrast.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")
blur.setStyleSheet("""QPushButton { font: 12px Arial; color: gray; border: 1px solid gray; padding-bottom: 4px; padding-top: 4px; padding-left: 8px; padding-right: 8px }
                         QPushButton:hover { background-color: lightgray; color: black }""")

# dropdown menu
filter_box = QComboBox()
filter_box.addItem("Original") # revert to original photo
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpen")
filter_box.addItem("B/W")
filter_box.addItem("Color")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

filter_box.setStyleSheet("""
    QComboBox {
        font: 12px Arial;
        color: gray;
        border: 1px solid gray;
        padding-bottom: 4px;
        padding-top: 4px;
        padding-left: 8px;
        padding-right: 8px;
    }

    QComboBox::drop-down {
        border: 0px;
    }

    QComboBox QAbstractItemView {
        color: gray;
        border: 1px solid gray;
        background-color: #202020;
        selection-background-color: lightgray;
    }
""")


picture_box = QLabel("Image will appear here!")

# App Design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

# column 1
col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)

# column 2
col2.addWidget(picture_box)

# add layouts to master layout
master_layout.addLayout(col1, 20) # stretch argument, takes 20% of the window size
master_layout.addLayout(col2, 80)

# add master layout to the main window
main_window.setLayout(master_layout)

# Functions
working_directory = ""

# filter files and extensions
def filter(files, extensions):
    results = [] # create list
    for file in files: # for file in all files
        for ext in extensions: # for extension in every extension
            if file.endswith(ext): # if file ends with certain extension
                results.append(file) # add to the list
    return results # return list


# Choose current work directory
def getWorkDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory() # open file dialog
    extensions = [".jpg",".jpeg",".png",".svg"]
    filenames = filter(os.listdir(working_directory), extensions)
    file_list.clear() # clear file list
    for filename in filenames:
        file_list.addItem(filename)
        
        
from PIL import Image
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import os

class Editor():
    def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "Edits/"
        
    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_directory, self.filename)
        # Open the image using PIL
        self.image = Image.open(fullname)
        self.original = self.image.copy()  # Take a copy of the current image
        
    def save_image(self):
        # Save the PIL image
        path = os.path.join(working_directory, self.save_folder)
        if not os.path.exists(path):
            os.mkdir(path)
            
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
        
    def show_image(self, path):
        picture_box.hide()
        image = QPixmap(path)
        w, h = picture_box.width(), picture_box.height()
        image = image.scaled(w, h, Qt.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()
        
    def transformImage(self, transformation):
        transformations = {
            "B/W": lambda image: image.convert("L"),
            "Blur": lambda image: image.filter(ImageFilter.BLUR),
            "Left": lambda image: image.transpose(Image.ROTATE_90),
            "Color": lambda image: ImageEnhance.Color(image).enhance(1.2),
            "Right": lambda image: image.transpose(Image.ROTATE_270),
            "Mirror": lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
            "Sharpen": lambda image: image.filter(ImageFilter.SHARPEN),
            "Contrast": lambda image: ImageEnhance.Contrast(image).enhance(1.2),
        }

        transformation_func = transformations.get(transformation)

        if transformation_func:
            self.image = transformation_func(self.image)
            self.save_image()
        
        # Pass the correct path to show_image
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)  # pass the image path here


        
    def apply_filter(self, filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            mapping = {
                "B/W": lambda image: image.convert("L"),
                "Blur": lambda image: image.filter(ImageFilter.BLUR),
                "Left": lambda image: image.transpose(Image.ROTATE_90),
                "Color": lambda image: ImageEnhance.Color(image).enhance(1.2),                
                "Right": lambda image: image.transpose(Image.ROTATE_270),
                "Mirror": lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpen": lambda image: image.filter(ImageFilter.SHARPEN),
                "Contrast": lambda image: ImageEnhance.Contrast(image).enhance(1.2),
            }
            filter_func = mapping.get(filter_name)
            if filter_func:
                self.image = filter_func(self.image)
                self.save_image()
                image_path = os.path.join(working_directory, self.save_folder, self.filename)
                self.show_image(image_path)
            pass
        
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)
        
def handle_filter():
    if file_list.currentRow() >= 0:
        select_filter = filter_box.currentText()
        main.apply_filter(select_filter)
        
def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main.load_image(filename)
        main.show_image(os.path.join(working_directory, main.filename))
        
main = Editor()
        

# Event loop        
btn_folder.clicked.connect(getWorkDirectory) # when folder button is clicked, call the getworkdirectory function
file_list.currentRowChanged.connect(displayImage)
filter_box.currentTextChanged.connect(handle_filter)

gray.clicked.connect(lambda: main.transformImage("B/W"))
btn_left.clicked.connect(lambda: main.transformImage("Left"))
btn_right.clicked.connect(lambda: main.transformImage("Right"))
sharpness.clicked.connect(lambda: main.transformImage("Sharpen"))
saturation.clicked.connect(lambda: main.transformImage("Color"))
contrast.clicked.connect(lambda: main.transformImage("Contrast"))
blur.clicked.connect(lambda: main.transformImage("Blur"))
mirror.clicked.connect(lambda: main.transformImage("Mirror"))

#
main_window.show()
main_window.setStyleSheet("QWidget { background-color: #202020; margin: 0 }")
app.exec_()
