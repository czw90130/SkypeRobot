FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/SkypeRobot/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/SkypeRobot/Angles.h"
  "../msg_gen/cpp/include/SkypeRobot/Whells.h"
  "../msg_gen/cpp/include/SkypeRobot/Hands.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
