#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      preet_000
#
# Created:     16-05-2015
# Copyright:   (c) preet_000 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()




screen.blit(s.image, s.pos)
        if  (TARGET_Y-20)<=(c.y+c.pos.bottom)<=(TARGET_Y+20) or (TARGET_Y-20)<=(c.y+c.pos.top)<=(TARGET_Y+20):
                    if (TARGET_X-20)<=(c.x + c.pos.right)<= (TARGET_X+20) or (TARGET_X-20)<=(c.x + c.pos.left)<=(TARGET_X+20):
                        c.hit_target=1
                        TARGET_Y= random.randint(0,555)
                        TARGET_X= random.randint(91,750)

