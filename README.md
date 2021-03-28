# ROS2-on-Ubuntu-18.04.5-LTS

### Installing ROS 2 via Debian Packages 

* https://docs.ros.org/en/dashing/Installation/Linux-Install-Debians.html

### Tutorials
 * Creating a workspace
 * Writing a simple publisher and subscriber (Python)
 * Using parameters in a class (Python)

 ### Build and run
```shell
# Create a new package
ros2 pkg create --build-type ament_python --node-name my_node my_package

# Build a package
rosdep install -i --from-path src --rosdistro dashing -y
colcon build --packages-select my_package && . install/local_setup.bash

# Run the node
ros2 run my_package my_node
ros2 launch python_parameters python_parameters_launch.py
```
 





