##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Import
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.fullscreen = False


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Import


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Class Main App
class MainApp(MDApp):
    # Start Function Main App
    def build(self):
        return Builder.load_file("style.kv")

    # End Function Main App

    # Start Function State
    def __init__(self, state=True, Score_player_X=0, Score_player_O=0, **kwargs):
        super().__init__(**kwargs)
        self.state = state
        self.Score_player_X = Score_player_X
        self.Score_player_O = Score_player_O

    # End Function State

    # Start Functions Buttons
    def button_1(self):
        btn_1 = self.root.ids.btn_1
        if self.state:
            if btn_1.text == "":
                btn_1.text = "X"
                self.state = False
        else:
            if btn_1.text == "":
                btn_1.text = "O"
                self.state = True

    def button_2(self):
        btn_2 = self.root.ids.btn_2
        if self.state:
            if btn_2.text == "":
                btn_2.text = "X"
                self.state = False
        else:
            if btn_2.text == "":
                btn_2.text = "O"
                self.state = True

    def button_3(self):
        btn_3 = self.root.ids.btn_3
        if self.state:
            if btn_3.text == "":
                btn_3.text = "X"
                self.state = False
        else:
            if btn_3.text == "":
                btn_3.text = "O"
                self.state = True

    def button_4(self):
        btn_4 = self.root.ids.btn_4
        if self.state:
            if btn_4.text == "":
                btn_4.text = "X"
                self.state = False
        else:
            if btn_4.text == "":
                btn_4.text = "O"
                self.state = True

    def button_5(self):
        btn_5 = self.root.ids.btn_5
        if self.state:
            if btn_5.text == "":
                btn_5.text = "X"
                self.state = False
        else:
            if btn_5.text == "":
                btn_5.text = "O"
                self.state = True

    def button_6(self):
        btn_6 = self.root.ids.btn_6
        if self.state:
            if btn_6.text == "":
                btn_6.text = "X"
                self.state = False
        else:
            if btn_6.text == "":
                btn_6.text = "O"
                self.state = True

    def button_7(self):
        btn_7 = self.root.ids.btn_7
        if self.state:
            if btn_7.text == "":
                btn_7.text = "X"
                self.state = False
        else:
            if btn_7.text == "":
                btn_7.text = "O"
                self.state = True

    def button_8(self):
        btn_8 = self.root.ids.btn_8
        if self.state:
            if btn_8.text == "":
                btn_8.text = "X"
                self.state = False
        else:
            if btn_8.text == "":
                btn_8.text = "O"
                self.state = True

    def button_9(self):
        btn_9 = self.root.ids.btn_9
        if self.state:
            if btn_9.text == "":
                btn_9.text = "X"
                self.state = False
        else:
            if btn_9.text == "":
                btn_9.text = "O"
                self.state = True

    # End Functions Buttons

    # Start Functions Delete Value
    def Delete_value(self):
        btn_1 = self.root.ids.btn_1
        btn_2 = self.root.ids.btn_2
        btn_3 = self.root.ids.btn_3
        btn_4 = self.root.ids.btn_4
        btn_5 = self.root.ids.btn_5
        btn_6 = self.root.ids.btn_6
        btn_7 = self.root.ids.btn_7
        btn_8 = self.root.ids.btn_8
        btn_9 = self.root.ids.btn_9

        btn_1.text = ""
        btn_2.text = ""
        btn_3.text = ""
        btn_4.text = ""
        btn_5.text = ""
        btn_6.text = ""
        btn_7.text = ""
        btn_8.text = ""
        btn_9.text = ""

    # End Functions Delete Value

    # Start Functions Play Again
    def play_again(self):
        MainApp.Delete_value(self)
        self.state = True
        result = self.root.ids.result
        result_score = self.root.ids.result_score
        turn = self.root.ids.turn

        result.text = ""
        result_score.text = ""
        turn.text = "Turn : Player 'X'"

    # End Functions Play Again

    # Start Functions Law Game
    def Law(self):
        # Start Variables Buttons
        btn_1 = self.root.ids.btn_1
        btn_2 = self.root.ids.btn_2
        btn_3 = self.root.ids.btn_3
        btn_4 = self.root.ids.btn_4
        btn_5 = self.root.ids.btn_5
        btn_6 = self.root.ids.btn_6
        btn_7 = self.root.ids.btn_7
        btn_8 = self.root.ids.btn_8
        btn_9 = self.root.ids.btn_9
        result = self.root.ids.result
        result_score = self.root.ids.result_score
        turn = self.root.ids.turn
        # End Variables Buttons

        if self.state:
            turn.text = "Turn : Player 'X'"
        else:
            turn.text = "Turn : Player 'O'"

        # Start If Main Game For X
        if btn_1.text == "X" and btn_2.text == "X" and btn_3.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_4.text == "X" and btn_5.text == "X" and btn_6.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_7.text == "X" and btn_8.text == "X" and btn_9.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_1.text == "X" and btn_4.text == "X" and btn_7.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_2.text == "X" and btn_5.text == "X" and btn_8.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_3.text == "X" and btn_6.text == "X" and btn_9.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_1.text == "X" and btn_5.text == "X" and btn_9.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_3.text == "X" and btn_5.text == "X" and btn_7.text == "X":
            result.text = "Result Is : Player 'X' Wins"
            self.state = True
            self.Score_player_X += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"
        # End If Main Game For X

        # Start If Main Game For O
        if btn_1.text == "O" and btn_2.text == "O" and btn_3.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_4.text == "O" and btn_5.text == "O" and btn_6.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_7.text == "O" and btn_8.text == "O" and btn_9.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_1.text == "O" and btn_4.text == "O" and btn_7.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_2.text == "O" and btn_5.text == "O" and btn_8.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_3.text == "O" and btn_6.text == "O" and btn_9.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_1.text == "O" and btn_5.text == "O" and btn_9.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"

        elif btn_3.text == "O" and btn_5.text == "O" and btn_7.text == "O":
            result.text = "Result Is : Player 'O' Wins"
            self.state = True
            self.Score_player_O += 1
            MainApp.Delete_value(self)
            result_score.text = f"Score Player 'X' Is : {self.Score_player_X}" \
                                f"    Score Player 'O' Is : {self.Score_player_O}"
        # End If Main Game For O
    # End Functions Law Game


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Class Main App


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Run App
if __name__ == "__main__":
    MainApp().run()
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Run App
