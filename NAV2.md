# NAV2
## ROS to ROS2 Navigation
* https://navigation.ros.org/about/ros1_comparison.html

1.  Ported packages:

    * amcl: Ported to nav2_amcl
    * map_server: Ported to nav2_map_server
    * nav2_planner: Replaces global_planner, hosts N planner plugins
    * nav2_controller: Replaces local_planner, hosts N controller plugins
    * Navfn: Ported to nav2_navfn_planner
    * DWB: Replaces DWA and ported to ROS 2 under nav2_dwb_controller metapackage
    * nav_core: Ported as nav2_core with updates to interfaces
    * costmap_2d: Ported as nav2_costmap_2d

2.  New packages:

    * nav2_bt_navigator: replaces move_base state machine
    * nav2_lifecycle_manager: Handles the server program lifecycles
    * nav2_waypoint_follower: Can take in many waypoints to execute a complex task through
    * nav2_system_tests: A set of integration tests for CI and basic tutorials in simulation
    * nav2_rviz_plugins: An rviz plugin to control the Navigation2 servers, command, cancel, and navigation with
    * nav2_experimental: Experimental (and incomplete) work for deep reinforement learning controllers
    * navigation2_behavior_trees: wrappers for the behavior tree library to call ROS action servers

## Transforms

1. The first transform ```map => odom``` is usually provided by a different ROS package dealing with localization and mapping such as AMCL. This transform updates live in use so **we don’t set static values for this in our robot’s TF tree.** 
2. The ```odom => base_link``` is usually published by our odometry system using sensors such as wheel encoders. 
3.  If there are multiple sensor base frames (e.g. camera_link, base_laser2, lidar_link etc.), then a **transformation back to base_link for each one is required.**
   
## Configuration
 * https://navigation.ros.org/configuration/index.html

1. AMCL
 * https://navigation.ros.org/configuration/packages/configuring-amcl.html
   ```shell
   ros2 run nav2_amcl amcl
   ```

2. Map Server / Saver
    ```shell
   ros2 run nav2_map_server map_server 7F.yaml
   ```

3. DWB Controller
 * is the default controller.
    ```shell
   ros2 run dwb_controller dwb_controller 
   ```    

4. NavFn Planner
 * implements a wavefront Dijkstra or A* expanded planner.
    ```shell
    ros2 run nav2_navfn_planner navfn_planner 
   ```     


5. Recovery Server
 * implements the server for handling recovery requests and hosting a vector of plugins implementing various C++ recoveries. 
    ```shell
    ros2 run nav2_recoveries recoveries_node 
   ```   
6. Behavior-Tree Navigator
 * implements the NavigateToPose task interface.
    ```shell
    ros2 run nav2_bt_navigator bt_navigator 
   ``` 

7. Lifecycle Manager
 * implements the method for handling the lifecycle transition states for the stack in a deterministic way. 
    ```shell
    ros2 run nav2_lifecycle_manager lifecycle_manager 
   ``` 
 