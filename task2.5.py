import subprocess
import sys
import os


def def_change_wd():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_pwd = os.chdir(current_dir)
    return new_pwd

def mkdir_for_resized_pic():
    wd = def_change_wd()
    if os.path.isdir('result') != True:
        os.mkdir('result')

def file_list_in_dir():
    file_list = os.listdir('source')
    return file_list

def convert_pic():
    for pic in file_list_in_dir():
        source_path = os.path.join('source/', pic)
        result_path = os.path.join('result/', pic)
        subprocess.run("convert.exe " + source_path  + " -resize 200 " + result_path)

print("start programm")
mkdir_for_resized_pic()
convert_pic()

print("end programm")
