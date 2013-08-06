
(cl:in-package :asdf)

(defsystem "SkypeRobot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Angles" :depends-on ("_package_Angles"))
    (:file "_package_Angles" :depends-on ("_package"))
    (:file "Whells" :depends-on ("_package_Whells"))
    (:file "_package_Whells" :depends-on ("_package"))
    (:file "Hands" :depends-on ("_package_Hands"))
    (:file "_package_Hands" :depends-on ("_package"))
  ))