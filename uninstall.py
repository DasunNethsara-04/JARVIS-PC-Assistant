import pyautogui as gui

class Task():
    def __init__(self, param, n):
        self.param = param
        self.n = n
        gui.press(param)

        for j in range(n):
            gui.press(param)


gui.press('Win')
keyword = "Control Panel"
for i in keyword:
    gui.press(i)

Task("Enter", 0)
Task("Tab", 17)
Task("Space", 0)
Task("Tab", 2)
keyword = "MARK 50"

for i in keyword:
    gui.press(i)

Task("Tab", 5)
Task("Space", 0)
Task("Enter", 0)