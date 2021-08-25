# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
   if((left1 > height2 and height1 < left2) or (top1 < width2 and width1 > top2)  ):
       return False
   elif((left1 < height2 and height1 > left2) or (top1 > width2 and width1 < top2) ):
       return True
   return False

# (0,2,1,4,1,6,8,4,True),(0,3,1,4,20,22,6,3,False),
# (5,12,11,14,31,36,8,4, False),(0,0,1,4,1,4,1,2, True)
   