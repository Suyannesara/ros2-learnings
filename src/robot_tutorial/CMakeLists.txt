cmake_minimum_required(VERSION 3.8)
project(robot_tutorial)

set(robot_tutorial_MAJOR_VERSION 0)
set(robot_tutorial_MINOR_VERSION 0)
set(robot_tutorial_PATCH_VERSION 0)
set(robot_tutorial_VERSION
  ${robot_tutorial_MAJOR_VERSION}.${robot_tutorial_MINOR_VERSION}.${robot_tutorial_PATCH_VERSION})

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Create an executable target
add_executable(my_publisher src/main.cpp)

# Link the executable target with the required libraries
target_link_libraries(my_publisher ${rclcpp_LIBRARIES} ${std_msgs_LIBRARIES})

# Install the executable
install(TARGETS
  my_publisher
  DESTINATION lib/${PROJECT_NAME}
)

# Install the launch files
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

# Install the package.xml file
ament_package()