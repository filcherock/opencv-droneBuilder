import sys
import socket
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QGroupBox
)
from PyQt5.QtCore import Qt

class UDPControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UDP Control Panel")
        self.x = 200
        self.y = 0
        self.z = 200
        self.a = 0
        self.g = 0

        # Setup UDP
        self.udp_ip = "192.168.42.241"
        self.udp_port = 8888
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # UI
        self.init_ui()
        self.send_udp()

    def init_ui(self):
        layout = QVBoxLayout()

        self.labels = {}
        for label in ["X", "Y", "Z", "A"]:
            box = QGroupBox(label)
            hbox = QHBoxLayout()

            btn_minus = QPushButton("←")
            btn_plus = QPushButton("→")
            value_label = QLabel("?")
            value_label.setAlignment(Qt.AlignCenter)
            value_label.setFixedWidth(40)
            self.labels[label] = value_label

            btn_minus.clicked.connect(lambda _, l=label: self.update_value(l, -1))
            btn_plus.clicked.connect(lambda _, l=label: self.update_value(l, 1))

            hbox.addWidget(btn_minus)
            hbox.addWidget(value_label)
            hbox.addWidget(btn_plus)

            box.setLayout(hbox)
            layout.addWidget(box)

        # G Radio Button
        self.radio_button = QRadioButton("G = 1")
        self.radio_button.toggled.connect(self.toggle_g)
        layout.addWidget(self.radio_button)

        self.setLayout(layout)

    def update_value(self, param, delta):
        if param == "X":
            self.x += delta
            self.labels["X"].setText(str(self.x))
        elif param == "Y":
            self.y += delta
            self.labels["Y"].setText(str(self.y))
        elif param == "Z":
            self.z += delta
            self.labels["Z"].setText(str(self.z))
        elif param == "A":
            self.a += delta
            self.labels["A"].setText(str(self.a))
        self.send_udp()

    def toggle_g(self):
        self.g = 1 if self.radio_button.isChecked() else 0
        self.radio_button.setText(f"G = {self.g}")
        self.send_udp()

    def send_udp(self):
        message = f"g:{self.x}:{self.y}:{self.a}:{self.z}:{self.g}#"
        print("Sending:", message)
        self.sock.sendto(message.encode(), (self.udp_ip, self.udp_port))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UDPControlApp()
    window.show()
    sys.exit(app.exec_())