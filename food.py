from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() #Inheritance olayını uyguluyor. Ve Food class'ımızı alt bir class haline getiriyoruz.
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5) # Normalde 20px*20px olan şekli 10px*10px olması için 0.5*20 olarak yazıyoruz.
        self.color('blue')
        self.speed('fastest')
        # Şekli, rengi, hızı gibi bir takım ayarlar yaptıktan sonra, 'food'umuzun oluşmasını sağlıyoruz.
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        #Random kordinatlarda, fakat ekran sınırlarımız içerisinde bir konuma yerleştiriliyor.