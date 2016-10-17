"""
Imagine we have an image where every pixel is white or black.
We’ll represent this image as a simple 2D array (0 = black, 1 = white).
The image you get is known to have a single black rectangle on a white 
background. 

Write a function that takes in the image and 
returns the coordinates of the rectangle 
-- either top-left and bottom-right; or top-left, width, and height.
"""

image = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
]


def get_coordinates_x_y(image, x, y, N, M):
    height = 0
    width = 0
    found_width = False
    for i in range(x, N):
        line = image[i]
        height += 1
        if not found_width:
            for j in range(y, M):
                if line[j] == '0':
                    found_width = True
                    width +=1
                else:
                    break
    print height, width, x, y

def get_coordinates_2(image):
    height = 0
    width = 0
    top_left = [0, 0]
    found_width = False
    cur_line = -1
    N = len(image)
    for line in image:
        M = len(line)
        cur_line += 1
        if 0 in line:
            for j in range(0, M):
                if line[j] == 0 and \
                    (cur_line == 0 and j == 0) or \
                    (image[cur_line-1][j] == 1 and 
                     image[cur_line-1][j-1] == 1 and
                     image[cur_line][j-1] == 1):
                    get_coordinates_x_y(image, cur_line, j, N, M)               
    
                    
def get_coordinates(image):
    height = 0
    width = 0
    top_left = [0, 0]
    found_width = False
    cur_line = 0
    for line in image:
        if 0 in line:
            height += 1
            if not found_width:
                found_width = True
                #width = line.count(0)
                for j in range(0, len(line)):
                    if line[j] == 0:
                        top_left[0] = cur_line
                        top_left[1] = j
                        curr_left = j
                    else:
                        curr_right = j-1
                               
        if not 0 in line and found_width:
            break
        cur_line += 1
    print height, width, top_left
    
get_coordinates_2(image)