## Terminal bashrc

1) bashrc
- 현재 shell 확인
```sh
$ echo $SHELL
```
- Sublime으로 .bashrc 열기
```sh
$ subl ~/.bashrc
```
 ※ **.bashrc에 들어가고 나서 제일 마지막 부분에 ros2 setup.bash 읽던 source 명령 추가**
 ```sh
$ echo "ROS2 humble is activated!"
$ source /opt/ros/humble/serup.bash
```
2) bashrc에서 alias 설정
- alias 지정 연습
```sh
$ alias alias_test="echo \"Alias test\""
```
- alias로 humble 만들기
```sh
$ alias humble="source /opt/ros/humble/serup.bash; echo \"ROS2 humble is activated!\""
```
- source ~/.bashrc도 alias 하기
```sh
$ alias sb="source ~/.bashrc; echo\"bashrc is reloaded\""
```

3) ros2 domain 설정
- ros_domain_id 설정
```sh
$ alias ros_domain="export ROS_DOMAIN_ID=13"
```
