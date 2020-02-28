from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    matrix = new_matrix()

    transformationMatrix = new_matrix()
    f = open(fname, "r")
    # print f.read()

    lines = f.readlines()

    # print(lines)

    #to remove the "\n" at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]

    print(lines)

    for i in range(len(lines)):
        if lines[i] == "line":
            coords = lines[i + 1].split(" ")
            for j in range(len(coords)):
                coords[j] = int(coords[j])
            x0 = coords[0]
            y0 = coords[1]
            z0 = coords[2]
            x1 = coords[3]
            y1 = coords[4]
            z1 = coords[5]

            edge = [x0, y0, z0, x1, y1, z1]


        if lines[i] == "ident":
            ident(transformationMatrix)

        if lines[i] == "scale":
            sArgs = lines[i + 1].split(" ")
            for j in range(len(sArgs)):
                sArgs[j] = int(sArgs[j])
            sMatrix = make_scale(sArgs[0], sArgs[1], sArgs[2])
            matrix_mult(sMatrix, transformationMatrix)

        if lines[i] == "translate":
            tArgs = lines[i + 1].split(" ")
            for j in range(len(tArgs)):
                tArgs[j] = int(tArgs[j])
            tMatrix = make_translate(tArgs[0], tArgs[1], tArgs[2])
            matrix_mult(tMatrix, transformationMatrix)

        if lines[i] == "rotate":
            rArgs = lines[i + 1].split(" ")
            axis = rArgs[0]
            theta = int(rArgs[1])
            rMatrix = []

            if axis == "x":
                rMatrix = make_rotX(theta)
            if axis == "y":
                rMatrix = make_rotY(theta)
            if axis == "z":
                rMatrix = make_rotZ(theta)

            matrix_mult(rMatrix, transformationMatrix)

        if lines[i] == "apply":
            matrix_mult(transformationMatrix, matrix)
