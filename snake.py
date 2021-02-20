from turtle import Screen,Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#GENEL AYARLAMALARI UST TARAFTA BILDIRIYORUZ.

class Snake:
    def __init__(self):
        self.segments = []
        #Ilk etap icin 3 adet segment oluşturmak üzere, yılanımızı oluşturuyoruz.
        self.createSneak()
        self.head = self.segments[0]



    def createSneak(self):
        for position in STARTING_POSITIONS: #ILK SEGMENTLERIMIZIN POZISYONU BELLI OLDUGU ICIN BELLI POZISYONLARI GONDERERK OLUSTURUYORUZ.
            self.addSegments(position)

    #SEGMENTLERIMIZI OLUSTURUP LISTEMIZE EKLIYORUZ. BOYLELIKLE 'SNAKE'MIZIN HER SEGMENTININ BULUNDUGU BIR LISTE ELDE EDIYORUZ.
    def addSegments(self,position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extandSegment(self):
        self.addSegments(self.segments[-1].position())
        '''
            Bu kısıma geldiğimizde, segments[-1] ile segmentlerimizin sonuncusunun pozisyon bilgisini elde ediyoruz.
            Bu bilgiyi addSegmente yolladığımız an için, bizim 3 segmentli bir yılanı da baz alırsak,
            İlk iki segmenti yan yana fakat, üç ve dördüncü segmenti ise bir anlıkta olsa üst üste kalacak.
            yani,
                
                    ### -> yılanın ilk hali
                    [#]## -> yılanın bir segment daha eklendiğindeki hali,
                    
             Bu durumdan ise main dosyamızda while döngüsü içerisinde herhangi bir yanlışla karşılaşıncaya dek devam eden bir
             move fonksiyonu çağrısı sayesinde kurtuluyoruz. Bundan ötürü sürekli hareket eden bir yılan olduğu için, o anlık kısmı görmemiz
             ufak 'delay'lerde bi hayli zor.        
        '''


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # new_x = self.segments[seg_num - 1].xcor()
            # new_y = self.segments[seg_num - 1].ycor()
            position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(position)
        self.head.forward(MOVE_DISTANCE)

        '''
            Peki bu move fonksiyonu işleyişi nasıl?
            Buradaki range() kullanımı, range(for loopunun çalışacağı ilk değer,varacağı son değer,varırken etkileneceği değişim)
            Yani kısaca range(start,stop,state).
            
            Peki range(len(self.segments) -1, 0 ,-1) komudu ne anlatmak istiyor. Listenin son indexi ile başla ve birer birer indir.
            Daha sonra 0'ı gördüğünde loop'u durdur.
            
            
            Loop içerisinde ise farzedelim ki 2. index dönmekte, 2. index dönerken 1. indexin pozisyonunu 2. indexe ata. Böylelikle ikinci index ve birinci indexin yerine geçecek
            ve bir anlığına da olsa aynı pozisyonda yer alacaklar. 
            Daha sonra aynı işlem 1. index dönerken , 1. indexin 0. indexin yerine atanmasıyla devam eder.
            En son kodda da self.head olarak belirttiğimiz, self.segments[0] olan segmenti de MOVE_DISTANE(20px) kadar ileri aktarılır.
            Böylelikle sürekli bu fonksiyon çalışır durumdayken 'Snake'imiz belirtilen açıda ileri doğru hareket eder.
            
        '''



    # 'Snake'mize yön verme.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
