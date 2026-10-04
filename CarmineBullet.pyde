# Координаты круга и его текущий размер
X = 200
Y = 200
XYZ = 150 # Начальный размер (он будет уменьшаться)
XXX = 

# Игровые очки и комбо
score = 0
kombo = 0

def setup():
    size(1000, 600)
    textSize(24)
    spawnCircle() # Создаем первый круг при старте

def draw():
    global XYZ, kombo
    background(0, 0, 65) # Очищаем экран темно-серым цветом
    
    # 1. Выводим счет и комбо на экран
    fill(255)
    text("Score: " + str(score), 20, 40)
    text("Combo: " + str(kombo) + "x", 20, 80)
    
    # 2. Рисуем круг (розовый с белой обводкой)
    stroke(70)       # Белая обводка
    strokeWeight(3)   # Толщина обводки
    fill(255, 230, 0) # Розовый цвет
    ellipse(X, Y, XYZ, XYZ)
    
    # 3. Уменьшаем круг с каждым кадром
    XYZ = XYZ - 2 
    
    # 4. Если круг уменьшился до нуля — игрок промахнулся
    if XYZ <= 0:
        kombo = 0 # Сбрасываем комбо
        spawnCircle() # Создаем новый круг в другом месте

# Функция, которая переносит круг в случайное место и сбрасывает его размер
def spawnCircle():
    global X, Y, XYZ
    X = random(50, width - 50)
    Y = random(50, height - 50)
    XYZ = 150 # Возвращаем большой размер

# Проверка: попал ли игрок по кругу
def checkHit():
    global score, kombo
    # Считаем расстояние от мышки до центра круга
    distance = dist(mouseX, mouseY, X, Y)
    
    # Если расстояние меньше радиуса (половины размера) — это попадание!
    if distance < (XYZ / 2):
        kombo = kombo + 1
        score = score + (100 * kombo) # Очки умножаются на комбо
        spawnCircle() # Убираем этот круг и создаем новый
    else:
        kombo = 0 # Если кликнули мимо круга — сброс комбо

# Проверка нажатия клавиш на клавиатуре (Z и X)
def keyPressed():
    if key == 'z' or key == 'x' or key == 'Z' or key == 'X':
        checkHit()

# Проверка клика мышки
def mousePressed():
    if mouseButton == LEFT:
        checkHit()
