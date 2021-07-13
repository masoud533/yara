# I had no idea about this code. I got help from the internet
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def Overlap(l1, r1, l2, r2):

    if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
        return False

    if (l1.x >= r2.x or l2.x >= r1.x):
        return False

    if (l1.y >= r2.y or l2.y >= r1.y):
        return False

    return True


if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if (Overlap(l1, r1, l2, r2)):
        print("Rectangles Overlap")
    else:
        print("Rectangles Don't Overlap")
