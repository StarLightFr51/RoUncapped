import os
import tkinter as tk
from tkinter import ttk

class assets:
    def add_label(self, parent, text: str, font: str, textsize, fonttype: str):
        self.label = ttk.Label(parent, text=text, font=(font, textsize, fonttype))
        self.label.pack()

    def add_entry(self, parent):
        self.spinbox = ttk.Spinbox(parent)
        self.spinbox.pack(pady=25)
        self.contents = tk.StringVar()
        self.contents.set("")
        self.spinbox["textvariable"] = self.contents

        self.spinbox.bind('<Key-Return>', self.set_fps)

    def set_fps(self, event):
        if self.contents.get().isdigit():
            self.path = os.getenv('LOCALAPPDATA') + '\\Roblox\\Versions'

            if os.path.exists(self.path):
                for file in os.listdir(self.path):
                    if os.path.exists(f'{self.path}\\{file}\\RobloxPlayerLauncher.exe'):
                        if not os.path.exists(f'{self.path}\\{file}\\ClientSettings'):
                            os.mkdir(f'{self.path}\\{file}\\ClientSettings')

                        else:
                            if not os.path.exists(f'{self.path}\\{file}\\ClientSettings\\ClientAppSettings.json'):
                                self.f = open(self.path + '\\' + file + '\\ClientSettings\\ClientAppSettings.json', 'x')
                                self.f = open(self.path + '\\' + file + '\\ClientSettings\\ClientAppSettings.json', 'w')
                                self.f.write("{\n\"DFIntTaskSchedulerTargetFps\" : " + self.contents.get() + "\n}")
                                self.f.close()
                        if not os.path.exists(f'{self.path}\\{file}\\ClientSettings\\ClientAppSettings.json'):
                            self.f = open(self.path + '\\' + file + '\\ClientSettings\\ClientAppSettings.json', 'x')
                            self.f = open(self.path + '\\' + file + '\\ClientSettings\\ClientAppSettings.json', 'w')
                            self.f.write("{\n\"DFIntTaskSchedulerTargetFps\" : " + self.contents.get() + "\n}")
                            self.f.close()
                        else:
                            self.f = open(self.path + '\\' + file + '\\ClientSettings\\ClientAppSettings.json', 'w')
                            self.f.write("{\n\"DFIntTaskSchedulerTargetFps\" : " + self.contents.get() + "\n}")
                            self.f.close()


        else:
            pass
