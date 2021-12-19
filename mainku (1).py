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

def orang():
        global pos_x, pos_y
        glPushMatrix()
        glTranslated(pos_x - 6, pos_y - 1, -1)
        # glRotatef(180.0, 0.0, 1.0, 1.0)
        glScaled(0.03, 0.03, 0)
        glBegin(GL_POLYGON)
        glColor3ub(240, 230, 140) #untuk mewarnai objek
        glVertex2f(257.416666666667, 176.3)
        glVertex2f(250, 180)
        glVertex2f(246.75, 184.033333333333)
        glVertex2f(242.483333333334, 188.833333333333)
        glVertex2f(240, 180)
        glVertex2f(229.683333333334, 178.033333333333)
        glVertex2f(221.95, 173.9)
        glVertex2f(220.083333333334, 166.833333333333)
        glVertex2f(219.55, 157.5)
        glVertex2f(220.216666666667, 151.5)
        glVertex2f(216.616666666667, 155.633333333333)
        glVertex2f(212.483333333334, 158.033333333333)
        glVertex2f(207.15, 156.166666666667)
        glVertex2f(206.083333333334, 151.633333333333)
        glVertex2f(207.283333333334, 147.5)
        glVertex2f(210.35, 143.633333333333)
        glVertex2f(214.483333333334, 141.1)
        glVertex2f(220, 140)
        glVertex2f(214.35, 134.966666666667)
        glVertex2f(208.483333333334, 132.966666666667)
        glVertex2f(200, 120)
        glVertex2f(200.083333333334, 115.1)
        glVertex2f(239.95, 115.1)
        glVertex2f(240, 120)
        glVertex2f(247.95, 124.833333333334)
        glVertex2f(253.15, 129.9)
        glVertex2f(257.15, 135.766666666667)
        glVertex2f(259.016666666667, 142.166666666667)
        glVertex2f(259.95, 152.833333333334)
        glVertex2f(265.816666666667, 154.3)
        glVertex2f(267.816666666667, 156.966666666667)
        glVertex2f(263.416666666667, 158.966666666667)
        glVertex2f(260, 160)
        glEnd()

 
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255)
        glVertex2f(257.416666666667, 176.3)
        glVertex2f(255.683333333334, 184.3)
        glVertex2f(254.35, 188.566666666667)
        glVertex2f(250.35, 193.633333333333)
        glVertex2f(245.683333333334, 196.7)
        glVertex2f(236.35, 197.766666666666)
        glVertex2f(219.55, 198.7)
        glVertex2f(202.216666666667, 196.966666666666)
        glVertex2f(193.55, 189.5)
        glVertex2f(189.15, 184.033333333333)
        glVertex2f(186.35, 178.966666666666)
        glVertex2f(182.083333333334, 172.433333333333)
        glVertex2f(180, 140)
        glVertex2f(175.888596491232, 98.28157894737)
        glVertex2f(200.083333333334, 115.1)
        glVertex2f(200, 120)
        glVertex2f(208.483333333334, 132.966666666667)
        glVertex2f(214.35, 134.966666666667)
        glVertex2f(220, 140)
        glVertex2f(214.483333333334, 141.1)
        glVertex2f(210.35, 143.633333333333)
        glVertex2f(207.283333333334, 147.5)
        glVertex2f(206.083333333334, 151.633333333333)
        glVertex2f(207.15, 156.166666666667)
        glVertex2f(212.483333333334, 158.033333333333)
        glVertex2f(216.616666666667, 155.633333333333)
        glVertex2f(220.216666666667, 151.5)
        glVertex2f(219.55, 157.5)
        glVertex2f(220.083333333334, 166.833333333333)
        glVertex2f(221.95, 173.9)
        glVertex2f(229.683333333334, 178.033333333333)
        glVertex2f(240, 180)
        glVertex2f(242.483333333334, 188.833333333333)
        glVertex2f(246.75, 184.033333333333)
        glVertex2f(250, 180)
        glEnd()


        glBegin(GL_POLYGON)
        glColor3ub(0, 0, 0)
        glVertex2f(246.011403508777, 168.132456140353)
        glVertex2f(242.783333333338, 167.290350877195)
        glVertex2f(241.730701754391, 165.044736842107)
        glVertex2f(242.713157894742, 162.939473684213)
        glVertex2f(244.678070175443, 161.325438596493)
        glVertex2f(247.204385964917, 161.114912280704)
        glVertex2f(249.590350877198, 162.58859649123)
        glVertex2f(250, 165.0)
        glVertex2f(248.537719298251, 167.079824561406)
        glEnd()


        glBegin(GL_TRIANGLES)
        glColor3ub(255, 0, 0)
        glVertex2f(248.835964912286, 147.70263157895)
        glVertex2f(250.730701754391, 134.913157894739)
        glVertex2f(257.204385964917, 144.071052631581)
        glEnd()

        glBegin(GL_QUADS)
        glColor3ub(255, 215, 0)
        glVertex2f(200.083333333334, 115.1)
        glVertex2f(200, 110)
        glVertex2f(239.95, 115.1)
        glVertex2f(240, 110)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 0)
        glVertex2f(190, 80)
        glVertex2f(200, 110)
        glVertex2f(195.75, 103.166666666667)
        glVertex2f(192.55, 94.166666666667)
        glVertex2f(190, 80)
        glVertex2f(189.15, 67.766666666667)
        glVertex2f(188.55, 49.366666666667)
        glVertex2f(170, 20)
        glVertex2f(260,20)
        glVertex2f(245.55, 50.766666666667)
        glVertex2f(246.15, 57.566666666667)
        glVertex2f(246.75, 70.566666666667)
        glVertex2f(245.55, 82.966666666667)
        glVertex2f(243.75, 94.766666666667)
        glVertex2f(242.15, 103.966666666667)
        glVertex2f(240, 110)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3ub(255, 255, 0)
        glVertex2f(189.15, 67.766666666667)
        glVertex2f(240, 110)
        glVertex2f(200, 110)
        glEnd()


        glBegin(GL_POLYGON)
        glColor3ub(255, 215, 0)
        glVertex2f(210, 100)
        glVertex2f(206.850000000002, 94.566666666667)
        glVertex2f(206.650000000002, 86.166666666667)
        glVertex2f(207.850000000002, 80.566666666667)
        glVertex2f(220, 80)
        glVertex2f(221.250000000002, 87.366666666667)
        glVertex2f(221.450000000002, 94.566666666667)
        glVertex2f(220, 100)
        glEnd()


        glBegin(GL_QUADS)
        glColor3ub(240, 230, 140)
        glVertex2f(210, 80)
        glVertex2f(207.672222222224, 44.511111111111)
        glVertex2f(215.583333333335, 44.244444444445)
        glVertex2f(216.0, 80)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3ub(240, 230, 140)
        glVertex2f(207.672222222224, 44.511111111111)
        glVertex2f(205.538888888891, 43.266666666667)
        glVertex2f(204.116666666669, 40.777777777778)
        glVertex2f(204.472222222224, 36.6)
        glVertex2f(207.138888888891, 35.266666666667)
        glVertex2f(210, 35.0)
        glVertex2f(213.538888888891, 34.911111111111)
        glVertex2f(216.738888888891, 35.977777777778)
        glVertex2f(217.983333333335, 38.822222222223)
        glVertex2f(217.62777777778, 41.044444444445)
        glVertex2f(215.583333333335, 44.244444444445)
        glEnd()


        glBegin(GL_QUADS)
        glColor3ub(240, 230, 140)
        glVertex2f(200, 20)
        glVertex2f(200, -20)
        glVertex2f(210, -20)
        glVertex2f(210, 20)
        glEnd()


        glBegin(GL_QUADS)
        glColor3f(128, 0, 0)
        glVertex2f(200, -20)
        glVertex2f(200, -30)
        glVertex2f(220, -30)
        glVertex2f(220, -20)
        glEnd()


        glBegin(GL_QUADS)
        glColor3ub(128, 0, 0)
        glVertex2f(210, -15.433333333333)
        glVertex2f(222.583333333336, -15.433333333333)
        glVertex2f(222.716666666669, -25.3)
        glVertex2f(220, -25.3)
        glEnd()
        glPopMatrix()

