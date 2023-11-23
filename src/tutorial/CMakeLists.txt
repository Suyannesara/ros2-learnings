cmake_minimum_required(VERSION 3.8)
project(tutorial)

set(tutorial_MAJOR_VERSION 0)
set(tutorial_MINOR_VERSION 0)
set(tutorial_PATCH_VERSION 0)
set(tutorial_VERSION
  ${tutorial_MAJOR_VERSION}.${tutorial_MINOR_VERSION}.${tutorial_PATCH_VERSION})

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


# find dependencies
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(controller_manager REQUIRED)
find_package(diff_drive_controller REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(gazebo_ros_control REQUIRED)
find_package(joint_state_controller REQUIRED)
find_package(position_controllers REQUIRED)
find_package(velocity_controllers REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(rqt_robot_steering REQUIRED)
find_package(rviz REQUIRED)
find_package(xacro REQUIRED)
