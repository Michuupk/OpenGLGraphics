import math
import sys
import numpy as np

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


theta_x = 0.0
theta_y = 0.0
theta_z = 0.0
pix2angle = 1.0
radius = 0 

left_mouse_button_pressed = 0
right_mouse_button_pressed = 0
mouse_x_pos_old = 0
mouse_y_pos_old = 0
mouse_z_pos_old = 0
delta_x = 0
delta_y = 0
camera_position = [1.0, 0.0, 0.0]
upv = [0.0, 1.0, 0.0]

d = 20
option = 3

def getfunction(option):
    # call of drawing function    
    if option == 1:
        return eggPoints()
    elif option == 2:
        return eggLine()
    elif option == 3:
        return eggTriangleStrip()
    elif option == 4:
        return utahTeapot()
    
def startup():
    glClearColor(0.0, 0.0, 0.1, 1.0)
    update_viewport(None, 800, 800)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    #glFrontFace(GL_CCW)
    #glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glShadeModel(GL_SMOOTH)
    
    material_ambient = [0.5, 0.5, 0.5, 1.0]
    material_diffuse = [1.0, 1.0, 1.0, 1.0]
    material_specular = [0.3, 0.3, 0.3, 1.0]
    material_shininess = 50
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

    glEnable(GL_LIGHTING)
    #Light0
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    
    #Light0
    light_ambient0 = [0.1, 0.1, 0.1, 1.0] # rgb
    light_diffuse0 = [1.0, 0.0, 0.0, 1.0]
    light_specular0 = [0.1, 0.1, 0.1, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular0)

    # light_position0 = [5.0, 0.0, 0.0, 1.0]
    # light_direction0 = [-1.0, 0.0, 0.0]
    # glLightfv(GL_LIGHT0, GL_POSITION, light_position0)
    # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, light_direction0)

    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 90.0) 
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 1.0)
     
    #Light1
    light_ambient1 = [0.1, 0.1, 0.1, 1.0] # rgb
    light_diffuse1 = [0.0, 0.0, 1.0, 1.0]
    light_specular1 = [0.1, 0.1, 0.1, 1.0]
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    
    # light_position1 = [-5.0, 0.0, 0.0, 1.0]
    # light_direction1 = [1.0, 0.0, 0.0]
    # glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    # glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, light_direction1)

    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 90.0) 
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 1.0)
    


def shutdown():
    pass

def squares():
    glBegin(GL_QUADS)
    
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(5.0, -5.0, -5.0)
    glVertex3f(5.0, -5.0, 5.0)
    
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glVertex3f(-5.0, -5.0, 5.0)
    
    glEnd()
    

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-50.0, 0.0, 0.0)
    glVertex3f(50.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -50.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -50.0)
    glVertex3f(0.0, 0.0, 50.0)

    glEnd()

def eggPoints():
    global d
    glBegin(GL_POINTS)

    glColor3f(1.0, 1.0, 1.0)
    u = 0
    v = 0
    for j in range (d):
        v = j / d
        for i in range (d):
            u = i / d
            x = ((-90 * math.pow(u,5) + 225 * math.pow(u,4) - 270 * math.pow(u,3) + 180 * math.pow(u,2) - 45 * u) * math.cos(3.1415*v))
            y = (160 * math.pow(u,4) - 320 * math.pow(u,3) + 160 * math.pow(u,2) - 5)
            z = ((-90 * math.pow(u,5) + 225 * math.pow(u,4) - 270 * math.pow(u,3) + 180 * math.pow(u,2) - 45 * u) * math.sin(3.1415*v))
            glVertex3f(x, y, z)
        u = 0

    glEnd()

def eggLine():
    global d
    glBegin(GL_LINE_LOOP)

    glColor3f(1.0, 1.0, 1.0)
    u = 0
    v = 0
    for j in range (d):
        v = j / d
        for i in range (d):
            u = i / d
            x = ((-90 * math.pow(u,5) + 225 * math.pow(u,4) - 270 * math.pow(u,3) + 180 * math.pow(u,2) - 45 * u) * math.cos(3.1415*v))
            y = (160 * math.pow(u,4) - 320 * math.pow(u,3) + 160 * math.pow(u,2) - 5)
            z = ((-90 * math.pow(u,5) + 225 * math.pow(u,4) - 270 * math.pow(u,3) + 180 * math.pow(u,2) - 45 * u) * math.sin(3.1415*v))
            glVertex3f(x, y, z)
        u = 0
    glEnd()

