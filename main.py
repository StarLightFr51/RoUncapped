"""
-------------------------------------------------------------------------------------------
Made by StarL1ght (Discord)
Hello you who have downloaded this open source software I'm just a beginner in python software development and
if you want upgrade it the code and the ui do it if you want.
A software for uncapped his fps (frame per seconds) in roblox (fps are capped at 60)

Thanks for downloading the source code and upgrade it
-------------------------------------------------------------------------------------------
"""

# import
import os
import glob
import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('RoUncapped')
root.geometry('400x400')

list_of_files = glob.glob(os.getenv('LOCALAPPDATA') + '/Roblox/Versions/*')
lastest_file = max(list_of_files, key=os.path.getctime)

ClientSettingsFolderPath = lastest_file + '\\ClientSettings'
ClientSettingsFilePath = lastest_file + '\\ClientSettings\\ClientAppSettings.json'
AppDataFolderPath = os.getenv('APPDATA') + '\\' + '.RoUncapped'
DataFolderPath = AppDataFolderPath + '\\' + 'Data'
AncienFPSFilePath = DataFolderPath + '\\' + 'AncienFPS.data'

AncienFpsFile = open(AncienFPSFilePath, 'r').read()
if AncienFpsFile == '':
    AncienFpsFile = 'None'


FPS_Text_Indication = ttk.Label(root, text="Choose the amount of FPS you want to be capped : ")
FPS_Text_Indication.pack()

FPS_Selector = ttk.Spinbox(root, from_=1, to=10000000000000000000000000000, wrap=True)
FPS_Selector.pack(pady=10)

DEFAULT_FPS = 60
FPS = 0

AncienFPS_Indication = ttk.Label(root, text="Last Choosen FPS : " + str(AncienFpsFile))
AncienFPS_Indication.pack(pady=5)


def save_fps():

    FPS = int(FPS_Selector.get())
    file = open(ClientSettingsFilePath, "w+")
    AnicenFPSFile = open(AncienFPSFilePath, "w")

    if FPS > 10000000000000000000000000000:
        FPS = 10000000000000000000000000000
    elif FPS < 1:
        FPS = 1

    AnicenFPSFile.write(str(FPS))
    AnicenFPSFile.close()
    file.write("{\n\"DFIntTaskSchedulerTargetFps\" : " + str(FPS) + "\n}")
    confirm_label = ttk.Label(root, text="Your FPS have been successfully saves !")
    confirm_label.pack(pady=5)

    confirm_label.after(3000, lambda : confirm_label.destroy())


Selection_Button = ttk.Button(root, text="Save Changes", command=save_fps)
Selection_Button.pack(pady=15)

if not os.path.exists(ClientSettingsFolderPath):
    os.mkdir(ClientSettingsFolderPath)

if not os.path.exists(ClientSettingsFilePath):
    file = open(ClientSettingsFilePath, "w+")
    file.write("{\n\"DFIntTaskSchedulerTargetFps\" : " + str(DEFAULT_FPS) + "\n")

if not os.path.exists(AppDataFolderPath):
    os.mkdir(AppDataFolderPath)

if not os.path.exists(DataFolderPath):
    os.mkdir(DataFolderPath)

if not os.path.exists(AncienFPSFilePath):
    file = open(AncienFPSFilePath, 'w+')
    file.close()

root.mainloop()
