#!/usr/bin/env python
import roslib; roslib.load_manifest('SkypeRobot')
import rospy
from SkypeRobot.msg import Angles

import Skype4Py


class AppCommunication(object):
    UNKNOWN = 0
    SKYPE_FAILED = 1
    SKYPE_CONNECTED = 2
    OPENING_CONNECTION = 3
    SENDING_INVITATION = 4
    INVITATION_ACCEPTED = 5
    WAITING_ACCEPT = 6
    CONNECTED = 7
    
    def __init__(self, name):
        self.state = self.UNKNOWN
        self.appName = name
	self.app = None
        self.skype = Skype4Py.Skype(Events=self)
	self.angle = Angles()

	if not self.skype.Client.IsRunning:
	    self.skype.Client.Start()
	    rospy.loginfo('Starting Skype..')
        self.skype.Attach()
        self.stream = None
        self.textState = 'Initialization'

	#Register application
        self.app = self.skype.Application(self.appName)
        if None == self.app:
            self.state = self.SKYPE_FAILED
            self.writeStatus()
            return
        self.app.Create()
        self.state = self.SKYPE_CONNECTED
	self.writeStatus()
        
        
    
    def InviteOpponent(self, skypeUsername):
	  
	if self.state != self.SKYPE_CONNECTED and self.state != self.OPENING_CONNECTION:
		return False	
	        
	self.state = self.OPENING_CONNECTION
        
        self.opponentHandle = skypeUsername
        self.opponentName = skypeUsername

        
        self.app.Connect(skypeUsername)
	self.writeStatus()
        
        return True

    def SendMsg(self, data):
        if self.CONNECTED == self.state:
            msgout = ApplicationMessage()
            msgout.Type = ApplicationMessage.APP_MSG
            msgout.Data = data
            self.stream.Write(msgout.ToString())
        
    def AcceptApp(self):
        da = ''
        if self.state == self.INVITATION_ACCEPTED:
            self.state = self.CONNECTED
            self.writeStatus()
        
        msgout = ApplicationMessage()
        msgout.Type = ApplicationMessage.APP_ACCEPT
        msgout.Data = da
        self.stream.Write(msgout.ToString())


    def StopApp(self):

        self.state = self.SKYPE_CONNECTED
	self.writeStatus()
        self.writeStatus()
        self.opponentHandle = ''
        self.opponentName = ''
        da = ''
        
        if(None != self.stream):
            msgout = ApplicationMessage()
            msgout.Type = ApplicationMessage.APP_END
            msgout.Data = da
            self.stream.Write(msgout.ToString())


    def closeAllApplicationStreams(self):
        for astream in self.app.Streams:
            astream.Disconnect()
    
    trigger = '#'

    def CallStatus(self, call, status):
        if status == Skype4Py.clsInProgress \
	and (call.Type == Skype4Py.cltIncomingP2P or call.Type == Skype4Py.cltOutgoingP2P ):
            
	    #if our video  is available then start it
            #if call.VideoSendStatus == Skype4Py.vssAvailable:
            call.StartVideoSend()
            #if we can receive video from the distant end then start it
            #if(call.VideoReceiveStatus == Skype4Py.vssAvailable):
            #   call.StartVideoReceive()
    
    def ProcessCommand(self, username, word):
        result = ''
        if word == 'hello':
            result = 'Hello!'

        elif word == 'help':
            result = 'Sorry no help available'
        
        elif word == 'start':
  
	    self.InviteOpponent(username)
            self.call = self.skype.PlaceCall(username)

            result = 'Connecting ' + username
            
        elif word == 'test':
            
            self.InviteOpponent(username)

            result = 'Connecting ' + username
            
        elif word == 'stop':
            self.StopApp()
            result = 'Stoping connection'
        else:
            result = 'Sorry, I do not recognize your command'

        self.skype.SendMessage(username,result)
        return result

    def MessageStatus(self, msg, status):
      
        if status == Skype4Py.cmsReceived and msg.Body.find(self.trigger) >= 0:
	    
            username = msg.Sender.Handle
            command = msg.Body[msg.Body.find(self.trigger)+1:]
            command = command.lower()
  	    rospy.loginfo('Command message received! From: ' + msg.Sender.Handle)
            self.ProcessCommand(msg.Sender.Handle, command)
	    msg.MarkAsSeen()

	
	

    def ApplicationStreams(self, pApp, pStreams):
	
        if pApp.Name != self.appName:
            return
        for astream in pStreams:
            if astream.PartnerHandle == self.opponentHandle and self.state == self.OPENING_CONNECTION:
                self.stream = astream
                self.state = self.SENDING_INVITATION
                self.writeStatus()
                
                msg = ApplicationMessage()
                msg.Type = ApplicationMessage.APP_INVITE
                self.stream.Write(msg.ToString())
	    elif astream.PartnerHandle == self.opponentHandle:
		self.stream = astream
		

    def ApplicationReceiving(self, pApp, pStreams):
        if pApp.Name != self.appName:

            return
        
        for astream in pStreams:
            msgin = ApplicationMessage()
            msgin.ParseString(astream.Read())

            msgout = ApplicationMessage()

	    if msgin.Type == ApplicationMessage.APP_SKELETON:
                if self.state == self.CONNECTED and astream.PartnerHandle == self.opponentHandle:
		    self.angle = self.parseAngles(msgin.Data)
		    rospy.loginfo(msgin.Data);
		    	    
 		    return
                    
                    #event
            elif msgin.Type == ApplicationMessage.APP_INVITE:
                
                #invitation received - reply with ACK
                self.state = self.INVITATION_ACCEPTED
                self.opponentHandle = astream.PartnerHandle
                self.opponentName = self.opponentHandle
                self.stream = astream
		self.writeStatus()
                
                msgout.Type = ApplicationMessage.INVITE_ACK
                self.stream.Write(msgout.ToString())

            elif msgin.Type == ApplicationMessage.INVITE_ACK:
                if self.state == self.SENDING_INVITATION and astream.PartnerHandle == self.opponentHandle:
                    # invitation ACK RECEIVED
                    self.state = self.WAITING_ACCEPT
                    self.writeStatus()
                    
            elif msgin.Type == ApplicationMessage.APP_ACCEPT:
                if self.state == self.SENDING_INVITATION or self.state == self.WAITING_ACCEPT and astream.PartnerHandle == self.opponentHandle:
                    self.state = self.CONNECTED
                    self.writeStatus()
                    
                    #raise event
            
            elif msgin.Type == ApplicationMessage.APP_MSG:
                if self.state == self.CONNECTED and astream.PartnerHandle == self.opponentHandle:
                    
                    pass
                    #event

            elif msgin.Type == ApplicationMessage.APP_END:
                if self.state != self.SKYPE_CONNECTED and self.state != self.UNKNOWN and astream.PartnerHandle == self.opponentHandle:
                    self.state = SKYP_CONNECTED
                    self.writeStatus()
                    self.stream = None
                    self.opponentHandle = ''
                    self.opponentName = ''
                    self.closeAllApplicationStreams()

                    return

    def writeStatus(self):
        msg = 'Skype'
        if self.state == self.SKYPE_FAILED:
            msg = "Failed to attach to Skype";
            
        elif self.state == self.SKYPE_CONNECTED:
            msg = "Connected to Skype";
                    
        elif self.state == self.OPENING_CONNECTION:
            msg = "Connecting to " + self.opponentName + "...";
                    
        elif self.state == self.SENDING_INVITATION:
            msg = "Inviting " + self.opponentName + " to a app ...";
                    
        elif self.state == self.INVITATION_ACCEPTED:
            msg = "Invited to app by " + self.opponentName;
                    
        elif self.state == self.WAITING_ACCEPT:
            msg = "Waiting for " + self.opponentName + " to accept ...";
            
        elif self.state ==  self.CONNECTED:
            msg = "Connected with " + self.opponentName;

        else:
            msg = "Unknown state";

        rospy.loginfo(msg)
        self.textState = msg

    def parseAngles(self, data):
    
	    msg = Angles()
	    pos = data.find(':')
	    #rospy.loginfo('1')
	    if pos > 0:
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
			while pos > 0 and pos < len(data)-2:
				pos2 = pos +1
				pos = data.find(':',pos2)
				strType = data[pos2:pos]
				pos2 = pos +1
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
	    return msg

    
