"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 14: Building Graphical User Interfaces with Tkinter

Author: Jhesed Tacadena
Date: 2017-01-30

Section 14 Contents:
  92. Introduction to Tkinter
  93. Setting up a GUI with Widgets
  94. Connecting GUI Widgets with Callback Functions
  95. Coding Exercise 7: Creating a Multi-widget GUI

Notes:
  * Contain window and widgets
"""

try:
  # Python 2
  from Tkinter import *
except ImportError:
  # Python 3
  from tkinter import *


if __name__ == '__main__':

  window = Tk()


  window.mainloop()