# Membuat bentuk kotak
# def kotak():
#     global pos_x, pos_y
#     glPushMatrix()
#     glColor3f(hijau,biru,merah)
#     glTranslated(pos_x, pos_y, 0)
#     glBegin(GL_POLYGON)
#     # Kiri Atas
#     glVertex2f(-2,-2)
#     # Kanan Atas
#     glVertex2f(2,-2)
#     # Kanan Bawah
#     glVertex2f(2, 2)
#     # Kiri Bawah
#     glVertex2f(-2,2)
#     glEnd()
#     glPopMatrix()

def enemy():
    global enemy_x, enemy_y
    glPushMatrix()
    glColor3f(hijau,1,1)
    glTranslated(enemy_x, enemy_y, 0)

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

def tembok1():
    # glColor3f(0,1,1)
    glColor3ub(207, 63, 10)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(20,-16)
    # Kanan bawah
    glVertex2f(koor_ortoX,-16)
    # Kanan atas
    glVertex2f(koor_ortoX, -14)
    # Kiri atas
    glVertex2f(20, -14)
    glEnd()

def tembok2():
        # glColor3f(0,1,1)
    glColor3ub(207, 63, 10)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(-10,-10)
    # Kanan bawah
    glVertex2f(16,-10)
    # Kanan atas
    glVertex2f(16, -8)
    # Kiri atas
    glVertex2f(-10, -8)
    glEnd()

