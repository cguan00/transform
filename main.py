from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# parse_file( 'script', edges, transform, screen, color )

# make_translate(4, 5, 6)
# make_scale(2,3,4)
# make_rotZ(0)
# make_rotY(180)
# make_rotX(180)


parse_file( "script" )
