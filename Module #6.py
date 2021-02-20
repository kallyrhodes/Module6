class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h
        
def create_rectangle( x, y, w, h):
        return Rectangle(Point(x,y),w,h)

def str_rectangle(r):
        return "({0}, {1}, {2},{3})".format(r.corner.x,r.corner.y, r.width, r.height)
def shift_rectangle(r , dx , dy):
        r.corner = Point(dx,dy)

def offset_rectangle(r1, dx, dy):
        return Rectangle(Point(r1.corner.x+dx,r1.corner.y+dy),r1.width,r1.height)

r1 = create_rectangle(10, 20, 30, 40)
print ("Rectangle r1 in string format is " , str_rectangle(r1))

shift_rectangle(r1, -10, -20)

print("Rectangle r1 in string format after shifting is ", str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print ("Rectangle r1 in string format is" , str_rectangle(r1)) # should be same as previous
print ("Rectangle r2 in string format is" , str_rectangle(r2))
