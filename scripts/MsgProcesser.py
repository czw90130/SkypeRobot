#!/usr/bin/env python
import roslib; roslib.load_manifest('SkypeRobot')
import rospy
from SkypeRobot.msg import Angles
from SkypeRobot.msg import Hands
from SkypeRobot.msg import Whells
from std_msgs.msg import String
from std_msgs.msg import Float64


class Parse(object):

	def __init__(self):
		
		self.preangle = Angles()
	
	def parseAngles(self, data):

		msg = Angles()
		handpos = data.find('H')
		pos = data.find(':')
		data = data[pos+1:]
		pos = data.find(':')

		if pos > 0 and handpos > 0:
			strType = data[0:pos]
			msg.TrackedNum = int(strType)
		
		if msg.TrackedNum == 0:
			msg.HeadH = -1
			msg.HeadV = -1
			msg.ShoulderSpin = -1
			msg.ShoulderElbowXLeft = -1
			msg.ShoulderElbowYLeft = -1
			msg.ElbowSpinLeft = -1
			msg.ShoulderElbowWristLeft = -1
			msg.WristSpinLeft = -1
			msg.ElbowWristHandLeft = -1
			msg.ShoulderElbowXRight = -1
			msg.ShoulderElbowYRight = -1
			msg.ElbowSpinRight = -1
			msg.ShoulderElbowWristRight = -1
			msg.WristSpinRight = -1
			msg.ElbowWristHandRight = -1
			return msg

		elif msg.TrackedNum == 3:
		
			msg.HeadH = -2
			msg.HeadV = -2
			msg.ShoulderSpin = -2
			msg.ShoulderElbowXLeft = -2
			msg.ShoulderElbowYLeft = -2
			msg.ElbowSpinLeft = -2
			msg.ShoulderElbowWristLeft = -2
			msg.WristSpinLeft = -2
			msg.ElbowWristHandLeft = -2
			msg.ShoulderElbowXRight = -2
			msg.ShoulderElbowYRight = -2
			msg.ElbowSpinRight = -2
			msg.ShoulderElbowWristRight = -2
			msg.WristSpinRight = -2
			msg.ElbowWristHandRight = -2
			
			while pos >= 0:
				pos2 = pos +1
				pos = data.find(':',pos2)
				strType = data[pos2:pos]
				if(-1 != strType.find('H')):
					break
				
				pos2 = pos + 1
				pos = data.find(':',pos2)				
			
				if 0 == int(strType):
					strType = data[pos2:pos]
					msg.HeadH = int(strType)
				elif 1 == int(strType):
					strType = data[pos2:pos]
					msg.HeadV = int(strType)
				elif 2 == int(strType):
					strType = data[pos2:pos]
					msg.ShoulderSpin = int(strType)
				elif 3 == int(strType):
					strType = data[pos2:pos]
					msg.ShoulderElbowXLeft = int(strType)
				elif 4 == int(strType):
					strType = data[pos2:pos]
					msg.ShoulderElbowYLeft = int(strType)
				elif 5 == int(strType):
					strType = data[pos2:pos]
					msg.ElbowSpinLeft = int(strType)
				elif 6 == int(strType):
					strType = data[pos2:pos]
					msg.ShoulderElbowWristLeft = int(strType)
				elif 7 == int(strType):
					strType = data[pos2:pos]
					msg.WristSpinLeft  = int(strType)
				elif 8 == int(strType):
					strType = data[pos2:pos]
					msg.ElbowWristHandLeft = int(strType)
				elif 9 == int(strType):
					strType = data[pos2:pos]
					msg.ShoulderElbowXRight = int(strType)
				elif 10 == int(strType):
					strType = data[pos2:pos]
					msg.ShoulderElbowYRight = int(strType)
				elif 11 == int(strType):
					strType = data[pos2:pos]
					msg.ElbowSpinRight = int(strType)
				elif 12 == int(strType):
					strType = data[pos2:pos]
					msg.ShoulderElbowWristRight = int(strType)
				elif 13 == int(strType):
					strType = data[pos2:pos]
					msg.WristSpinRight = int(strType)
				elif 14 == int(strType):
					strType = data[pos2:pos]
					msg.ElbowWristHandRight = int(strType)
					
			pos2 = data.find('H') + 1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandXLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandYLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandXRight = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandYRight = int(strType)
		else:
			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.HeadH = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.HeadV = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.ShoulderSpin = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.ShoulderElbowXLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.ShoulderElbowYLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.ElbowSpinLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.ShoulderElbowWristLeft = int(strType)
	
			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.WristSpinLeft = int(strType)
		    	
			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.ElbowWristHandLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
			msg.ShoulderElbowXRight = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.ShoulderElbowYRight = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.ElbowSpinRight = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.ShoulderElbowWristRight = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.WristSpinRight = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.ElbowWristHandRight = int(strType)

			pos2 = data.find('H') + 1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandXLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandYLeft = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandXRight = int(strType)

			pos2 = pos +1
			pos = data.find(':',pos2)
			strType = data[pos2:pos]
		    	msg.HandYRight = int(strType)
		
			
		return msg

	def callback(self, data):
	       	angle = self.parseAngles(data)
		if angle.HeadH == -2:
			angle.HeadH = self.preangle.HeadH
		if angle.HeadV == -2:
			angle.HeadV = self.preangle.HeadV

		if angle.ShoulderSpin == -2:
			angle.ShoulderSpin = self.preangle.ShoulderSpin

		if angle.ShoulderElbowXLeft == -2:
			angle.ShoulderElbowXLeft = self.preangle.ShoulderElbowXLeft

		if angle.ShoulderElbowYLeft == -2:
			angle.ShoulderElbowYLeft = self.preangle.ShoulderElbowYLeft 

		if angle.ElbowSpinLeft == -2:
			angle.ElbowSpinLeft = self.preangle.ElbowSpinLeft

		if angle.ShoulderElbowWristLeft == -2:
			angle.ShoulderElbowWristLeft = self.preangle.ShoulderElbowWristLeft

		if angle.WristSpinLeft == -2:
			angle.WristSpinLeft = self.preangle.WristSpinLeft

		if angle.ElbowWristHandLeft == -2:
			angle.ElbowWristHandLeft = self.preangle.ElbowWristHandLeft

		if angle.ShoulderElbowXRight == -2:
			angle.ShoulderElbowXRight = self.preangle.ShoulderElbowXRight

		if angle.ShoulderElbowYRight == -2:
			angle.ShoulderElbowYRight = self.preangle.ShoulderElbowYRight

		if angle.ElbowSpinRight == -2:
			angle.ElbowSpinRight = self.preangle.ElbowSpinRight

		if angle.ShoulderElbowWristRight == -2:
			angle.ShoulderElbowWristRight = self.preangle.ShoulderElbowWristRight

		if angle.WristSpinRight == -2:
			angle.WristSpinRight = self.preangle.WristSpinRight

		if angle.ElbowWristHandRight == -2:
			angle.ElbowWristHandRight = self.preangle.ElbowWristHandRight
		
		self.preangle = angle
 
		return angle

