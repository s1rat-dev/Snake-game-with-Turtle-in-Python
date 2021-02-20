from turtle import Turtle
FONT = ('Courier',16,'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() # Bir 'Inheritance' olayı görüyoruz.
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-220, 270)
        self.updateScoreboard()
        self.hideturtle() # hide turtle komudu imlecimizi saklar ve yazının görünmesine olanak sağlar. Yapılmadığı taktirde, belirtilen konumda sadece imleç gözükür
                                                                                                                # - tabi ki belirttiğimiz 'shape' özelliğine sahip. -

    def updateScoreboard(self):
        self.write('Score: {0}'.format(self.score), align = ALIGNMENT, font = FONT)
        #Write fonksiyonu ile, (Yazinin_kendisi,Yazinin_duracagi_alignment,yazi_fontu) kurallarını da uygulayarak. Ekrana yazı basımını gerçekleştiriyoruz.
        #Tabi tekrar bir skor yazmak istersek eğer, Aynı pozisyonda üst üste geleceği için,

    def gameOver(self):
        self.goto(0,0)
        self.write('GAME OVER', align = ALIGNMENT, font = FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()
