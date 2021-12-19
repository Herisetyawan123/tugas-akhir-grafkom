from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
from math import *

# Koordinat x dan y untuk posisi kotak
pos_x = -56
pos_y = -10


enemy_x = 60
enemy_y = -20

w, h = 1200, 600
koor_ortoX = (w / 2) / 10
koor_ortoY = (h / 2) / 10

game_over = False
kalah = False
finish = False


deltaX=0
boolGerakX= False


nyawa = 3

# Warna Kotak
hijau = 255
biru = 255
merah = 0


# limit_tanah 
limit_tanah = -20
tembok = (19, -12)
kiri = -58
kanan = 58

# event
lompat = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(- koor_ortoX, koor_ortoX, - koor_ortoY, koor_ortoY)

# Membuat bentuk kotak
def kotak():
    global pos_x, pos_y
    glPushMatrix()
    glColor3f(hijau,biru,merah)
    glTranslated(pos_x, pos_y, 0)
    glBegin(GL_POLYGON)
    # Kiri Atas
    glVertex2f(-2,-2)
    # Kanan Atas
    glVertex2f(2,-2)
    # Kanan Bawah
    glVertex2f(2, 2)
    # Kiri Bawah
    glVertex2f(-2,2)
    glEnd()
    glPopMatrix()

 
def background():
    # glColor3f(0,1,1)
    glColor3ub(105, 200, 255)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(-koor_ortoX,-koor_ortoY)
    # Kanan bawah
    glVertex2f(koor_ortoX,-koor_ortoY)
    # Kanan atas
    glVertex2f(koor_ortoX, koor_ortoY)
    # Kiri atas
    glVertex2f(-koor_ortoX,koor_ortoY)
    glEnd()

def tanah():
    # glColor3f(0,1,1)
    glColor3ub(207, 63, 10)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(-koor_ortoX,-koor_ortoY)
    # Kanan bawah
    glVertex2f(koor_ortoX,-koor_ortoY)
    # Kanan atas
    glVertex2f(koor_ortoX, -22)
    # Kiri atas
    glVertex2f(-koor_ortoX, -22)
    glEnd()

def circle(x, y):
    sides = 32
    glBegin(GL_POLYGON)
    glColor3ub(222, 131, 20)
    for i in range(100):
        cosine=cos(i*2*pi/sides)+x
        sine=sin(i*2*pi/sides)+y
        glVertex2f(cosine,sine)
    glEnd()

def rumput():
    # glColor3f(0,1,1)
    glColor3ub(0, 181, 27)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(-koor_ortoX,-22)
    # Kanan bawah
    glVertex2f(koor_ortoX,-22)
    # Kanan atas
    glVertex2f(koor_ortoX, -24)
    # Kiri atas
    glVertex2f(-koor_ortoX, -24)
    glEnd()

def text(string, x,y,z):
    glRasterPos3f(x,y,z)
    for word in string:
        glColor3f(0,0,0)
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(word))

def display():
    global nyawa
    glClear(GL_COLOR_BUFFER_BIT)
    background()
    tanah()

    bawah = 28
    for x in range(-55, 60, 5):
        circle(x, -bawah)
        if bawah == 28:
            bawah = 26
        else:
            bawah = 28

    # kotak()

    glFlush()

def timer(value): #fungsi timer
    glutTimerFunc(1000//5, timer, 0)  
    # callback function timer dg parameter miliseconds, fungsi yang dipanggil, dan value
    global limit_tanah,pos_x, pos_y,enemy_y, enemy_x, lompat, game_over, tembok, nyawa, kalah, loop, boxx, finish 
    #panggil variabel global kedalam fungsi timer
    if not(game_over) and not(finish):
        # kanan
        if (not( enemy_x + 6 > pos_x > enemy_x - 6) or (pos_y - 6 >= enemy_y)) and not(game_over):
            pass
            if pos_y >= 10 and (34 <= pos_x <= koor_ortoX):
                if not(pos_y in (limit_tanah, 10)):
                    pos_y -= 2  
            elif pos_y >= 4 and (-8 <= pos_x <= 30):
                if not(pos_y in (limit_tanah, 4)):
                    pos_y -= 2  

            elif pos_y >= tembok[1] and pos_x >= 19:
                if not(pos_y in (limit_tanah, tembok[1])):
                    pos_y -= 2    
            elif pos_y >= -6 and (-10 <= pos_x <= 16):
                if not(pos_y in (limit_tanah, -6)):
                    pos_y -= 2 
            elif pos_y >= -2 and (-40 <= pos_x <= -12):
                if not(pos_y in (limit_tanah, -2)):
                    pos_y -= 2  



            elif pos_y > limit_tanah:
                if not(pos_y in (limit_tanah, tembok[1])) or not(pos_y >= tembok[1] and pos_x >= 19):
                    pos_y -= 2       
                
            if enemy_y > limit_tanah :
                enemy_y -= 2
            if enemy_x > -65 and enemy_y == limit_tanah:
                enemy_x -= 2

        elif not(game_over):

            nyawa -= 1
            
            # restart
            pos_x = -56
            pos_y = -10

            kalah = True
            enemy_x = 60
            enemy_y = -20
            if nyawa < 1:
                game_over = True
            time.sleep(1)
        

            # game_over = True
        
        if pos_x == 50 and pos_y == 10:
            finish = True

        if pos_y in (limit_tanah, tembok[1], -6, -2, 4, 10):
            lompat = 0
     
def bendera():
    glColor3f(1.0,1.0,1.)
    glBegin(GL_LINES)
    glVertex2f(50, 20)
    glVertex2f(50, 8)
    glEnd()

    glColor3f(hijau,biru,merah)
    glBegin(GL_POLYGON)
    # Kiri Atas
    glVertex2f(50,20)
    # Kanan Atas
    glVertex2f(55,20)
    # Kanan Bawah
    glVertex2f(50, 18)
    # Kiri Bawah
    glVertex2f(55, 18)
    glEnd()
 
def input_keyboard(key,x,y):
    global pos_x, pos_y, lompat, game_over, finish
    # Untuk mengubah posisi kotak
    if not(game_over) and not(finish):
        if key == GLUT_KEY_UP:
            if lompat < 1:
                pos_y += 10
                lompat += 1
                print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y, lompat)
        elif key == GLUT_KEY_RIGHT:
            if pos_x < 58:
                pos_x += 2
                print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
        elif key == GLUT_KEY_LEFT:
            if pos_x > -58:
                pos_x -= 2
                print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Happy Sunday")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    # glfwGetCursorPos(window,xpos,ypos)
    glutTimerFunc(50, update, 0)
    glutTimerFunc(0,timer,0)
    init()
    glutMainLoop()

main()  