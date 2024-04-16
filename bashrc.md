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
$ source /opt/ros/humble/setup.bash
```
2) bashrc에서 alias 설정
- alias 지정 연습
```sh
$ alias alias_test="echo \"Alias test\""
```
- alias로 humble 만들기
```sh
$ alias humble="source /opt/ros/humble/setup.bash; echo \"ROS2 humble is activated!\""
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

## Intermediate Using Bashrc
- **sh 파일을 이용한 관리**
- .bashrc
```sh
source ~/alias_settings.sh
```
- alias_settings.sh
```sh
# argcomplete for ros2 & colcon
alias tmp1="eval \"\$(register-python-argcomplete3 ros2)\""
alias tmp2="tmp1; eval \"\$(register-python-argcomplete3 colcon)\""

# ALIAS settings
ID=13

alias killgazebo="killall gzserver gzclient"

alias sz="source ~/.zshrc; echo \"Zshrc is reloaded!\""
alias sb="source ~/.bashrc; echo \"Bashrc is reloaded!\""

alias ros_domain="export ROS_DOMAIN_ID=\$ID; echo \"ROS_DOMAINID is set to \$ID !\""
alias humble="source /opt/ros/humble/setup.bash; ros_domain; echo \"ROS2 Humble is activated\""

ws_setting()
{
	humble
	source ~/$1/install/local_setup.bash
	echo "$1 workspace is activated."
	tmp2
}

alias  ros2_study="ws_setting \"ros2_study\""

```

##  ROS 시스템이 네트워크에서 다른 호스트와 통신
- 1 : 내 pc만 환경을 한정
- 0 : 외부 호스트와도 통신 허용
```sh
$ export ROS_LOCALHOST_OLNY=0 or 1
```

