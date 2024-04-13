# ui 없는 version

import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QTimer

from geometry_msgs.msg import Twist
import rclpy

class ControlTurtlesim(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

        self.node = rclpy.create_node('turtlesim_controller')
        self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.draw_circle_timer = None  # Timer for drawing circle

    def init_ui(self):
        self.setGeometry(100, 100, 600, 400)  # Increased window size
        self.setWindowTitle('Turtlesim Control')

        # Labels for linear and angular velocities
        label_linear_x = QLabel('Linear X:', self)
        label_linear_x.setGeometry(380, 50, 80, 30)

        label_linear_y = QLabel('Linear Y:', self)
        label_linear_y.setGeometry(380, 100, 80, 30)

        label_angular_z = QLabel('Angular Z:', self)
        label_angular_z.setGeometry(380, 150, 80, 30)

        # Input fields for linear and angular velocities
        self.linear_x_input = QLineEdit(self)
        self.linear_x_input.setGeometry(460, 50, 100, 30)

        self.linear_y_input = QLineEdit(self)
        self.linear_y_input.setGeometry(460, 100, 100, 30)

        self.angular_z_input = QLineEdit(self)
        self.angular_z_input.setGeometry(460, 150, 100, 30)

        # Buttons for control
        btn_forward = QPushButton('Forward', self)
        btn_forward.setGeometry(50, 50, 150, 50)
        btn_forward.clicked.connect(self.move_forward)

        btn_backward = QPushButton('Backward', self)
        btn_backward.setGeometry(50, 120, 150, 50)
        btn_backward.clicked.connect(self.move_backward)

        btn_rotate_left = QPushButton('Rotate Left', self)
        btn_rotate_left.setGeometry(220, 120, 150, 50)
        btn_rotate_left.clicked.connect(self.rotate_left)

        btn_rotate_right = QPushButton('Rotate Right', self)
        btn_rotate_right.setGeometry(220, 50, 150, 50)
        btn_rotate_right.clicked.connect(self.rotate_right)

        btn_stop = QPushButton('Stop', self)
        btn_stop.setGeometry(50, 190, 150, 50)
        btn_stop.clicked.connect(self.stop)

        btn_launch_turtlesim = QPushButton('Launch Turtlesim', self)
        btn_launch_turtlesim.setGeometry(50, 270, 150, 50)
        btn_launch_turtlesim.clicked.connect(self.launch_turtlesim)

        btn_draw_circle = QPushButton('Draw Circle', self)
        btn_draw_circle.setGeometry(220, 190, 150, 50)
        btn_draw_circle.clicked.connect(self.draw_circle)

        # Additional button to stop drawing circle
        btn_stop_draw_circle = QPushButton('Stop Drawing Circle', self)
        btn_stop_draw_circle.setGeometry(220, 270, 150, 50)
        btn_stop_draw_circle.clicked.connect(self.stop_draw_circle)

    def draw_circle(self):
        if self.draw_circle_timer is not None:  # If already drawing circle, do nothing
            return

        self.draw_circle_timer = QTimer()
        self.draw_circle_timer.timeout.connect(self._draw_circle)
        self.draw_circle_timer.start(100)  # Adjust the interval as needed

    def _draw_circle(self):
        vel = Twist()
        vel.linear.x = 2.0  
        vel.angular.z = 1.8  
        self.publisher.publish(vel)

    def stop_draw_circle(self):
        if self.draw_circle_timer is not None:
            self.draw_circle_timer.stop()
            self.draw_circle_timer = None


    def move_forward(self):
        twist = Twist()
        twist.linear.x = float(self.linear_x_input.text())
        twist.linear.y = float(self.linear_y_input.text())
        self.publisher.publish(twist)

    def move_backward(self):
        twist = Twist()
        twist.linear.x = -float(self.linear_x_input.text())
        twist.linear.y = -float(self.linear_y_input.text())
        self.publisher.publish(twist)

    def rotate_right(self):
        twist = Twist()
        twist.angular.z = -float(self.angular_z_input.text())
        self.publisher.publish(twist)

    def rotate_left(self):
        twist = Twist()
        twist.angular.z = float(self.angular_z_input.text())
        self.publisher.publish(twist)

    def stop(self):
        twist = Twist()
        self.publisher.publish(twist)

    def launch_turtlesim(self):
        subprocess.Popen(['ros2', 'run', 'turtlesim', 'turtlesim_node'])

def main():
    rclpy.init()
    app = QApplication(sys.argv)
    window = ControlTurtlesim()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()