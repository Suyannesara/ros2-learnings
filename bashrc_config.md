## Ros2 .bashrc commands

OBS: Substitute where indicated with: **{}**

*1. Open .bashrc file*
```bash
    nano ~/.basrc
```

*2. Copy these commands inside*
```bash
source /opt/ros/**{your_distro}**/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source ~/**{your_ros_worskspace_path}**/install/setup.bash
```

**Done!**


