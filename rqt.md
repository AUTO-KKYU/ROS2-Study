### rqt Plot으로 실시간 확인

- 준비사항 3 terminal
- **Terminal 1**
```sh
$ ros2study
$ ros2 run turtlesim turtlesim_node
```
![Screenshot from 2024-04-15 17-45-35](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/d593269d-2df0-4d54-b461-4d24d15ad4be)

- **Terminal 2**
```sh
$ ros2study
$ ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
![Screenshot from 2024-04-15 17-47-48](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/455c86d7-ef4e-482a-b47d-778d9fb56303)

- **Terminal 3**
```sh
$ ros2study
$ rqt
```

- rqt에서 visualization에 plot 선택
- 원하는 Topic을 선택하거나 제거 가능
<div align="left">
  
![Screencastfrom04-15-202405_50_22PM-ezgif com-video-to-gif-converter](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/6f88c3de-3c0e-436f-9fbe-95ce709889c3)

- Figure options에서 더 보기 좋게 설정 가능
<div align="left">
  
![Screencastfrom04-15-202405_52_59PM-ezgif com-video-to-gif-converter](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/61237e81-b213-4622-bad0-2c17b8192544)
