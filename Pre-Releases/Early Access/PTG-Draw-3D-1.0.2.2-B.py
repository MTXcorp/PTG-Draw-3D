import turtle as t
import os
#Defining the Menus
def main_menu_file():
    os.system("cls")
    print("PTG Draw 3D")
    print("1 = Create A Drawing")
    print("2 = Load A Drawing")
    print("3 = Check Version")
    print("4 = Exit")
    Input1 = input("|>")
def Set_name():
    os.system("cls")
    print("Name Of Drawing?")
    name = input("|>")
    main_menu_shape()
def main_menu_shape():
    os.system("cls")
    print(name + " - PTG Draw 3D")
    print("1 = Add A Shape")