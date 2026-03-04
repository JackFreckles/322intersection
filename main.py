
def get_orientation(p1: list[int, int], p2: list[int, int], p3: list[int, int]) -> str:
    angle = (p2[0] - p1[0])*(p3[1] - p2[1]) - (p2[1] - p1[1])*(p3[0] - p2[0])
    
    if angle == 1:
        return 2
    elif angle == 0:
        return 0
    else:
        return 1
    
def on_segment(p1, p2, p3):
    angle = (p2[0] - p1[0])*(p3[1] - p2[1]) - (p2[1] - p1[1])*(p3[0] - p2[0])

    if (angle == 0):
        return True
    else:
        return False

def do_intersect(segment1, segment2):
    line1 = (segment1[0][1] - segment1[0][0], segment1[1][1] - segment1[1][0])
    line2 = (segment2[0][1] - segment2[0][0], segment2[1][1] - segment2[1][0])
    
if __name__ == "__main__":
    p1 = (2,4)
    p2 = (3,5)
    p3 = (4,6)
    p4 = (4, 8)

    seg1 = (p1, p2)
    seg2 = (p3, p4)
    print(get_orientation(p1, p2, p4))
    print(on_segment(p1, p2, p3))