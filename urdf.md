## ROS2 - URDF(Unified Robot Description Format) 

- URDF는 XML 형식으로 구성되며 ROS 및 Gazebo와 연동하여 가상환경에서 다양한 동작을 실험 가능
- ament_cmake, ament_python 둘 다 각각의 환경에서 동작해보았으나 둘 다 비슷비슷함

### Make package 
```sh
$ mkdir -p /urdf_study/src
# choose 1
$ ros2 pkg create --build-type ament_cmake urdf_study
# choose 2
$ ros2 pkg create --build-type ament_python urdf_tutorial
$ cd ..
$ colcon build --symlink-install
```

### Let's start to make basic shape of base_link 

- make folder : launch , urdf , rviz
- add some code in setup.py
  ```sh
  import os
  from glob import glob
  
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
    ],
  ```

  - check spec xacro file (urdf folder)
  - src/urdf_tutorial/urdf/robot_1.xacro
      - base_link: 가상의 링크
      - body: 가로, 세로, 높이 각각 1m인 상자
      - body_joint: base_link와 body를 연결하는 joint
   
  - check launch file (launch folder)
  - src/urdf_tutorial/launch/robot_1.launch.py
    - ‘robot.urdf’ 파일을 ‘robot_description’으로 하는 ‘robot_state_publisher’ 노드를 생성
    - 자세한 내용은 http://wiki.ros.org/robot_state_publisher 참고
    
---

### Prepare 3 new terminal
1. 아래 명령을 실행해서 컴파일 및 ‘robot_1.launch.py’ 파일을 실행
    - workspace에서 실행   
```sh
$ colcon build
$ source install/setup.bash
$ ros2 launch urdf_tutorial robot_1.launch.py
```
<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/64ff390b-7133-48fd-92cd-1d75e9f35be0">

2. 두 번째 터미널에서 아래 명령을 실행해서 Rviz를 실행
```sh
$ source install/setup.bash
$ rviz2
```
<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/280256fb-43f7-4675-96f4-99643c5fa0f4">

3. rviz 실행 창

    3.1 실행된 RViz 창에서 ‘Fixed Frame’을 ‘base_link’로 변경

    3.2 왼쪽 하단의 ‘Add’ 버튼을 누르면 실행되는 팝업창에서 ‘TF’를 선택하고 ‘Ok’ 버튼을 누르기

    3.3 TF의 하위 항목 중 ‘Show Names’를 선택

    3.4 다시 한번 왼쪽 하단의 ‘Add’ 버튼을 누르면 실행되는 팝업창에서 ‘RobotModel’을 선택하고 ‘Ok’ 버튼을 누르기

    3.5 RobotModel의 하위 항목 중 ‘Description Topic’을 ‘/robot_description’으로 변경

    3.6 rviz 설정을 적용하고 싶으면 파일을 저장하고 파일명을 `.rviz`로 지정

<img src = "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/f6c49325-5a33-4c02-9c58-02a1423e0217">


4. rqt_graph로 확인
<img src= "https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/0d0aa19a-71cf-43cf-a41d-0e70188d2e77">
