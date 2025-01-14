import math
import sys
import numpy as np
from PIL import Image
from pathlib import Path

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


theta_x = 0.0
theta_y = 0.0
theta_z = 0.0
pix2angle = 1.0
radius = 10.0
light0_p = [5.0, 0.0, 0.0] #position
light0_d = [0.0, 0.0, -1.0] #direction
light1_p = [-5.0, 0.0, 0.0]
light1_d = [0.0, 0.0, 1.0]
radius_of_lights = [10.0, -10.0]
angle_of_lights = [0.0, 0.0]

light_source_move = 0

left_mouse_button_pressed = 0
right_mouse_button_pressed = 0
mouse_x_pos_old = 0
mouse_y_pos_old = 0
mouse_z_pos_old = 0
delta_x = 0
delta_y = 0
camera_position = [1.0, 0.0, 0.0]
upv = [0.0, 1.0, 0.0]

d = 30
option = 3
whatimage = 1
files = []
folder_path = Path('tekstury')
files = [f for f in folder_path.iterdir() if f.is_file()]

def getfunction(option):
    # call of drawing function    
    if option == 1:
        return eggPoints()
    elif option == 2:
        return eggLine()
    elif option == 3:
        return eggTriangles()
    elif option == 4:
        return utahTeapot()
    
def startup():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    update_viewport(None, 800, 800)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_CULL_FACE)
    glFrontFace(GL_CCW)
    glShadeModel(GL_SMOOTH)
    
    material_ambient = [0.2, 0.2, 0.2, 1.0]
    material_diffuse = [1.0, 1.0, 1.0, 1.0]
    material_specular = [0.3, 0.3, 0.3, 1.0]
    material_shininess = 50
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

    #glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glEnable(GL_TEXTURE_2D)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    
    #Light0
    light_ambient0 = [0.1, 0.1, 0.1, 1.0] # rgb
    light_diffuse0 = [1.0, 0.0, 0.0, 1.0]
    light_specular0 = [0.1, 0.1, 0.1, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular0)

    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 30.0) 
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 1.0)
     
    #Light1
    light_ambient1 = [0.1, 0.1, 0.1, 1.0] # rgb
    light_diffuse1 = [0.0, 0.0, 1.0, 1.0]
    light_specular1 = [0.1, 0.1, 0.1, 1.0]
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)

    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 30.0) 
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 1.0)
    
def shutdown():
    pass

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0) #red x-axis
    glVertex3f(-50.0, 0.0, 0.0)
    glVertex3f(50.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0) #green y-axis
    glVertex3f(0.0, -50.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)

    glColor3f(0.0, 0.0, 1.0) #blue z-axis
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

