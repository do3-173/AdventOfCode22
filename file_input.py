import os

def file_input(file_name):
    f = open(os.path.join('./input', file_name), "r")
    return f.readlines()