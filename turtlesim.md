## ROS2 Turtlesim

1) Install turtlesim package
```sh
$ sudo apt install ros-humble-turtlesim
```
2) Check turtlesim package
```sh
$ . ~/ros2_rolling/install/local_setup.bash
$ ros2 pkg executables turtlesim
```
3) Execute Turtlesim
```sh
$ . ~/ros2_rolling/install/local_setup.bash
```

4) Control Turtlesim
```sh
$ ros2 run turtlesim turtle_teleop_key
```
---
## ROS2 rqt

1) Install rqt
```sh
$ sudo apt install ~nros-humble-rqt*
$ rqt
```
2) 기존 turtle 말고 spawn 활용하여 새로운 turtle 제어 하고 싶을 때, 터미널 창 새로 열기
```sh
$ ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:='이름'/cmd_vel
```
