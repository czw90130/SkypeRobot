#!/usr/bin/env python
import roslib; roslib.load_manifest('SkypeRobot')
import rospy
from std_msgs.msg import String

import threading
import serial
from cStringIO import StringIO



class AppCommunication(object):
    
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200):
	self.SkeletonMessage = '0:'
        self.HandMessage = '0:'
        self.KeepRuning = True
        
        self.Serial = serial.Serial(port = port, baudrate = baudrate, timeout = 1)
        self.ReceiverThread = threading.Thread(target=self.Listen)
        self.ReceiverThread.setDaemon(True)
        self.ReceiverThread.start()

    def Listen(self):
        stringIO = StringIO()
        while self.KeepRunning:
            data = self.Serial.read()
            if data == '\0':
                self.ApplicationReceiving(stringIO.getvalue())
                stringIO.close()
                stringIO = StringIO()
            else:
                stringIO.write(data)
	

    def SendMsg(self, data):
        msgout = ApplicationMessage()
        msgout.Type = ApplicationMessage.APP_MSG
        msgout.Data = data
        self.Serial.write(msgout.ToString())


    def StopApp(self):
        rospy.loginfo("Stopping serial gateway")
        self.KeepRuning = False
        time.sleep(.1)
        self.Serial.close()
	

    def ApplicationReceiving(self, stream):
        msgin = ApplicationMessage()
        msgin.ParseString(stream)

        msgout = ApplicationMessage()

        if msgin.Type == ApplicationMessage.APP_SKELETON:
            #Skeleton msg
            self.SkeletonMessage = msgin.Data
            rospy.loginfo(msgin.Data)
                
            return

        elif msgin.Type == ApplicationMessage.APP_HAND:
                #Hand msg
            self.HandMessage = msgin.Data
            rospy.loginfo(msgin.Data)
		    	    
            return

                    

    
class ApplicationMessage(object):

    UNKNOWN = [1,'UNKNOWN']
    APP_INVITE = [2,'APP_INVITE']
    INVITE_ACK = [3,'INVITE_ACK']
    APP_DECLINE = [4,'APP_DECLINE']
    APP_ACCEPT = [5,'APP_ACCEPT']
    APP_MSG = [6,'APP_MSG']
    APP_SKELETON = [7,'APP_SKELETON']
    APP_HAND = [8,'APP_HAND']
    APP_END = [9,'APP_END']


    Type = UNKNOWN

    Data = ''

    def ToString(self):
        
        words = self.Type[1]
        words += ':'
        words += self.Data
        
        return words

    def ParseString(self, words):
        
        self.Type = self.UNKNOWN
        self.Data = ''
        
        pos = words.find(':')

        if pos > 0:
            self.Type = (eval('self.' + words[0:pos]))
            self.Data = words[pos+1:]

	

def talker():
    skePub = rospy.Publisher('skypeSkeletonMsg', String)
    hanPub = rospy.Publisher('skypeHandMsg', String)
    rospy.init_node('talker')
    perSkeMsg = '?'
    perHanMsg = '?'
    skype = AppCommunication()
    stopDy = 0
    while not rospy.is_shutdown():
	
	SkeMsg = skype.SkeletonMessage
	if SkeMsg != perSkeMsg: 
            skePub.publish(SkeMsg)
	perSkeMsg = SkeMsg

        HanMsg = skype.HandMessage
	if HanMsg != perHanMsg: 
            hanPub.publish(HanMsg)
	perHanMsg = HanMsg


    skype.StopApp()
    rospy.sleep(2)

    if skype.app != None:
        skype.app.Delete()
        
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
