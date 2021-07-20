try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class Quiz:
    pass


class HvsAI:
    pass


class LearnArt:
    pass


class HowToPlay:
    pass


class Settings:
    pass


class Menu:
    root = Tk()
    root.title('Start Menu')

    HEIGHT = 550
    WIDTH = 800

    root.geometry(f'{HEIGHT}x{WIDTH}')

    root.minsize(WIDTH, HEIGHT)
    root.maxsize(WIDTH, HEIGHT)

    QuizBtn = Button(root,
                     text='QUIZ',
                     font=('times', 15, 'bold'),
                     borderwidth='4',
                     fg='#5778BB',
                     bg='#9C9FA5',
                     width='36',
                     command=lambda: Quiz())  # Destroys current window and runs class Quiz

    QuizBtn.place(relx=0.15, rely=0.20,
                  relheight=0.090, relwidth=0.68)

    HvsAIBtn = Button(root,
                      text='Human Vs. AI',
                      font=('times', 15, 'bold'),
                      borderwidth='4',
                      fg='#5778BB',
                      bg='#9C9FA5',
                      width='36',
                      command=lambda: HvsAI())  # Destroys current window and runs class HvsAI

    HvsAIBtn.place(relx=0.15, rely=0.32,
                   relheight=0.090, relwidth=0.68)

    LearnArtBtn = Button(root,
                         text='Learn about Art',
                         font=('times', 15, 'bold'),
                         borderwidth='4',
                         fg='#5778BB',
                         bg='#9C9FA5',
                         width='36',
                         command=lambda: LearnArt())  # Destroys current window and runs class LearnArt

    LearnArtBtn.place(relx=0.15, rely=0.44,
                      relheight=0.090, relwidth=0.68)

    HowToPlayBtn = Button(root,
                          text='How To Play',
                          font=('times', 15, 'bold'),
                          borderwidth='4',
                          fg='#5778BB',
                          bg='#9C9FA5',
                          width='36',
                          command=lambda: HowToPlay())  # Destroys current window and runs class HowToPlay

    HowToPlayBtn.place(relx=0.15, rely=0.68,
                       relheight=0.090, relwidth=0.68)

    SettingsBtn = Button(root,
                         text='Settings',
                         font=('times', 15, 'bold'),
                         borderwidth='4',
                         fg='#5778BB',
                         bg='#9C9FA5',
                         width='36',
                         command=lambda: Settings())  # Destroys current window and runs class Settings

    SettingsBtn.place(relx=0.15, rely=0.80,
                      relheight=0.090, relwidth=0.68)

    root.mainloop()


Menu()
