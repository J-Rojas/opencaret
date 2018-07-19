from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    """Launch a talker and a listener."""
    return LaunchDescription([
        launch_ros.actions.Node(
            package='canoc', node_executable='transceiver', output='screen'),
        launch_ros.actions.Node(
            package='radar', node_executable='radar_controller', output='screen'),
        launch_ros.actions.Node(
            package='robot_state_publisher', node_executable='robot_state_publisher', 
            arguments=[os.path.join(get_package_share_directory('prius_description'),'urdf','prius.urdf')]
        ),
        launch_ros.actions.Node(
            package='tf2_ros', node_executable='static_transform_publisher',
            arguments=['0', '0', '0', '1.5708', '0', '0', 'world', 'base_link']
        )
])