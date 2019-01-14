#!/usr/bin/python

import tkinter

import cv2
import PIL.Image
import PIL.ImageTk


window = tkinter.Tk()


# Window configuration fullscreen
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


app = FullScreenApp(window)

straight_line_image = cv2.imread("images/straight_line.jpg")
straight_line_image_height, straight_line_image_width, straight_line_image_no_channels = straight_line_image.shape

circle_image = cv2.imread("images/circle.jpg")
circle_image_height, circle_image_width, circle_image_no_channels = circle_image.shape

canvas = tkinter.Canvas(window, width=straight_line_image_width, height=straight_line_image_height)
canvas.pack()

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(straight_line_image))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

window.mainloop()
