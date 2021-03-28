from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='python_parameters',
            node_executable='param_talker',
            node_name='custom_parameter_node',
            output='screen',
            parameters=[
                {'my_parameter': 'earth'}
            ]
        ),
        Node(
            package='py_pubsub',
            node_executable='talker',
            node_name='custom_talker_node',
            output='screen',

        ),
    ])
