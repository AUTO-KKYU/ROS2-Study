## Show Mobile Robot Model on Rviz

- Rviz Setting
    -  Fixed Frame : base_link
    -  Add RobotModel → Description Topic : robot_description
 - 이전 모델에 대해서는 rviz로 저장해서 같은 명령어를 실행하면 가장 최신에 대한 내용만 나옴
  
- bashrc로 alias -> humble 설정 이미 완료한 상태임. 코드 수정했으면 colcon build 해주기

- basic model
```sh
$ ros2 launch my_robot_description display.launch.xml
```
<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/9d4d04fb-5730-48f8-99b8-90411f8c0dea">

- basic model with wheels
<img src="https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/156823ee-f47e-464a-aa68-58d3e5d05c3e">

- wheels + Ultrasonic Sensor
<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/494ccff5-f1c8-415b-a8f9-ecd74f6a42bf">

- wheels + Ultrasonic Sensor + 2D LIDAR
<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/9f2b9769-5cb3-4aca-b142-f34d557319ac">

---
## Show Mobile Robot Model on Gazebo

- URDF에서 rviz로 로봇을 관찰하는 것은 즐거운 일이지만, 물성(중력, 관성, 충돌)을 보여주지는 않는다
- 이런 경우 물리엔진이 탑재가 된 프로그램이 필요한데 ROS 유저는 GAZEBO를 많이 사용함

```sh
$ ros2 launch my_robot_gazebo launch_sim.launch.xml
```
<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/3db959d6-0325-43a3-a87d-b95596076de7">

<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/eb56a5e3-3991-41c0-8afc-cb601c1d077d">

https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/1d90a403-fc1b-4486-813d-b693884211c2

https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/0ec36525-28f2-4b92-af0a-76957a39349a

https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/4ef80dc2-2294-41ec-8fb5-df835b178a19




