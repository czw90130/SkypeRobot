#! /usr/bin/env python
import roslib
roslib.load_manifest('SkypeRobot')
import sys
import rospy
import cv
import math
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from SkypeRobot.msg import Angles
from SkypeRobot.msg import Hands
from SkypeRobot.msg import Whells

class gui_generator:
    def __init__(self, imgdir):
        
        self.menu_bar = cv.LoadImage(imgdir+'menu_bar.jpg')
        self.menu_bar_msk = cv.LoadImage(imgdir+'menu_bar_msk.png', 0)

        self.move_bk = cv.LoadImage(imgdir+'move_bk.jpg')
        self.g_cube = cv.LoadImage(imgdir+'greenCube.jpg')
        self.r_cube = cv.LoadImage(imgdir+'redCube.jpg')
        
        self.whellslide_bk = cv.LoadImage(imgdir+'whellslide_bk.jpg')
        self.whellslide_in = cv.LoadImage(imgdir+'whellslide_in.jpg')

        self.hp_r = cv.LoadImage(imgdir+'HandPointer.png')
        self.hp_r_msk = cv.LoadImage(imgdir+'HandPointer.png', 0)
        self.hp_r_bk = cv.LoadImage(imgdir+'HandPointer_outer_R0.jpg')
        self.hp_hd_r = cv.LoadImage(imgdir+'HandPointerHold.png')
        self.hp_hd_r_msk = cv.LoadImage(imgdir+'HandPointerHold.png', 0)
        self.hp_hd_r_bk = cv.LoadImage(imgdir+'HandPointerHold_outer.jpg')
        self.hp_l = cv.LoadImage(imgdir+'HandPointer_L.png')
        self.hp_l_msk = cv.LoadImage(imgdir+'HandPointer_L.png', 0)
        self.hp_l_bk = cv.LoadImage(imgdir+'HandPointer_outer_R0_L.jpg')
        self.hp_hd_l = cv.LoadImage(imgdir+'HandPointerHold_L.png')
        self.hp_hd_l_msk = cv.LoadImage(imgdir+'HandPointerHold_L.png', 0)
        self.hp_hd_l_bk = cv.LoadImage(imgdir+'HandPointerHold_outer_L.jpg')
        
        self.rhand_x = 0
        self.rhand_y = 0
        self.rhand_st = 0
        self.lhand_x = 0
        self.lhand_y = 0
        self.lhand_st = 0

        self.prelhst = 0
        self.prerhst = 0
        self.imgdir = imgdir

        self.hands_sub = rospy.Subscriber("robotHands", Hands, self.callback_hands)
        self.hands_sub = rospy.Subscriber("robotAngles", Angles, self.callback_angles)

    def setMenu(self, bk_img, showpr):
        pt = 120 - showpr*120/100
               
        temp = cv.GetImage(bk_img)
        cv.SetImageROI(temp,(0, 0, temp.width-pt, temp.height))    

        cv.SetImageROI(self.menu_bar,(pt, 0, self.menu_bar.width, self.menu_bar.height)) 
        cv.SetImageROI(self.menu_bar_msk,(pt, 0, self.menu_bar.width, self.menu_bar.height)) 
        cv.Copy(self.menu_bar, temp, self.menu_bar_msk)
        cv.ResetImageROI(self.menu_bar)
        cv.ResetImageROI(self.menu_bar_msk)

        cv.SetImageROI(self.menu_bk,(pt, 0, self.menu_bk.width, self.menu_bk.height))
        cv.AddWeighted(temp, 1.0, self.menu_bk,  0.5, 0,temp)
        cv.ResetImageROI(self.menu_bk)

        cv.ResetImageROI(temp)
        cv.Copy(cv.GetMat(temp),bk_img)

    def setButton(self, bk_img, x, y, arm, move):

        temp = cv.GetImage(bk_img)
        m = move*80/100
        a = arm*85/100

        if y<470 and y>320 and x<160 and x>15 : 
            rel = 1
        else:
            rel = 0.1

        cv.AddWeighted(temp, 1.0, self.move_bk, rel, 0,temp)

        cv.SetImageROI(temp,(24+m, 370, 51, 47))
        if move < 50:
            cv.AddWeighted(temp, 1.0, self.r_cube, rel, 0,temp)
        else:
            cv.AddWeighted(temp, 1.0, self.g_cube, rel, 0,temp)
        cv.ResetImageROI(temp)

        cv.SetImageROI(temp,(65, 329+a, 51, 47))
        if arm < 50:
            cv.AddWeighted(temp, 1.0, self.r_cube, rel, 0,temp)
        else:
            cv.AddWeighted(temp, 1.0, self.g_cube, rel, 0,temp)
        cv.ResetImageROI(temp)

        cv.Copy(cv.GetMat(temp),bk_img)

    def setMoveBk(self, bk_img, lbase_x, lbase_y, rbase_x, rbase_y, ly, ry):

        lbase_x = lbase_x - 30
        lbase_y = lbase_y - 50
        rbase_x = rbase_x - 30
        rbase_y = rbase_y - 50
        
        if lbase_x>560 or rbase_x>560 or lbase_y>300 or rbase_y>300 or lbase_y<60 or rbase_y<60:
            return 0
        temp = cv.GetImage(bk_img)
        #cv.AddWeighted(temp, 1.0, self.move_bk,  0.5, 0,temp)
        cv.SetImageROI(temp,(rbase_x, rbase_y, 80, 120))
        cv.AddWeighted(temp, 1.0, self.whellslide_bk, 1, 0,temp)
        cv.ResetImageROI(temp)
        cv.SetImageROI(temp,(rbase_x, rbase_y+ry, 80, 120))
        cv.AddWeighted(temp, 1.0, self.whellslide_in, 1, 0,temp)
        cv.ResetImageROI(temp)

        cv.SetImageROI(temp,(lbase_x, lbase_y, 80, 120))
        cv.AddWeighted(temp, 1.0, self.whellslide_bk, 1, 0,temp)
        cv.ResetImageROI(temp)
        cv.SetImageROI(temp,(lbase_x, lbase_y+ly, 80, 120))
        cv.AddWeighted(temp, 1.0, self.whellslide_in, 1, 0,temp)
        cv.ResetImageROI(temp)
        

        cv.Copy(cv.GetMat(temp),bk_img)
        return 1


    def setHandPointer(self, bk_img):
        temp_bk = cv.GetImage(bk_img)
        
        temp = cv.CreateImage((752,600), 8, 3)
        cv.SetImageROI(temp,(56, 60, temp_bk.width, temp_bk.height))
        cv.Copy(temp_bk, temp)
        cv.ResetImageROI(temp)

        
        cv.SetImageROI(temp,(self.rhand_x*696/640, self.rhand_y*540/480, 56, 60))
        if 100 > self.rhand_st:
            if self.prerhst != self.rhand_st:
                ct = self.rhand_st - 2
                if ct < 0:
                    ct = 0
                elif ct > 3:
                    ct = 3

                self.hp_r_bk = cv.LoadImage(self.imgdir+'HandPointer_outer_R'+str(ct)+'.jpg')
                self.prerhst = self.rhand_st
            
            cv.Copy(self.hp_r, temp, self.hp_r_msk)
            cv.AddWeighted(temp, 1.0, self.hp_r_bk, 1, 0,temp)
        else:
            cv.Copy(self.hp_hd_r, temp, self.hp_hd_r_msk)
            cv.AddWeighted(temp, 1.0, self.hp_hd_r_bk, 1, 0,temp)
        cv.ResetImageROI(temp)

        cv.SetImageROI(temp,(self.lhand_x*696/640, self.lhand_y*540/480, 56, 60))
        if 100 > self.lhand_st:
            if self.prelhst != self.lhand_st:
                ct = self.lhand_st - 2
                if ct < 0:
                    ct = 0
                elif ct > 3:
                    ct = 3

                self.hp_l_bk = cv.LoadImage(self.imgdir+'HandPointer_outer_R'+str(ct)+'_L.jpg')
                self.prelhst = self.lhand_st

            cv.Copy(self.hp_l, temp, self.hp_l_msk)
            cv.AddWeighted(temp, 1.0, self.hp_l_bk, 1, 0,temp)            
        else:
            cv.Copy(self.hp_hd_l, temp, self.hp_hd_l_msk)
            cv.AddWeighted(temp, 1.0, self.hp_hd_l_bk, 1, 0,temp)
        cv.ResetImageROI(temp)
        #cv.ShowImage("Image window", temp)
        cv.SetImageROI(temp,(56, 60, temp_bk.width, temp_bk.height))
        cv.Copy(temp, bk_img)
    

    def callback_hands(self, data):
        self.lhand_st = data.HandLeft
        self.rhand_st = data.HandRight

    def callback_angles(self, data):
        bias = math.fabs(data.HandXLeft-320)*22/320 +  math.fabs(data.HandYLeft-240)*22/240
        if 100 < self.lhand_st:
            self.lhand_x = data.HandXLeft
            self.lhand_y = data.HandYLeft 
        elif 0 == data.HandXLeft or 640 == data.HandXLeft  or 0 == data.HandYLeft  or 480 == data.HandYLeft:
            self.lhand_st = 0
            self.lhand_x = data.HandXLeft
            self.lhand_y = data.HandYLeft 
        
        elif data.ShoulderElbowWristLeft < 90 - bias:
            if self.lhand_st <15:
                self.lhand_st = self.lhand_st + 1
            
            #if(2 > self.lhand_st):
            self.lhand_x = data.HandXLeft
            self.lhand_y = data.HandYLeft 
    
        elif data.ShoulderElbowWristLeft > 90 - bias:
            self.lhand_st = self.lhand_st - 5
            if self.lhand_st < 0:
               self.lhand_st = 0

            #if(2 > self.lhand_st):
            self.lhand_x = data.HandXLeft
            self.lhand_y = data.HandYLeft 
 

        bias = math.fabs(data.HandXRight-320)*22/320 +  math.fabs(data.HandYRight-240)*22/240
        if 100 < self.rhand_st:
            self.rhand_x = data.HandXRight
            self.rhand_y = data.HandYRight
        elif 0 == data.HandXRight or 640 == data.HandXRight  or 0 == data.HandYRight  or 480 == data.HandYRight:
            self.rhand_st = 0
            self.rhand_x = data.HandXRight
            self.rhand_y = data.HandYRight
        
        elif data.ShoulderElbowWristRight < 90 - bias:
            if self.rhand_st <15:
                self.rhand_st = self.rhand_st + 1
            
            if(2 > self.rhand_st):
                self.rhand_x = data.HandXRight
                self.rhand_y = data.HandYRight 
    
        elif data.ShoulderElbowWristRight > 90 - bias:
            self.rhand_st = self.rhand_st - 5
            if self.rhand_st < 0:
               self.rhand_st = 0

            if(2 > self.rhand_st):
                self.rhand_x = data.HandXRight
                self.rhand_y = data.HandYRight

            
            
        
        
        

