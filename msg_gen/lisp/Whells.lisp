; Auto-generated. Do not edit!


(cl:in-package SkypeRobot-msg)


;//! \htmlinclude Whells.msg.html

(cl:defclass <Whells> (roslisp-msg-protocol:ros-message)
  ((LeftWhell
    :reader LeftWhell
    :initarg :LeftWhell
    :type cl:fixnum
    :initform 0)
   (RightWhell
    :reader RightWhell
    :initarg :RightWhell
    :type cl:fixnum
    :initform 0)
   (MoveState
    :reader MoveState
    :initarg :MoveState
    :type cl:fixnum
    :initform 0)
   (ArmState
    :reader ArmState
    :initarg :ArmState
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Whells (<Whells>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Whells>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Whells)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name SkypeRobot-msg:<Whells> is deprecated: use SkypeRobot-msg:Whells instead.")))

(cl:ensure-generic-function 'LeftWhell-val :lambda-list '(m))
(cl:defmethod LeftWhell-val ((m <Whells>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:LeftWhell-val is deprecated.  Use SkypeRobot-msg:LeftWhell instead.")
  (LeftWhell m))

(cl:ensure-generic-function 'RightWhell-val :lambda-list '(m))
(cl:defmethod RightWhell-val ((m <Whells>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:RightWhell-val is deprecated.  Use SkypeRobot-msg:RightWhell instead.")
  (RightWhell m))

(cl:ensure-generic-function 'MoveState-val :lambda-list '(m))
(cl:defmethod MoveState-val ((m <Whells>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:MoveState-val is deprecated.  Use SkypeRobot-msg:MoveState instead.")
  (MoveState m))

(cl:ensure-generic-function 'ArmState-val :lambda-list '(m))
(cl:defmethod ArmState-val ((m <Whells>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ArmState-val is deprecated.  Use SkypeRobot-msg:ArmState instead.")
  (ArmState m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Whells>) ostream)
  "Serializes a message object of type '<Whells>"
  (cl:let* ((signed (cl:slot-value msg 'LeftWhell)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'RightWhell)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'MoveState)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'MoveState)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ArmState)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ArmState)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Whells>) istream)
  "Deserializes a message object of type '<Whells>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'LeftWhell) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'RightWhell) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'MoveState)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'MoveState)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ArmState)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'ArmState)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Whells>)))
  "Returns string type for a message object of type '<Whells>"
  "SkypeRobot/Whells")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Whells)))
  "Returns string type for a message object of type 'Whells"
  "SkypeRobot/Whells")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Whells>)))
  "Returns md5sum for a message object of type '<Whells>"
  "6915f32f700bc1942ecaa4b776cd432c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Whells)))
  "Returns md5sum for a message object of type 'Whells"
  "6915f32f700bc1942ecaa4b776cd432c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Whells>)))
  "Returns full string definition for message of type '<Whells>"
  (cl:format cl:nil "int16    LeftWhell~%int16    RightWhell~%uint16	 MoveState~%uint16   ArmState~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Whells)))
  "Returns full string definition for message of type 'Whells"
  (cl:format cl:nil "int16    LeftWhell~%int16    RightWhell~%uint16	 MoveState~%uint16   ArmState~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Whells>))
  (cl:+ 0
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Whells>))
  "Converts a ROS message object to a list"
  (cl:list 'Whells
    (cl:cons ':LeftWhell (LeftWhell msg))
    (cl:cons ':RightWhell (RightWhell msg))
    (cl:cons ':MoveState (MoveState msg))
    (cl:cons ':ArmState (ArmState msg))
))
