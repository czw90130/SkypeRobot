; Auto-generated. Do not edit!


(cl:in-package SkypeRobot-msg)


;//! \htmlinclude Angles.msg.html

(cl:defclass <Angles> (roslisp-msg-protocol:ros-message)
  ((TrackedNum
    :reader TrackedNum
    :initarg :TrackedNum
    :type cl:fixnum
    :initform 0)
   (HeadH
    :reader HeadH
    :initarg :HeadH
    :type cl:fixnum
    :initform 0)
   (HeadV
    :reader HeadV
    :initarg :HeadV
    :type cl:fixnum
    :initform 0)
   (ShoulderSpin
    :reader ShoulderSpin
    :initarg :ShoulderSpin
    :type cl:fixnum
    :initform 0)
   (ShoulderElbowXLeft
    :reader ShoulderElbowXLeft
    :initarg :ShoulderElbowXLeft
    :type cl:fixnum
    :initform 0)
   (ShoulderElbowYLeft
    :reader ShoulderElbowYLeft
    :initarg :ShoulderElbowYLeft
    :type cl:fixnum
    :initform 0)
   (ElbowSpinLeft
    :reader ElbowSpinLeft
    :initarg :ElbowSpinLeft
    :type cl:fixnum
    :initform 0)
   (ShoulderElbowWristLeft
    :reader ShoulderElbowWristLeft
    :initarg :ShoulderElbowWristLeft
    :type cl:fixnum
    :initform 0)
   (WristSpinLeft
    :reader WristSpinLeft
    :initarg :WristSpinLeft
    :type cl:fixnum
    :initform 0)
   (ElbowWristHandLeft
    :reader ElbowWristHandLeft
    :initarg :ElbowWristHandLeft
    :type cl:fixnum
    :initform 0)
   (ShoulderElbowXRight
    :reader ShoulderElbowXRight
    :initarg :ShoulderElbowXRight
    :type cl:fixnum
    :initform 0)
   (ShoulderElbowYRight
    :reader ShoulderElbowYRight
    :initarg :ShoulderElbowYRight
    :type cl:fixnum
    :initform 0)
   (ElbowSpinRight
    :reader ElbowSpinRight
    :initarg :ElbowSpinRight
    :type cl:fixnum
    :initform 0)
   (ShoulderElbowWristRight
    :reader ShoulderElbowWristRight
    :initarg :ShoulderElbowWristRight
    :type cl:fixnum
    :initform 0)
   (WristSpinRight
    :reader WristSpinRight
    :initarg :WristSpinRight
    :type cl:fixnum
    :initform 0)
   (ElbowWristHandRight
    :reader ElbowWristHandRight
    :initarg :ElbowWristHandRight
    :type cl:fixnum
    :initform 0)
   (HandXLeft
    :reader HandXLeft
    :initarg :HandXLeft
    :type cl:fixnum
    :initform 0)
   (HandYLeft
    :reader HandYLeft
    :initarg :HandYLeft
    :type cl:fixnum
    :initform 0)
   (HandXRight
    :reader HandXRight
    :initarg :HandXRight
    :type cl:fixnum
    :initform 0)
   (HandYRight
    :reader HandYRight
    :initarg :HandYRight
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Angles (<Angles>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Angles>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Angles)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name SkypeRobot-msg:<Angles> is deprecated: use SkypeRobot-msg:Angles instead.")))

(cl:ensure-generic-function 'TrackedNum-val :lambda-list '(m))
(cl:defmethod TrackedNum-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:TrackedNum-val is deprecated.  Use SkypeRobot-msg:TrackedNum instead.")
  (TrackedNum m))

(cl:ensure-generic-function 'HeadH-val :lambda-list '(m))
(cl:defmethod HeadH-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HeadH-val is deprecated.  Use SkypeRobot-msg:HeadH instead.")
  (HeadH m))

(cl:ensure-generic-function 'HeadV-val :lambda-list '(m))
(cl:defmethod HeadV-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HeadV-val is deprecated.  Use SkypeRobot-msg:HeadV instead.")
  (HeadV m))

(cl:ensure-generic-function 'ShoulderSpin-val :lambda-list '(m))
(cl:defmethod ShoulderSpin-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ShoulderSpin-val is deprecated.  Use SkypeRobot-msg:ShoulderSpin instead.")
  (ShoulderSpin m))

(cl:ensure-generic-function 'ShoulderElbowXLeft-val :lambda-list '(m))
(cl:defmethod ShoulderElbowXLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ShoulderElbowXLeft-val is deprecated.  Use SkypeRobot-msg:ShoulderElbowXLeft instead.")
  (ShoulderElbowXLeft m))

(cl:ensure-generic-function 'ShoulderElbowYLeft-val :lambda-list '(m))
(cl:defmethod ShoulderElbowYLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ShoulderElbowYLeft-val is deprecated.  Use SkypeRobot-msg:ShoulderElbowYLeft instead.")
  (ShoulderElbowYLeft m))

(cl:ensure-generic-function 'ElbowSpinLeft-val :lambda-list '(m))
(cl:defmethod ElbowSpinLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ElbowSpinLeft-val is deprecated.  Use SkypeRobot-msg:ElbowSpinLeft instead.")
  (ElbowSpinLeft m))

(cl:ensure-generic-function 'ShoulderElbowWristLeft-val :lambda-list '(m))
(cl:defmethod ShoulderElbowWristLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ShoulderElbowWristLeft-val is deprecated.  Use SkypeRobot-msg:ShoulderElbowWristLeft instead.")
  (ShoulderElbowWristLeft m))

(cl:ensure-generic-function 'WristSpinLeft-val :lambda-list '(m))
(cl:defmethod WristSpinLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:WristSpinLeft-val is deprecated.  Use SkypeRobot-msg:WristSpinLeft instead.")
  (WristSpinLeft m))

(cl:ensure-generic-function 'ElbowWristHandLeft-val :lambda-list '(m))
(cl:defmethod ElbowWristHandLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ElbowWristHandLeft-val is deprecated.  Use SkypeRobot-msg:ElbowWristHandLeft instead.")
  (ElbowWristHandLeft m))

(cl:ensure-generic-function 'ShoulderElbowXRight-val :lambda-list '(m))
(cl:defmethod ShoulderElbowXRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ShoulderElbowXRight-val is deprecated.  Use SkypeRobot-msg:ShoulderElbowXRight instead.")
  (ShoulderElbowXRight m))

(cl:ensure-generic-function 'ShoulderElbowYRight-val :lambda-list '(m))
(cl:defmethod ShoulderElbowYRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ShoulderElbowYRight-val is deprecated.  Use SkypeRobot-msg:ShoulderElbowYRight instead.")
  (ShoulderElbowYRight m))

(cl:ensure-generic-function 'ElbowSpinRight-val :lambda-list '(m))
(cl:defmethod ElbowSpinRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ElbowSpinRight-val is deprecated.  Use SkypeRobot-msg:ElbowSpinRight instead.")
  (ElbowSpinRight m))

(cl:ensure-generic-function 'ShoulderElbowWristRight-val :lambda-list '(m))
(cl:defmethod ShoulderElbowWristRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ShoulderElbowWristRight-val is deprecated.  Use SkypeRobot-msg:ShoulderElbowWristRight instead.")
  (ShoulderElbowWristRight m))

(cl:ensure-generic-function 'WristSpinRight-val :lambda-list '(m))
(cl:defmethod WristSpinRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:WristSpinRight-val is deprecated.  Use SkypeRobot-msg:WristSpinRight instead.")
  (WristSpinRight m))

(cl:ensure-generic-function 'ElbowWristHandRight-val :lambda-list '(m))
(cl:defmethod ElbowWristHandRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:ElbowWristHandRight-val is deprecated.  Use SkypeRobot-msg:ElbowWristHandRight instead.")
  (ElbowWristHandRight m))

(cl:ensure-generic-function 'HandXLeft-val :lambda-list '(m))
(cl:defmethod HandXLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HandXLeft-val is deprecated.  Use SkypeRobot-msg:HandXLeft instead.")
  (HandXLeft m))

(cl:ensure-generic-function 'HandYLeft-val :lambda-list '(m))
(cl:defmethod HandYLeft-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HandYLeft-val is deprecated.  Use SkypeRobot-msg:HandYLeft instead.")
  (HandYLeft m))

(cl:ensure-generic-function 'HandXRight-val :lambda-list '(m))
(cl:defmethod HandXRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HandXRight-val is deprecated.  Use SkypeRobot-msg:HandXRight instead.")
  (HandXRight m))

(cl:ensure-generic-function 'HandYRight-val :lambda-list '(m))
(cl:defmethod HandYRight-val ((m <Angles>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader SkypeRobot-msg:HandYRight-val is deprecated.  Use SkypeRobot-msg:HandYRight instead.")
  (HandYRight m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Angles>) ostream)
  "Serializes a message object of type '<Angles>"
  (cl:let* ((signed (cl:slot-value msg 'TrackedNum)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'HeadH)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'HeadV)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ShoulderSpin)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ShoulderElbowXLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ShoulderElbowYLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ElbowSpinLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ShoulderElbowWristLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'WristSpinLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ElbowWristHandLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ShoulderElbowXRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ShoulderElbowYRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ElbowSpinRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ShoulderElbowWristRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'WristSpinRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ElbowWristHandRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'HandXLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'HandYLeft)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'HandXRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'HandYRight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Angles>) istream)
  "Deserializes a message object of type '<Angles>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'TrackedNum) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'HeadH) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'HeadV) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ShoulderSpin) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ShoulderElbowXLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ShoulderElbowYLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ElbowSpinLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ShoulderElbowWristLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'WristSpinLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ElbowWristHandLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ShoulderElbowXRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ShoulderElbowYRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ElbowSpinRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ShoulderElbowWristRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'WristSpinRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ElbowWristHandRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'HandXLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'HandYLeft) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'HandXRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'HandYRight) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Angles>)))
  "Returns string type for a message object of type '<Angles>"
  "SkypeRobot/Angles")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Angles)))
  "Returns string type for a message object of type 'Angles"
  "SkypeRobot/Angles")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Angles>)))
  "Returns md5sum for a message object of type '<Angles>"
  "961f4b7ebde630ec3d43d34559d7d4da")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Angles)))
  "Returns md5sum for a message object of type 'Angles"
  "961f4b7ebde630ec3d43d34559d7d4da")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Angles>)))
  "Returns full string definition for message of type '<Angles>"
  (cl:format cl:nil "int16    TrackedNum~%int16	 HeadH~%int16    HeadV~%int16    ShoulderSpin~%int16    ShoulderElbowXLeft~%int16    ShoulderElbowYLeft~%int16    ElbowSpinLeft~%int16    ShoulderElbowWristLeft~%int16    WristSpinLeft~%int16    ElbowWristHandLeft~%int16    ShoulderElbowXRight~%int16    ShoulderElbowYRight~%int16    ElbowSpinRight~%int16    ShoulderElbowWristRight~%int16    WristSpinRight~%int16    ElbowWristHandRight~%int16    HandXLeft~%int16    HandYLeft~%int16    HandXRight~%int16    HandYRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Angles)))
  "Returns full string definition for message of type 'Angles"
  (cl:format cl:nil "int16    TrackedNum~%int16	 HeadH~%int16    HeadV~%int16    ShoulderSpin~%int16    ShoulderElbowXLeft~%int16    ShoulderElbowYLeft~%int16    ElbowSpinLeft~%int16    ShoulderElbowWristLeft~%int16    WristSpinLeft~%int16    ElbowWristHandLeft~%int16    ShoulderElbowXRight~%int16    ShoulderElbowYRight~%int16    ElbowSpinRight~%int16    ShoulderElbowWristRight~%int16    WristSpinRight~%int16    ElbowWristHandRight~%int16    HandXLeft~%int16    HandYLeft~%int16    HandXRight~%int16    HandYRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Angles>))
  (cl:+ 0
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Angles>))
  "Converts a ROS message object to a list"
  (cl:list 'Angles
    (cl:cons ':TrackedNum (TrackedNum msg))
    (cl:cons ':HeadH (HeadH msg))
    (cl:cons ':HeadV (HeadV msg))
    (cl:cons ':ShoulderSpin (ShoulderSpin msg))
    (cl:cons ':ShoulderElbowXLeft (ShoulderElbowXLeft msg))
    (cl:cons ':ShoulderElbowYLeft (ShoulderElbowYLeft msg))
    (cl:cons ':ElbowSpinLeft (ElbowSpinLeft msg))
    (cl:cons ':ShoulderElbowWristLeft (ShoulderElbowWristLeft msg))
    (cl:cons ':WristSpinLeft (WristSpinLeft msg))
    (cl:cons ':ElbowWristHandLeft (ElbowWristHandLeft msg))
    (cl:cons ':ShoulderElbowXRight (ShoulderElbowXRight msg))
    (cl:cons ':ShoulderElbowYRight (ShoulderElbowYRight msg))
    (cl:cons ':ElbowSpinRight (ElbowSpinRight msg))
    (cl:cons ':ShoulderElbowWristRight (ShoulderElbowWristRight msg))
    (cl:cons ':WristSpinRight (WristSpinRight msg))
    (cl:cons ':ElbowWristHandRight (ElbowWristHandRight msg))
    (cl:cons ':HandXLeft (HandXLeft msg))
    (cl:cons ':HandYLeft (HandYLeft msg))
    (cl:cons ':HandXRight (HandXRight msg))
    (cl:cons ':HandYRight (HandYRight msg))
))