class image_converter:
    def __init__(self, gui):
        self.image_pub = rospy.Publisher("vcamera",Image)
        
        cv.NamedWindow("Image window", 1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("image", Image, self.callback)
        self.bk_image = cv.CreateMat(480,640,cv.CV_8UC3)        
        self.gui = gui

        self.whell_pub = rospy.Publisher('robotWhells', Whells)

        self.move_state = 0
        self.arm_state = 0

        self.pre_whell = Whells()
        self.lwhellbase_x = 0
        self.lwhellbase_y = 0
        self.rwhellbase_x = 0
        self.rwhellbase_y = 0
        self.pre_whell.RightWhell = 0
        self.pre_whell.LeftWhell = 0

    def setButtons(self):
        
        x = self.gui.lhand_x - 30
        y = self.gui.lhand_y - 30

        if 1 == self.move_state & 1 and self.gui.lhand_st > 200 and self.gui.rhand_st > 200:
            return

        if 0 == self.move_state & 1 and 0 == self.move_state & 2:
            if self.gui.lhand_st > 200 and y<370 and y>320 and x<75 and x>20 and 0 == self.arm_state & 2:
                self.move_state = 2
            self.move = 0
        elif 1 == self.move_state & 1 and 0 == self.move_state & 2:
            if self.gui.lhand_st > 200 and y<370 and y>320 and x<155 and x>100 and 0 == self.arm_state & 2:
                self.move_state = 3
            self.move = 100
        elif 2 == self.move_state & 2:
            if self.gui.lhand_st > 200:
                self.move = x - 24*100/80
                if self.move < 0:
                    self.move = 0
                elif self.move > 100:
                    self.move = 100
            else:
                whell = Whells()
                if self.move > 50:
                    self.move_state = 1
                    self.move = 100
                else:
                    self.move_state = 0
                    self.move = 0
                whell.MoveState = self.move_state
                whell.ArmState = self.arm_state
                self.whell_pub.publish(whell)

        #ARM
        y = self.gui.lhand_y + 30
        if 0 == self.arm_state & 1 and 0 == self.arm_state & 2:
            if self.gui.lhand_st > 200 and y<385 and y>325 and x<115 and x>65  and 0 == self.move_state & 2:
                self.arm_state = 2
            self.arm = 0
        elif 1 == self.arm_state & 1 and 0 == self.arm_state & 2:
            if self.gui.lhand_st > 200 and y<470 and y>410 and x<115 and x>65  and 0 == self.move_state & 2:
                self.arm_state = 3
            self.arm = 100
        elif 2 == self.arm_state & 2:
            if self.gui.lhand_st > 200:
                self.arm = y - 325*100/85
                if self.arm < 0:
                    self.arm = 0
                elif self.arm > 100:
                    self.arm = 100
            else:
                whell = Whells()
                if self.arm > 50:
                    self.arm_state = 1
                    self.arm = 100
                else:
                    self.arm_state = 0
                    self.arm = 0
                whell.ArmState = self.arm_state
                whell.MoveState = self.move_state
                self.whell_pub.publish(whell)
        
        self.gui.setButton(self.bk_image, x, y, self.arm, self.move)

    def setWhells(self):
        whell = Whells()
        if self.gui.rhand_st > 200 and self.gui.lhand_st > 200:
            
            if 0 == self.lwhellbase_x and 0 == self.lwhellbase_y and 0 == self.rwhellbase_x and 0 == self.rwhellbase_y:
                self.lwhellbase_x = self.gui.lhand_x
                self.lwhellbase_y = (self.gui.lhand_y + self.gui.rhand_y) / 2
                self.rwhellbase_x = self.gui.rhand_x
                self.rwhellbase_y = self.lwhellbase_y #Stay same with lbase
            else:
                ly = self.gui.lhand_y - self.lwhellbase_y
                if ly < -60:
                    ly = -60
                elif ly > 60:
                    ly = 60
                ry = self.gui.rhand_y - self.rwhellbase_y
                if ry < -60:
                    ry = -60
                elif ry > 60:
                    ry = 60
                
                r = -ry/6
                if r > 0:
                    if r < 4:
                        whell.RightWhell = 0
                    else:
                        whell.RightWhell = r - 4
                else:
                    if r > -4:
                        whell.RightWhell = 0
                    else:
                        whell.RightWhell = r + 4

                l = -ly/6
                if l > 0:
                    if l < 4:
                        whell.LeftWhell = 0
                    else:
                        whell.LeftWhell = l - 4
                else:
                    if l > -4:
                        whell.LeftWhell = 0
                    else:
                        whell.LeftWhell = l + 4
                
        

                self.gui.setMoveBk(self.bk_image, self.lwhellbase_x, self.lwhellbase_y, self.rwhellbase_x, self.rwhellbase_y, ly, ry)
                
        else:
            whell.LeftWhell = 0
            whell.RightWhell = 0
            self.lwhellbase_x = 0
            self.lwhellbase_y = 0
            self.rwhellbase_x = 0
            self.rwhellbase_y = 0

        if whell.RightWhell != self.pre_whell.RightWhell or whell.LeftWhell != self.pre_whell.LeftWhell:
            whell.ArmState = self.arm_state
            whell.MoveState = self.move_state
            self.whell_pub.publish(whell)
            self.pre_whell.RightWhell = whell.RightWhell
            self.pre_whell.LeftWhell = whell.LeftWhell
            

    
    def callback(self, data):
        
        
        try:
            cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
        except CvBridgeError, e:
            rospy.logerr(e)
        
        try:
            cv.Resize(cv_image, self.bk_image)
            cv.Flip(self.bk_image,self.bk_image, 1)
        except cv.error, e:
            rospy.logerr(e) 

        #self.gui.setMenu(self.bk_image, 10)
        
        #Set the background
        self.setButtons()

        # if mode == move
        if 1 == self.move_state & 1:
            self.setWhells()

        self.gui.setHandPointer(self.bk_image)
        
        
        cv.ShowImage("Image window", self.bk_image)
        cv.WaitKey(3)

        try:
            self.image_pub.publish(self.bridge.cv_to_imgmsg(self.bk_image, "bgr8"))
        except CvBridgeError, e:
            rospy.logerr(e)

def main(args):
    
    rospy.init_node('osd_gui', anonymous=True)
    

    ind = args[0].rfind('/')
    gui = gui_generator(args[0][0:ind]+'/../images/')
    
    ic = image_converter(gui)
    
    if rospy.names.remap_name("image") == "image":
        rospy.logwarn('Topic \'image\' has not been remapped!')

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"
    cv.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
            


