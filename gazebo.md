## Gazebo
- 구축한 환경을 기반으로 Gazebo를 이용해서 자동차 운전을 simulation 해보는 과정
- 시뮬레이션을 사용하여 로봇의 동작을 모델링하고 테스트하는 환경
- Gazebo install에 대한 부분은 main.md에서 이미 설명함

---
### gazebo with basic robot car
- urdf.md에서 진행했던 robot_car.xacro에 이어서 진행함

1. 아래 명령을 실행해서 ‘robot_state_publisher’를 실행
   -  이때 use_sim_time 옵션을 true로 설정해서 simulation mode를 활성화
```sh
$ ros2 launch urdf_tutorial robot_car.launch.py use_sim_time:=true
```
2. 두 번째 터미널에서 아래 명령을 실행해서 Gazebo를 실행
```sh
$ ros2 launch gazebo_ros gazebo.launch.py
```
3. 세 번째 터미널에서 gazebo에 'roboto_description' Topic을 spawn
```sh
$ $ ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity with_robot
```

**3번 과정이 조금 복잡하므로, sim.launch.py를 새로 생성하여 이 과정을 하나의 Script로 만들어서 한꺼번에 실행할 수 있도록**

그래서 다음 명령어만 실행하면 모두 1,2,3을 한꺼번에 실행 
```sh
$ ros2 launch urdf_tutorial sim.launch.py
```
---
### Gazebo에서 차량 Simulation
***Gazebo에 자동차를 조절할 수 있는 Plugin을 로딩하고 키보드를 이용해 운전해 보는 과정***

- Gazebo가 diff_dirver Plugin을 사용해서 운전 simulation을 할 수 있도록
- Gazebo에서 robot car을 조정하기 위해 gazebo.xacro 파일을 하나 더 생성 함
- gazebo.xacro file을 include해서 기존 robot_car.xacro 파일에 적용되도록 코드 수정함

#### 최종 실행 과정
1. 아래 명령을 실행해서 ‘sim.launch.py’를 다시 실행
```sh
$ colcon build --symlink-install
$ ros2 launch urdf_tutorial sim.launch.py
```

2. 두 번째 터미널에서 아래 명령을 실행해서 ‘teleop_twist_keyboard’를 실행
```sh
$ ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
**- Rviz Simulation**
  
https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/b26ccd3b-a5a7-4829-aa5d-84a3108e920d


**- Gazebo Simulation**

https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/3c87be81-0f5c-4715-8ba4-62be7810ebe6