class ApplicationMessage(object):

    UNKNOWN = [1,'UNKNOWN']
    APP_INVITE = [2,'APP_INVITE']
    INVITE_ACK = [3,'INVITE_ACK']
    APP_DECLINE = [4,'APP_DECLINE']
    APP_ACCEPT = [5,'APP_ACCEPT']
    APP_MSG = [6,'APP_MSG']
    APP_SKELETON = [7,'APP_SKELETON']
    APP_END = [8,'APP_END']

    HeadH = 0
    HeadV = 1
    ShoulderSpin = 2
    ShoulderElbowXLeft = 3
    ShoulderElbowYLeft = 4
    ElbowSpinLeft = 5
    ShoulderElbowWristLeft = 6
    WristSpinLeft = 7
    ElbowWristHandLeft = 8
    ShoulderElbowXRight = 9
    ShoulderElbowYRight = 10
    ElbowSpinRight = 11
    ShoulderElbowWristRight = 12
    WristSpinRight = 13
    ElbowWristHandRight = 14

    Angle = [-1 for x in range(0, 15)]

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
    pub = rospy.Publisher('robotAngles', Angles)
    rospy.init_node('talker')
    angle = Angles()
    preangle = Angles()
    skype = AppCommunication('DemoTest')
    stopDy = 0
    while not rospy.is_shutdown():
        str = "hello world State:" + skype.textState
	angle = skype.angle
	if angle != preangle:
	    if angle.HeadH == -2:
		angle.HeadH = preangle.HeadH
            if angle.HeadV == -2:
		angle.HeadV = preangle.HeadV

            if angle.ShoulderSpin == -2:
		angle.ShoulderSpin = preangle.ShoulderSpin

            if angle.ShoulderElbowXLeft == -2:
		angle.ShoulderElbowXLeft = preangle.ShoulderElbowXLeft

            if angle.ShoulderElbowYLeft == -2:
		angle.ShoulderElbowYLeft = preangle.ShoulderElbowYLeft 

            if angle.ElbowSpinLeft == -2:
		angle.ElbowSpinLeft = preangle.ElbowSpinLeft

            if angle.ShoulderElbowWristLeft == -2:
		angle.ShoulderElbowWristLeft = preangle.ShoulderElbowWristLeft

            if angle.WristSpinLeft == -2:
		angle.WristSpinLeft = preangle.WristSpinLeft

            if angle.ElbowWristHandLeft == -2:
		angle.ElbowWristHandLeft = preangle.ElbowWristHandLeft

            if angle.ShoulderElbowXRight == -2:
		angle.ShoulderElbowXRight = preangle.ShoulderElbowXRight

            if angle.ShoulderElbowYRight == -2:
		angle.ShoulderElbowYRight = preangle.ShoulderElbowYRight

            if angle.ElbowSpinRight == -2:
		angle.ElbowSpinRight = preangle.ElbowSpinRight

            if angle.ShoulderElbowWristRight == -2:
		angle.ShoulderElbowWristRight = preangle.ShoulderElbowWristRight

            if angle.WristSpinRight == -2:
		angle.WristSpinRight = preangle.WristSpinRight

            if angle.ElbowWristHandRight == -2:
		angle.ElbowWristHandRight = preangle.ElbowWristHandRight
		
       	    pub.publish(angle)
	    preangle = angle
	


    skype.StopApp()
    rospy.sleep(2)

    if skype.app != None:
        skype.app.Delete()
        
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
