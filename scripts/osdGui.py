#! /usr/bin/env python
import roslib
roslib.load_manifest('SkypeRobot')
import sys
import rospy
import cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
    def __init__(self):
        self.image_pub = rospy.Publisher("vcamera",Image)
    
        cv.NamedWindow(">Image window", 1)
        self.bridge =ridge()
        self.image_sub = rospy.Subscriber("image", Image, self.callback)
    
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
        except CvBridgeError, e:
            rospy.logerr(e)

            bk_size = cv.Size(640, 480)
            cv.resize(cv_image, bk_image, bk_size)

            cv.ShowImage("Image window", cv_image)
            cv.WaitKey(3)

            try:
                self.image_pub.publish(self.bridge.cv_to_imgmsg(cv_image, "bgr8"))
            except CvVridgeError, e:
                rospy.logerr(e)

def main(args):
    ic = image_converter()
    rospy.init_node('osd_gui', anonymous=True)

    rospy.loginfo('Hello!')
    
    if rospy.names.remap("image") == "image":
        rospy.logwarn('Topic \'image\' has not been remapped!')

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"
    cv.DestroyAllWindows()


if __name__ == '__main__':
    rospy.loginfo('Hello!')
    main(sys.argv)
    rospy.loginfo('Hello!!!!!!!!!!!1')        


