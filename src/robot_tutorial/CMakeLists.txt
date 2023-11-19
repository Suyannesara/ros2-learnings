cmake_minimum_required(VERSION 3.5)
project(robot_tutorial)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Specify source files
set(SOURCE_FILES
  src/main.cpp
)

# Create an executable target
add_executable(my_publisher ${SOURCE_FILES})

# Link the executable target against required libraries
target_link_libraries(my_publisher
  ${rclcpp_LIBRARIES}
  ${std_msgs_LIBRARIES}
)

# Install the executable
install(TARGETS
  my_publisher
  DESTINATION lib/robot_tutorial
)

# Install other files (if any)
install(DIRECTORY
  launch
  DESTINATION share/robot_tutorial/
)

# Add include directories
include_directories(include)

# Export dependencies
ament_export_dependencies(rclcpp std_msgs)

ament_package()
