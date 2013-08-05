#!/usr/bin/env python
import roslib; roslib.load_manifest('SkypeRobot')
import rospy
from std_msgs.msg import String
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
	self.SkeletonMessage = '0:'
        self.HandMessage = '0:'

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
                #Skeleton msg
                if self.state == self.CONNECTED and astream.PartnerHandle == self.opponentHandle:
                    self.SkeletonMessage = msgin.Data
                    rospy.loginfo(msgin.Data)
		    	    
 		    return

            elif msgin.Type == ApplicationMessage.APP_HAND:
                #Hand msg
                if self.state == self.CONNECTED and astream.PartnerHandle == self.opponentHandle:
                    self.HandMessage = msgin.Data
                    rospy.loginfo(msgin.Data)
		    	    
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
    skype = AppCommunication('DemoTest')
    stopDy = 0
    while not rospy.is_shutdown():
        str = "State:" + skype.textState
	
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
