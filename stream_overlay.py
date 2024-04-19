import tkinter as tk
from PIL import Image, ImageTk




class streamGUI():
    def __init__(self):
        self.parent = tk.Tk()
        self.parent.geometry("1920x1080")
        self.parent.title("Spoontastic Stream Overlay")

        #path = os.getcwd()
        #to_resize = Image.open(path+'/images/overlay1.png')

        to_resize = Image.open(r'/Users/ryanjacobs/Desktop/files/mt_battle_overlay/overlay.png')

        to_resize = to_resize.resize((1536, 864), Image.LANCZOS)
        self.score = ImageTk.PhotoImage(to_resize)

        self.score_display = tk.Canvas(self.parent, width=1920, height=1080)
        self.score_display.pack()
        self.score_display.create_image(0,0, image=self.score, anchor='nw')
        self.p1_label = tk.Label(self.parent, font=("copperplate", 28), bg='#FCC110', fg='black')
        self.p1_label.place(x=400, y=55, anchor="center")
        self.p1_team = tk.Label(self.parent, font=("copperplate", 28), bg='#FCC110', fg='gray')
        self.p1_team.place(x=2100, y=60, anchor="center")
        self.p2_team = tk.Label(self.parent, font=("copperplate", 28), bg='#FCC110', fg='#a3a0a0')
        self.p2_team.place(x=2100, y=60, anchor="center")
        self.p2_label = tk.Label(self.parent, font=("copperplate", 28), bg='#FCC110', fg='black')
        self.p2_label.place(x=1150, y=55, anchor="center")
        self.p1_score = tk.Label(self.parent, font=("copperplate", 30), bg='#FCC110', fg='black')
        self.p1_score.place(x=607, y=58, anchor="center")
        self.p2_score = tk.Label(self.parent, font=("copperplate", 30), bg='#FCC110', fg='black')
        self.p2_score.place(x=935, y=58, anchor="center")
        self.tournament = tk.Label(self.parent, font=("copperplate", 18), bg='#FCC110', fg='black')
        self.tournament.place(x=395, y=123, anchor="center")
        self.round = tk.Label(self.parent, font=("copperplate", 18), bg='#FCC110', fg='black')
        self.round.place(x=1072, y=122, anchor="center")
        self.set_format = tk.Label(self.parent, font=("copperplate", 22), bg='#FCC110', fg='black')
        self.set_format.place(x=1250, y=122, anchor="center")


        self.p1_label_centered = False
        self.p2_label_centered = False


    def update_p1_label(self, tag, team):
        label_font_size = 28
        team_font_size = 28
        self.p1_label_centered = False
        p1_label_height = 35
        self.p1_label.config(text=tag, font=("copperplate", label_font_size), bg="#FCC110")
        self.p1_team.config(text=team, font=("copperplate", team_font_size), bg="#FCC110")

        if team == "Team":
            self.p1_team.place(x=2100, y=0)
            while not self.p1_label_centered:
                p1_label_height = 56
                self.parent.update_idletasks()
                tag_width = float(self.p1_label.winfo_width())
                if tag_width > 290:
                    label_font_size -= 1
                    p1_label_height += 0.6
                    self.p1_label.config(font=("copperplate",label_font_size))
                else:
                    self.p1_label.place(x=400, y=p1_label_height, anchor="center")
                    self.p1_label_centered = True

        else:
            self.parent.update_idletasks()
            tag_width = float(self.p1_label.winfo_width())
            team_width = float(self.p1_team.winfo_width())
            total_width = 20+tag_width+team_width
            while total_width > 250:
                p1_label_height += 0.6
                label_font_size -= 1
                team_font_size -= 1
                self.p1_label.config(font=("copperplate", label_font_size))
                self.p1_team.config(font=("copperplate", team_font_size))
                self.p1_label.place(x=2100, y=0)
                self.p1_team.place(x=2100, y=0)
                self.parent.update_idletasks()
                tag_width = float(self.p1_label.winfo_width())
                team_width = float(self.p1_team.winfo_width())
                total_width = 20 + tag_width + team_width
            print(label_font_size)
            target = 400
            center = ((20 + tag_width + team_width) / 2) + 290
            shift = target - center
            print(center, shift)
            self.p1_team.place(x=shift+290, y=p1_label_height, anchor="nw")
            self.p1_label.place(x=shift+295+team_width, y=p1_label_height, anchor="nw")

    def update_p2_label(self, tag, team):
        label_font_size = 28
        team_font_size = 28
        self.p1_label_centered = False
        p2_label_height = 35
        self.p2_label.config(text=tag, font=("copperplate", label_font_size), bg="#FCC110")
        self.p2_team.config(text=team, font=("copperplate", team_font_size), bg="#FCC110")

        if team == "Team":
            self.p2_team.place(x=2100, y=0)
            while not self.p2_label_centered:
                p2_label_height = 56
                self.parent.update_idletasks()
                tag_width = float(self.p2_label.winfo_width())
                if tag_width > 290:
                    label_font_size -= 1
                    p2_label_height += 0.6
                    self.p2_label.config(font=("copperplate", label_font_size))
                else:
                    self.p2_label.place(x=1150, y=p2_label_height, anchor="center")
                    self.p2_label_centered = True

        else:
            self.parent.update_idletasks()
            tag_width = float(self.p2_label.winfo_width())
            team_width = float(self.p2_team.winfo_width())
            total_width = 20 + tag_width + team_width
            while total_width > 250:
                p2_label_height += 0.6
                label_font_size -= 1
                team_font_size -= 1
                self.p2_label.config(font=("copperplate", label_font_size))
                self.p2_team.config(font=("copperplate", team_font_size))
                self.p2_label.place(x=2100, y=0)
                self.p2_team.place(x=2100, y=0)
                self.parent.update_idletasks()
                tag_width = float(self.p2_label.winfo_width())
                team_width = float(self.p2_team.winfo_width())
                total_width = 20 + tag_width + team_width
            print(label_font_size)
            target = 1150
            center = ((20 + tag_width + team_width) / 2) + 980
            shift = target - center
            print(center, shift)
            self.p2_team.place(x=shift + 980, y=p2_label_height, anchor="nw")
            self.p2_label.place(x=shift + 985 + team_width, y=p2_label_height, anchor="nw")


    def update_p1_team(self, value):
        self.p1_team.config(text=value)

    def update_p2_team(self, value):
        self.p2_team.config(text=value)

    def update_p1_score(self, value):
        self.p1_score.config(text=value)

    def update_p2_score(self, value):
        self.p2_score.config(text=value)

    def update_tournament(self, value):
        self.tournament.config(text=value)

    def update_round(self, value):
        font_size = 20
        self.round.config(text=value)
        self.round.config(font=("copperplate", font_size))
        self.round.place(x=2100, y=0)
        self.parent.update_idletasks()
        width = self.round.winfo_width()
        while width > 175:
            font_size -= 1
            self.round.config(font=("copperplate", font_size))
            self.round.place(x=2100, y=0)
            self.parent.update_idletasks()
            width = self.round.winfo_width()
            print(width)

        self.round.place(x=1072, y=122, anchor="center")










    def update_set_format(self, value):
        if value == "3":
            self.set_format.config(text="Bo3")
        else:
            self.set_format.config(text="Bo5")

    def get_parent(self):
        return self.parent



    def launch_stream_overlay(self):
        self.parent.mainloop()







