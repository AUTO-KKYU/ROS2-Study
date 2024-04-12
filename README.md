# ROS2-Study

## Ubuntu 22.04 ROS2 Installation

1) **리눅스의 로케일을 UTF-8로 설정**
- 먼저 apt의 업데이트  및 로케일을 설치
```sh
$ sudo apt update && sudo apt install locales
```
- 로케일을 UTF-8로 설정
```sh
$ sudo locale-gen en_US en_US.UTF-8
$ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
$ export LANG=en_US.UTF-8
```
2) **시스템에 ROS 2를 위한 저장소를 추가**
- 우분투의 universe 저장소를 활성화
```sh
$ apt-cache policy | grep universe
```
- ROS2의 apt 저장소를 시스템에 추가 
  - 다음 명령을 통하여 GPG 키를 승인
```sh
$ sudo apt update && sudo apt install curl gnupg lsb-release
$ sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
 ```
- 소스 리스트에 저장소 추가
```sh
$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
 ```

3) **ROS2 패키지 설치**
- 업데이트 및 업그레이드 
```sh
$ sudo apt update
$ sudo apt upgrade
```
-  ROS, RViz, demos, tutorials 등의 데스크탑 패키지를 설치
```sh
$ sudo apt install ros-humble-desktop
```
- Communication libraries, message packages, command line tools. No GUI tools 등의 ROS-base 패키지를 설치
```sh
$ sudo apt install ros-humble-ros-base
```

4) **ROS2 설치 확인**
- Terminal 1
```sh
$ source /opt/ros/humble/setup.bash
$ ros2 run demo_nodes_cpp talker
```
- Terminal 2
```sh
$ source /opt/ros/humble/setup.bash
$ ros2 run demo_nodes_py listener
```

### TALKER -> Listener
![2024-04-06175040-ezgif com-video-to-gif-converter](https://github.com/AUTO-KKYU/ROS2-Study/assets/118419026/7e0df402-bea3-42ff-9cff-f4190b4b9a85)

---
## Install Editor (sublime text)
url sublime text : https://www.sublimetext.com/docs/linux_repositories.html

```sh
$ wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null
$ echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
$ sudo apt-get update
$ sudo apt-get install sublime-text
```
---
## Install dev tools 
```sh
sudo apt update && sudo apt install -y \
  python3-flake8-docstrings \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools
```
```sh
sudo apt install -y \
   python3-flake8-blind-except \
   python3-flake8-builtins \
   python3-flake8-class-newline \
   python3-flake8-comprehensions \
   python3-flake8-deprecated \
   python3-flake8-import-order \
   python3-flake8-quotes \
   python3-pytest-repeat \
   python3-pytest-rerunfailures
```
## Install colcon 
```sh
sudo apt install python3-colcon-common-extensions
```
