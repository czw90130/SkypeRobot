; Auto-generated. Do not edit!


(cl:in-package SkypeRobot-msg)


;//! \htmlinclude Hands.msg.html

(cl:defclass <Hands> (roslisp-msg-protocol:ros-message)
  ((HandLeft
    :reader HandLeft
    :initarg :HandLeft
    :type cl:fixnum
    :initform 0)
   (HandRight
    :reader HandRight
    :initarg :HandRight
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Hands (<Hands>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Hands>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Hands)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name SkypeRobot-msg:<Hands> is deprecated: use SkypeRobot-msg:Hands instead.")))

(cl:ensure-generic-function 'HandLeft-val :lambda-list '(m))
(cl:defmethod HandLeft-val ((m <Hands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HandLeft-val is deprecated.  Use SkypeRobot-msg:HandLeft instead.")
  (HandLeft m))

(cl:ensure-generic-function 'HandRight-val :lambda-list '(m))
(cl:defmethod HandRight-val ((m <Hands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HandRight-val is deprecated.  Use SkypeRobot-msg:HandRight instead.")
  (HandRight m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Hands>) ostream)
  "Serializes a message object of type '<Hands>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'HandLeft)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'HandLeft)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'HandRight)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'HandRight)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Hands>) istream)
  "Deserializes a message object of type '<Hands>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'HandLeft)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'HandLeft)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'HandRight)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'HandRight)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Hands>)))
  "Returns string type for a message object of type '<Hands>"
  "SkypeRobot/Hands")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Hands)))
  "Returns string type for a message object of type 'Hands"
  "SkypeRobot/Hands")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Hands>)))
  "Returns md5sum for a message object of type '<Hands>"
  "5ab3baf2ba0e67706b94d42614b454f4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Hands)))
  "Returns md5sum for a message object of type 'Hands"
  "5ab3baf2ba0e67706b94d42614b454f4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Hands>)))
  "Returns full string definition for message of type '<Hands>"
  (cl:format cl:nil "uint16    HandLeft~%uint16    HandRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Hands)))
  "Returns full string definition for message of type 'Hands"
  (cl:format cl:nil "uint16    HandLeft~%uint16    HandRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Hands>))
  (cl:+ 0
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Hands>))
  "Converts a ROS message object to a list"
  (cl:list 'Hands
    (cl:cons ':HandLeft (HandLeft msg))
    (cl:cons ':HandRight (HandRight msg))
))
