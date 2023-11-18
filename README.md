### ROS2 Package Creation and Node Setup
**Tasks Described:**
1. [Create a Package](#1-create-a-package)
   1. [Specify Package Build System Type](#11-specify-package-build-system-type-ament_python-or-cmake)
   2. [Specify Package Dependencies](#12-specify-package-dependencies)
2. [Build Package](#2-build-package)
3. [Setup a Node](#3-node-setup)
4. [Run a Node](#4-run-a-node)
5. [Other Useful Commands](#5-other-useful-commands)
---

### 1. Create a Package

#### 1.1 Specify Package Build System Type (ament_python OR cmake)

```bash
$ ros2 pkg create your_package_name --build-type ament_python
```

#### 1.2 Specify Package Dependencies

```bash
$ ros2 pkg create your_package_name --dependencies dependency_name
```

### 2. Build Package

**Note:** Using `colcon` as the build tool.

```bash
$ cd workspace_folder (root)
$ colcon build
$ source ./install/setup.bash
```

### 3. Node Setup

Edit `./your_package_name/setup.py` and add a console script as an entry point for your node.

```python
setup(
    # ... other configurations ...
    entry_points={
        'console_scripts': [
            "my_first_node = my_robot_controller.my_first_node:main"
        ],
    }
)
```

Explanation:

- `"my_first_node = my_robot_controller.my_first_node:main"`
    - `my_first_node`: The name you want to use to run your node.
    - `my_robot_controller.my_first_node`: Path to your node script.
    - `main`: The function to be executed when the node is run.

### 4. Run a Node

```bash
$ ros2 run my_robot_controller my_first_node
```

Explanation:

- `my_robot_controller`: Package name.
- `my_first_node`: Node name.

### 5. Other Useful Commands

#### Make Node File Executable

Only necessary while not downloading the executable script.

```bash
$ chmod +x my_first_node.py
```

#### Build with Symlink Install

In order not to rebuild every time.

```bash
$ colcon build --symlink-install
```

#### Open Nodes Graph

```bash
$ rqt_graph
```