def tembok3():
        # glColor3f(0,1,1)
    glColor3ub(207, 63, 10)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(-40,-6)
    # Kanan bawah
    glVertex2f(-12,-6)
    # Kanan atas
    glVertex2f(-12, -4)
    # Kiri atas
    glVertex2f(-40, -4)
    glEnd()

def tembok4():
        # glColor3f(0,1,1)
    glColor3ub(207, 63, 10)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(-8,0)
    # Kanan bawah
    glVertex2f(30,0)
    # Kanan atas
    glVertex2f(30, 2)
    # Kiri atas
    glVertex2f(-8, 2)
    glEnd()

def tembok5():
    # glColor3f(0,1,1)
    glColor3ub(207, 63, 10)
    glBegin(GL_POLYGON)
    # Kiri bawah
    glVertex2f(34,6)
    # Kanan bawah
    glVertex2f(koor_ortoX,6)
    # Kanan atas
    glVertex2f(koor_ortoX, 8)
    # Kiri atas
    glVertex2f(34, 8)
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
    tembok1()
    tembok2()
    tembok3()
    tembok4()
    tembok5()
    bawah = 28
    for x in range(-55, 60, 5):
        circle(x, -bawah)
        if bawah == 28:
            bawah = 26
        else:
            bawah = 28

    # kotak()
    rumput()
    enemy()
    bendera()
    text("nyawa : "+str(nyawa), 46,27,0)   
    if game_over:
        text("Game Over", -6, -1,0)    
    elif finish:
        text("You Win", -6, -1,0)   

    orang() 
    glFlush()

def timer(value): #fungsi timer
    glutTimerFunc(1000//5, timer, 0)  
    # callback function timer dg parameter miliseconds, fungsi yang dipanggil, dan value
    global limit_tanah,pos_x, pos_y,enemy_y, enemy_x, lompat, game_over, tembok, nyawa, kalah, loop, boxx, finish 
    #panggil variabel global kedalam fungsi timer
    if not(game_over) and not(finish):
        # kanan
        if (not( enemy_x + 6 > pos_x > enemy_x - 6) or (pos_y - 6 >= enemy_y)) and not(game_over):
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