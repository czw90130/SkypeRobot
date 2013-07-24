FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/SkypeRobot/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/Angles.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Angles.lisp"
  "../msg_gen/lisp/Hands.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Hands.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
