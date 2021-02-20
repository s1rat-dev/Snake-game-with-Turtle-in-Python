from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

#Kullanımı kolaylaştırmak amacıyla Snake,Scoreboard ve Food olarak üç ayrı class oluşturup module halinde import ediyoruz.


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(False) #Ekrandaki otomatik update özelliğini kapatır. Manual olarak kendiniz yapmak istiyorsanız  bu özelliği kapatmanız gerekiyor.
screen.title('My Snake Game')


snake = Snake()
scoreBoard = Scoreboard()
food = Food()


#Screen Event Listeners
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')



game_is_on = True
while game_is_on:
    screen.update() # Her hareket edildiğinde görüntüyü update ederiz, sanki bir animasyonun karelerini birleştiriyormuşuz gibi düşünülebilir.
    time.sleep(0.075)# Burada time.sleep olmamış olsa o kadar hızlı bir animasyon elde ederiz ki, kontrol etmesi imkansızlaşır.
    snake.move()


    # Eğer 'snake'miz 'food'unu yerse,
    if snake.head.distance(food) < 15: # Distance pixeller arası mesafeyi bildirir. Bunu anlık olarak hareket ederken while içerisine
        #yazarsanız, sisteminiz için gerekli olan minimum mesafeyi elde edip, onu kullanabilirsiniz.
        food.refresh() #Ortaya 7.5px çaplı daire olarak çıkan yemler, yeni bir koordinatla tekrar oluşturulur ve yerleştirilir.
        snake.extandSegment()#Yeni bir turtle oluşturup onu yılanımızın önüne ekleyen fonksiyonu çalıştırır.
        scoreBoard.increaseScore()#Ekrandaki skor bir puan artar.

    # Yılanımızın hangi ekran aralığında yürür olacağına karar veriyoruz.
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreBoard.gameOver()


    # Yılanımız kendine değdiği vakit, ki bu kendi kafası kendine değemeyeceği için, 'list sliding' olayını uygulayarak. Head
    # haricindeki segmentlerin head ile arasındaki mesafe 10px'den az mı diye kontrol ediyoruz. 10pxden az olduğu vakit, anlıyoruz
    # ki yılanımızın bir segmenti ile kafası çarpışmış.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreBoard.gameOver()




screen.exitonclick()