class HandParse(object):

	def __init__(self):
		
		self.hands = Hands()
		self.hands.HandLeft = 32768
		self.hands.HandRight = 32768	
	
	def parseHands(self, data):	
		if 'L' == data[6]:
			self.hands.HandLeft = int(data[7:])
			rospy.loginfo('Left hand: %d', self.hands.HandLeft)
		elif 'R'== data[6]:
			self.hands.HandRight = int(data[7:])
			rospy.loginfo('Right hand: %d', self.hands.HandRight)
		
skePar = Parse()
hanPar = HandParse()

def skeleton_callback(data):
	skePar.callback(str(data))	

def hand_callback(data):
	hanPar.parseHands(str(data))


Arm_state = False
Whell_state = True
Whell_left = 0
Whell_right = 0
def state_onoff(data):
	if 0 == data.MoveState:
		Whell_state = False
		Whell_left = 0
		Whell_right = 0
	else:
		Whell_state = True
		Whell_left = data.LeftWhell
		Whell_right = data.RightWhell
	if 0 == data.ArmState:
		Arm_state = False
	else:
		Arm_state = True

	

	


def MsgProcesser():
    angPub = rospy.Publisher('robotAngles', Angles)
    hanPub = rospy.Publisher('robotHands', Hands)

    ################################Change Here!!###########################
    pub01 = rospy.Publisher('/tilt_controller/command', Float64)
    pub02 = rospy.Publisher('/pan_controller/command', Float64)
    pub03 = rospy.Publisher('/ElbowSpin_controller/command', Float64)
    pub04 = rospy.Publisher('/ElbowWrist_controller/command', Float64)
    #######################################################################
    rospy.init_node('MsgProcesser')
    rospy.Subscriber('skypeSkeletonMsg', String, skeleton_callback)
    rospy.Subscriber('skypeHandMsg', String, hand_callback)
    rospy.Subscriber('robotWhells', Whells, hand_callback)
    angle = Angles()
    hand = Hands()
    hand.HandLeft = 32768
    hand.HandRight = 32768
    
    while not rospy.is_shutdown():
	    if angle !=  skePar.preangle: 
		    angPub.publish(skePar.preangle)

		    angle = skePar.preangle

	    if hand.HandLeft !=  hanPar.hands.HandLeft or hand.HandRight !=  hanPar.hands.HandRight: 
    		    hanPub.publish(hanPar.hands)

		    hand.HandLeft =  hanPar.hands.HandLeft
		    hand.HandRight =  hanPar.hands.HandRight

              ##########################Change Here!!####################################
	    if skePar.preangle.TrackedNum != 0 and Arm_state:
		    if angle.ShoulderElbowXLeft<=90:
			    tp =  -float(angle.ShoulderElbowXLeft)*0.017   
			    pub01.publish(tp)
			    #rospy.loginfo("I heard X:%f" % tp)

		    if angle.ShoulderElbowYLeft<=149:
			    tp =  float(angle.ShoulderElbowYLeft)*0.017  
			    pub02.publish(tp)
			    #rospy.loginfo("I heard Y:%f" % tp)
			    tp =  float(angle.ElbowSpinLeft)*0.017 
			    pub03.publish(tp)
			    #rospy.loginfo("I heard _Spin:%f" % tp)
			    tp =  float(angle.ShoulderElbowWristLeft)*0.017 
			    pub04.publish(tp)
			    #rospy.loginfo("I heard _Elbow:%f" % tp)
		#########################################################################

	    
	    
	
        
        
if __name__ == '__main__':
    try:
        MsgProcesser()
    except rospy.ROSInterruptException:
        pass
