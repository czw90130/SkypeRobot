FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/SkypeRobot/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/SkypeRobot/msg/__init__.py"
  "../src/SkypeRobot/msg/_Angles.py"
  "../src/SkypeRobot/msg/_Hands.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
