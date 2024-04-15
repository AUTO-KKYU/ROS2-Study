## Recording Topic

1) 먼저 환경 만들기
```sh
$ ros2study
$ ros2 run turtlesim turtlesim_node 
```
2) 새로운 창에서 topic 발행
```sh
$ ros2study
$ ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2., y: 0., z: 0.}, angular: {x: 0., y:0., z: 1.8}}"
```
- topic의 내용은 다음과 같다.
- 특정 토픽에 메시지를 게시하는데, /turtle1/cmd_vel이라는 토픽에 geometry_msgs/msg/Twist 형식의 메시지를 게시
- 거북이의 선속도 및 각속도를 설정한다
- 즉, 이 명령을 실행하면 해당 토픽에 메시지가 발행되어 ROS 시스템 내의 다른 노드에서 이를 구독할 수 있다

3) 새로운 창에서 topic record
```sh
$ ros2study
$ ros2 bag record -o turtle_test -a
```
4) 녹화된 데이터를 재생
- 데이터를 재생함으로써 ROS 시스템에 녹화된 메시지를 다시 게시하여 시스템의 동작을 시뮬레이션하거나 테스트
```sh
$ ros bag play turtle_test
```

### RQt에서도 rosbag 존재
![Screencastfrom04-15-202404_46_14PM-ezgif com-video-to-gif-converter (1)](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/ea753a1a-7068-44ab-8363-d132d3b1893a)

### 실시간 screen background 색상 변경
![Screencastfrom04-15-202405_12_54PM-ezgif com-video-to-gif-converter](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/d5e8e484-c132-4973-9c7c-3aebc53fe07d)

