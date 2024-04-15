## roslaunch

- 패키지 내에 launch 폴더 생성
- 폴더 구조는 다음과 같다.
<img align="left">

![Screenshot from 2024-04-15 16-06-16](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/8a163e11-fe82-4b1f-b830-95d2cb5b50ca)

- turtlesim_and_teleop_launch.py 파일을 생성하여 특정 내용을 삽입하고 setup.py에 코드를 첨가한다
- 추가해야 할 부분은 setup.py에서 다음과 같이 수정한다
```sh
import os
import glob

data_files=[('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py')))]
```
- 추가적으로 my_publisher 일부 토픽이름을 변경한다
```
기존 : '/turtle1/cmd_vel'
변경 : '/turtlesim/turtle1/cmd_vel'
```


### launch 명령어 살펴보기
```sh
$ ros2 launch <패키지 이름> <launch 파일 이름>
$ ros2 launch my_first_package turtlesim_and_teleop.launch.py
```
- 실행 결과는 다음과 같다.
<img align="left">

![4770b73b-dd27-4a3f-9884-f93758aa4df8-ezgif com-video-to-gif-converter](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/3ffd2b04-3798-42b8-869a-df941d363e90)

### 노드와 토픽간의 연결을 시각화 하기 위해 rqt로 확인
![Screenshot from 2024-04-15 16-21-43](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/f0603ca7-2a29-4ea0-9957-f3f622f342de)

- 추가적으로 launch에서는 파라미터도 바꿀 수 있다
Node(package / executable / output / parameters )