def eggTriangles():
    global d
    tab = np.zeros((d, d, 3))
    texture = np.zeros((d, d, 2))

    ul = np.linspace(0.0, 0.5, d)
    vl = np.linspace(0.0, 2.0, d)

    ut = np.linspace(0.0, 1.0, d)
    vt = np.linspace(0.0, 1.0, d)

    for j, u in enumerate(ul):
        for i, v in enumerate(vl):
            x = (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * math.cos(3.1415 * v)
            y = (160 * u**4 - 320 * u**3 + 160 * u**2 - 5)
            z = (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * math.sin(3.1415 * v)
            tab[i, j] = [x, y, z]
            texture[j, i] = [ut[i], vt[j]]
            
    def calculate_normal(v1, v2, v3):
        u = np.subtract(v2, v1)
        v = np.subtract(v3, v1)
        normal = np.cross(u, v)
        norm = np.linalg.norm(normal)
        if norm == 0:
            return normal
        return normal / norm
    glEnable(GL_CULL_FACE)
    glFrontFace(GL_CW)
    texture_image = Image.open(files[whatimage])
    glTexImage2D(
        GL_TEXTURE_2D, 0, 3, texture_image.size[0], texture_image.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, texture_image.tobytes("raw", "RGB", 0, -1)
    )
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_TRIANGLES)
    for j in range(1, d):
        for i in range(1, d):
            v1 = tab[i - 1, j - 1]
            v2 = tab[i, j - 1]
            v3 = tab[i, j]
            v4 = tab[i - 1, j]

            normal1 = calculate_normal(v1, v2, v3)
            normal2 = calculate_normal(v1, v3, v4)

           # Pierwszy trójkąt
            glColor3f(1.0, 1.0, 1.0)  # white
            glNormal3f(*normal1)
            glTexCoord2f(*texture[i - 1, j - 1])  # Współrzędne tekstury dla v1
            glVertex3f(*v1)
            glTexCoord2f(*texture[i, j - 1])  # Współrzędne tekstury dla v2
            glVertex3f(*v2)
            glTexCoord2f(*texture[i, j])  # Współrzędne tekstury dla v3
            glVertex3f(*v3)

            # Drugi trójkąt
            glColor3f(1.0, 1.0, 1.0)  # white
            glNormal3f(*normal2)
            glTexCoord2f(*texture[i - 1, j - 1])  # Współrzędne tekstury dla v1
            glVertex3f(*v1)
            glTexCoord2f(*texture[i, j])  # Współrzędne tekstury dla v3
            glVertex3f(*v3)
            glTexCoord2f(*texture[i - 1, j])  # Współrzędne tekstury dla v4
            glVertex3f(*v4)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
def utahTeapot():
    global obj_model
    glDisable(GL_CULL_FACE)
    glFrontFace(GL_CCW)
    if obj_model:
        texture_image = Image.open(files[whatimage])
        glTexImage2D(
        GL_TEXTURE_2D, 0, 3, texture_image.size[0], texture_image.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, texture_image.tobytes("raw", "RGB", 0, -1)
        )
        glEnable(GL_TEXTURE_2D)
        glBegin(GL_TRIANGLES)
        for face in obj_model['faces']:
            for vertex_data in face:
                vertex_id, texture_id, normal_id = (int(idx)- 1 if idx else -1 for idx in vertex_data.split('/'))
                if texture_id >= 0:
                    glTexCoord2fv(obj_model['textures'][texture_id])
                if normal_id >= 0:
                    glNormal3fv(obj_model['normals'][normal_id])
                glColor3f(1.0, 1.0, 1.0)
                glVertex3fv(obj_model['vertices'][vertex_id])
        glEnd()
        glDisable(GL_TEXTURE_2D)

def load_shape_from_obj(file_path):
    try:
        vertices = []
        faces = []
        textures = []
        normals = []
        with open(file_path) as f:
            for line in f:
                if line.startswith('v '):
                    vertex = list(map(float, line[2:].strip().split()))
                    vertices.append(vertex)
                elif line.startswith('vt '):
                    texture = list(map(float, line[3:].strip().split()))
                    textures.append(texture[:2])
                elif line.startswith('vn '):
                    normal = list(map(float, line[3:].strip().split()))
                    normals.append(normal)
                elif line.startswith('f '):
                    face = [entry for entry in line[2:].strip().split()]
                    faces.append(face)


        shape_data = {
            "vertices": np.array(vertices, dtype=np.float32),
            "textures": np.array(textures, dtype=np.float32),
            "normals": np.array(normals, dtype=np.float32),
            "faces": faces
        }
        return shape_data

    except FileNotFoundError:
        print(f"{file_path} not found.")
    except:
        print("An error occurred while loading the shape.")

angle_x = 0.0
angle_y = 0.0
angle_z = 0.0
def spin():
    glRotatef(angle_x, 1.0, 0.0, 0.0)  # Obrót w osi X
    glRotatef(angle_y, 0.0, 1.0, 0.0)  # Obrót w osi Y
    glRotatef(angle_z, 0.0, 0.0, 1.0)  # Obrót w osi Z

def keyboard_key_callback(window, key, scancode, action, mods):
    global angle_x, angle_y, angle_z, option, d, light0_p, light1_p, light_source_move
    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_A:  # Strzałka w lewo - obrót w osi Y
            angle_y -= 10.0
        elif key == GLFW_KEY_D:  # Strzałka w prawo - obrót w osi Y
            angle_y += 10.0
        elif key == GLFW_KEY_W:  # Strzałka w górę - obrót w osi X
            angle_x += 10.0
        elif key == GLFW_KEY_S:  # Strzałka w dół - obrót w osi X
            angle_x -= 10.0
        elif key == GLFW_KEY_Q:  # Klawisz "Q" - obrót w osi Z
            angle_z += 10.0
        elif key == GLFW_KEY_E:  # Klawisz "E" - obrót w osi Z
            angle_z -= 10.0
        elif key == GLFW_KEY_BACKSLASH: #Klawisz "\" - zmiana textury
            global whatimage, files
            if whatimage < len(files) - 1:
                whatimage += 1
            else:
                whatimage = 0
        elif key == GLFW_KEY_Z: # Klawisz "Z" - włączenie/wyłączenie światła
            print("Zmiana Światła")
            if glIsEnabled(GL_LIGHTING):
                glDisable(GL_LIGHTING)
            else:
                glEnable(GL_LIGHTING)
        elif key == GLFW_KEY_SPACE:  # spacja - zmiana obiektu
            print("Zmiana obiektu")
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
        elif key == GLFW_KEY_1:
            if glIsEnabled(GL_LIGHT0):
                glDisable(GL_LIGHT0)
            else:
                glEnable(GL_LIGHT0)
        elif key == GLFW_KEY_2:
            if glIsEnabled(GL_LIGHT1):
                glDisable(GL_LIGHT1)
            else:
                glEnable(GL_LIGHT1)
        elif key == GLFW_KEY_0:
            if glIsEnabled(GL_LIGHT1):
                glDisable(GL_LIGHT1)
                glDisable(GL_LIGHT0)
            else:
                glEnable(GL_LIGHT1)
                glEnable(GL_LIGHT0)
        elif key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
            glfwSetWindowShouldClose(window, GLFW_TRUE)
        elif key == GLFW_KEY_X: # Klawisz "X" - przesunięcie światła
            print("Zmiana światła na : ")
            if light_source_move < 2:
                light_source_move += 1
            else:
                light_source_move = 0
            if(light_source_move == 0):
                print("oba światła")
            elif(light_source_move == 1):
                print("światło czerwone")
            elif(light_source_move == 2):
                print("światło niebieskie")
        elif light_source_move == 0: # Klawisz "X" - przesunięcie światła
            if key == GLFW_KEY_J:  # J - przesunięcie świateł w lewo po okręgu
                angle_of_lights[0] += 0.1
                angle_of_lights[1] += 0.1
            elif key == GLFW_KEY_L:  # L - przesunięcie świateł w prawo po okręgu
                angle_of_lights[0] -= 0.1
                angle_of_lights[1] -= 0.1
            elif key == GLFW_KEY_I:  # I - przesunięcie świateł w górę
                light0_p[1] -= 1.0
                light1_p[1] -= 1.0
            elif key == GLFW_KEY_K:  # K - przesunięcie świateł w dół
                light0_p[1] += 1.0
                light1_p[1] += 1.0
            elif key == GLFW_KEY_U:  # U - przesunięcie świateł do przodu
                radius_of_lights[0] += 1.0
                radius_of_lights[1] += 1.0
            elif key == GLFW_KEY_O:  # O - przesunięcie świateł do tyłu
                radius_of_lights[0] -= 1.0
                radius_of_lights[1] -= 1.0
        elif light_source_move == 1: # światło czerwone
            if key == GLFW_KEY_J:  # J - przesunięcie światła czerwonego w lewo
                angle_of_lights[0] += 0.1
            elif key == GLFW_KEY_L:  # L - przesunięcie światła czerwonego w prawo
                angle_of_lights[0] -= 0.1
            elif key == GLFW_KEY_I:  # I - przesunięcie światła czerwonego w górę
                light0_p[1] -= 1.0
            elif key == GLFW_KEY_K:  # K - przesunięcie światła czerwonego w dół
                light0_p[1] += 1.0
            elif key == GLFW_KEY_U:  # U - przesunięcie światła czerwonego do przodu
                radius_of_lights[0] += 1.0
            elif key == GLFW_KEY_O:  # O - przesunięcie światła czerwonego do tyłu
                radius_of_lights[0] -= 1.0
        elif light_source_move == 2: # światło niebieskie
            if key == GLFW_KEY_J:  # J - przesunięcie światła niebieskiego w lewo
                angle_of_lights[1] += 0.1
            elif key == GLFW_KEY_L:  # L - przesunięcie światła niebieskiego w prawo
                angle_of_lights[1] -= 0.1
            elif key == GLFW_KEY_I:  # I - przesunięcie światła niebieskiego w górę
                light1_p[1] -= 1.0
            elif key == GLFW_KEY_K:  # K - przesunięcie światła niebieskiego w dół
                light1_p[1] += 1.0
            elif key == GLFW_KEY_O:  # O - przesunięcie światła niebieskiego do przodus
                radius_of_lights[1] += 1.0
            elif key == GLFW_KEY_U:  # U - przesunięcie światła niebieskiego do tyłu
                radius_of_lights[1] -= 1.0

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

def signum(x):
    if x < 0.0:
        return 1.0
    elif x > 0.0:
        return -1.0
    else:
        return 0.0
        
def update_coordinates(radius, angle):
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    return x, y

def render(time):
    global theta_x
    global theta_y
    global theta_z
    global radius
    global option
    global camera_position
    global upv
    global light0_p
    global light0_d
    global light1_p
    global light1_d
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
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

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    #red light
    light0_p[0], light0_p[2] = update_coordinates(radius_of_lights[0], angle_of_lights[0])
    light_position0 = [light0_p[0], light0_p[1], light0_p[2], 1.0]
    light0_d[0] = signum(light_position0[0])
    light0_d[1] = signum(light_position0[1])
    light0_d[2] = signum(light_position0[2])
    light_direction0 = [light0_d[0], light0_d[1], light0_d[2]]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position0)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, light_direction0)

    #blue light
    light1_p[0], light1_p[2] = update_coordinates(radius_of_lights[1], angle_of_lights[1])
    light_position1 = [light1_p[0], light1_p[1], light1_p[2], 1.0]
    light1_d[0] = signum(light_position1[0])
    light1_d[1] = signum(light_position1[1])
    light1_d[2] = signum(light_position1[2])
    light_direction1 = [light1_d[0], light1_d[1], light1_d[2]]
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, light_direction1)
    glPopMatrix()

    glLoadIdentity()
    gluLookAt(camera_position[0] * radius,camera_position[1] * radius,camera_position[2] * radius, 0.0, 0.0, 0.0, upv[0], upv[1], upv[2])
    
    axes()
     
    spin()
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
    glLoadIdentity()
    
    gluPerspective(90, 1.0, 0.1, 100.0)
    glViewport(0, 0, width, height)

    if width <= height:
        glOrtho(-10, 10, -10 / aspectRatio, 10 / aspectRatio, 10, -10)
    else:
        glOrtho(-10 * aspectRatio, 10 * aspectRatio, -10, 10, 10, -10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    global option
    global d
    global obj_model
    obj_model = load_shape_from_obj("teapot.obj")

    if obj_model is None:
        print("Nie udało się załadować modelu.")
        return
    
    if(d == 0):
        d = int(input("Podaj N: "))
        
    print("Zmiana obiektu przy pomocy Spacji")
    print(" ")
    print("Zmiana N przy pomocy klawiszy \"[\" i \"]\" ")
    print(" ")
    print("Poruszanie obiektem przy pomocy WSADQE")
    print("Poruszanie kamerą przy pomocy myszki oraz kółka myszki")
    print("Przełącznik światła klawisz Z")
    print("Przęłączanie kontorlowanego światła przy pomocy X")
    print("Przesunięcie światła przy pomocy klawiszy ILKI")
    print("Zmiana odległości śwaitła względem obiektu UO")
    print("Przełączanie śwaitła czerwonego pod 1")
    print("Przełączanie śwaitła niebieskiego pod 2")
    print("Przełączanie obu świateł pod 0")
    print(" ")
    print("Zmiana tekstury przy pomocy klawisza \"\\\"")
        
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
