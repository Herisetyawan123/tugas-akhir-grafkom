#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
w,h= 500,500




#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 400, 0.0, 400, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()

    glutSwapBuffers() #utk membersihkan layar, double buffering


def main():
    glutInit() #inisialisasi glut
    glutInitDisplayMode(GLUT_RGBA) #utk mengatur display supaya berwarna
    glutInitWindowSize(500, 500) #utk mengatur ukuran window
    glutInitWindowPosition(0, 0) #utk mengatur letak window
    #utk transparansi (tapi belum bisa)
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #glEnable(GL_BLEND)
    wind = glutCreateWindow("Point and Lines") #utk memberi nama pada window
    glutDisplayFunc(showScreen) #utk fungsi callback
    glutIdleFunc(showScreen) #utk fungsi callback
    glutMainLoop() #fungsi yang akan memulai keseluruhan program