def eggTriangleStrip():
    global d
    tab = np.zeros((d, d, 3))

    ul = np.linspace(0.0, 0.5, d)
    vl = np.linspace(0.0, 2.0, d)
    for j, u in enumerate(ul):
        for i, v in enumerate(vl):
            x = (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * math.cos(3.1415 * v)
            y = (160 * u**4 - 320 * u**3 + 160 * u**2 - 5)
            z = (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * math.sin(3.1415 * v)
            tab[i, j] = [x, y, z]
            
    glBegin(GL_TRIANGLES)
    for j in range(d):
        for i in range(d):
            
            pos1 = tab[i - 1, j]
            pos2 = tab[i, j - 1]
            pos3 = tab[i, j]
            pos4 = tab[i - 1, j - 1]
            
            glColor3f(1.0, 0.0, 0.0) #r
            glVertex3f(*tab[i - 1, j])  #1
            glColor3f(0.0, 1.0, 0.0) #g
            glVertex3f(*tab[i, j - 1]) #2
            glColor3f(0.0, 0.0, 1.0) #b
            glVertex3f(*tab[i, j]) #3
            
            glColor3f(1.0, 0.0, 1.0) 
            glVertex3f(*tab[i - 1, j]) #1
            glColor3f(1.0, 1.0, 0.0)
            glVertex3f(*tab[i - 1, j - 1]) #4
            glColor3f(0.0, 1.0, 1.0)
            glVertex3f(*tab[i, j - 1]) #2
            
    glEnd()

def readTeapot():

    file1 = open("teapot.obj","r")
    xs = []
    ys = []
    zs = []
    
    while file1.read(1) == "v":
        text = file1.readline().split()
        x = text[0]
        y = text[1] 
        z = text[2]
        xs.append(x)
        ys.append(y)
        zs.append(z)
    file1.close()
    
    return xs, ys, zs

def utahTeapot():
    
    xs = list()
    ys = list()
    zs = list()
    
    xs, ys, zs = readTeapot()

    glBegin(GL_POINTS)
    
    glColor3f(0.0, 1.0, 0.0)
    
    i = 0
    for i in range(len(xs)):
        x = float(xs[i])
        y = float(ys[i])
        z = float(zs[i])
        glVertex3f(x, y, z)
        
    glEnd();    

angle_x = 0.0
angle_y = 0.0
angle_z = 0.0
def spin():
    glEnable(GL_NORMALIZE)
    glRotatef(angle_x, 1.0, 0.0, 0.0)  # Obrót w osi X
    glRotatef(angle_y, 0.0, 1.0, 0.0)  # Obrót w osi Y
    glRotatef(angle_z, 0.0, 0.0, 1.0)  # Obrót w osi Z

def keyboard_key_callback(window, key, scancode, action, mods):
    global angle_x, angle_y, angle_z, option, d
    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_LEFT:  # Strzałka w lewo - obrót w osi Y
            angle_y -= 10.0
        elif key == GLFW_KEY_RIGHT:  # Strzałka w prawo - obrót w osi Y
            angle_y += 10.0
        elif key == GLFW_KEY_UP:  # Strzałka w górę - obrót w osi X
            angle_x += 10.0
        elif key == GLFW_KEY_DOWN:  # Strzałka w dół - obrót w osi X
            angle_x -= 10.0
        elif key == GLFW_KEY_Z:  # Klawisz "Z" - obrót w osi Z
            angle_z += 10.0
        elif key == GLFW_KEY_X:  # Klawisz "X" - obrót w osi Z
            angle_z -= 10.0
        elif key == GLFW_KEY_L: # Klawisz "L" - włączenie/wyłączenie światła
            if glIsEnabled(GL_LIGHTING):
                glDisable(GL_LIGHTING)
            else:
                glEnable(GL_LIGHTING)  
        elif key == GLFW_KEY_SPACE:  # spacja - zmiana obiektu
            if (option < 4):
                option += 1
            else:
                option = 1
        elif key == GLFW_KEY_RIGHT_BRACKET:
            d += 1
            print(d)
        elif key == GLFW_KEY_LEFT_BRACKET:
            if(d == 0):
                d = 0
            else:
                d -= 1
                print(d)
        elif key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
            glfwSetWindowShouldClose(window, GLFW_TRUE)

def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old
    global delta_y
    global mouse_y_pos_old
    if left_mouse_button_pressed == 1:
        delta_x += (x_pos - mouse_x_pos_old) * 0.005
        mouse_x_pos_old = x_pos

        delta_y += (y_pos - mouse_y_pos_old) * 0.005
        mouse_y_pos_old = y_pos

def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed
    global right_mouse_button_pressed
    global mouse_x_pos_old, mouse_y_pos_old

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
        mouse_x_pos_old, mouse_y_pos_old = glfwGetCursorPos(window)
    else:
        left_mouse_button_pressed = 0
                       
    if button == GLFW_MOUSE_BUTTON_RIGHT and action == GLFW_PRESS:
        right_mouse_button_pressed = 1
    else:
        right_mouse_button_pressed = 0

def scroll_callback(window, xoffset, yoffset):
    global radius
    if -45 <= radius <= 45:
        radius -= yoffset
    if radius < -45:
        radius = -45
    if radius > 45:
        radius = 45
        

def render(time):
    global theta_x
    global theta_y
    global theta_z
    global radius
    global option
    global camera_position
    global upv
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    if left_mouse_button_pressed:
        camera_position[0] = math.cos(delta_y) * math.cos(delta_x)
        camera_position[1] = math.sin(delta_y)
        camera_position[2] = math.cos(delta_y) * math.sin(delta_x)

        upv[0] = -math.cos(delta_x) * math.sin(delta_y)
        upv[1] = math.cos(delta_y)
        upv[2] = -math.sin(delta_x) * math.sin(delta_y)

        up_length = math.sqrt(upv[0]**2 + upv[1]**2 + upv[2]**2)
        upv[0] /= up_length/2
        upv[1] /= up_length/2
        upv[2] /= up_length/2
        
    else:
        radius = radius
        upv[0] = upv[0]
        upv[1] = upv[1]
        upv[2] = upv[2]
        camera_position[0] = camera_position[0]
        camera_position[1] = camera_position[1]
        camera_position[2] = camera_position[2]

    gluLookAt(camera_position[0] * radius,camera_position[1] * radius,camera_position[2] * radius, 0.0, 0.0, 0.0, upv[0], upv[1], upv[2])
    
    glPushMatrix()
    glLoadIdentity()
    
    #red light
    light_position0 = [7.0, 0.0, 0.0, 1.0]
    light_direction0 = [-1.0, 0.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position0)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, light_direction0)

    #blue light
    light_position1 = [-7.0, 0.0, 0.0, 1.0]
    light_direction1 = [1.0, 0.0, 0.0]
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, light_direction1)
    
    
    glPopMatrix()

    axes()
    
    spin()
    #squares()
    getfunction(option)

    glFlush()

def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width
    
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height
    
    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    gluPerspective(90, 1.0, 0.1, 100.0)

    if width <= height:
        glOrtho(-10, 10, -10 / aspectRatio, 10 / aspectRatio, 10, -10)
    else:
        glOrtho(-10 * aspectRatio, 10 * aspectRatio, -10, 10, 10, -10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    global option
    global d
    
    if(d == 0):
        d = int(input("Podaj N: "))
        
    print("Zmiana obiektu przy pomocy spacji")
    print(" ")
    print("Zmiana N przy pomocy klawiszy \"[\" i \"]\" ")
    print(" ")
    print("Poruszanie obiektem przy pomocy strzałek oraz klawiszy \"Z\" i \"X\"")
    print("Poruszanie kamerą przy pomocy myszki oraz kółka myszki")
        
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(800, 800, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
    glfwSetScrollCallback(window, scroll_callback)

    glfwSwapInterval(1)
    

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()

if __name__ == '__main__':
    main()
