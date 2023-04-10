import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton

class CenteredWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tech Checkout")
        self.resize(1000, 900)
        self.center()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Label goes here")
        self.label.move(50, 50)

        self.b1 = QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

        self.show()

    def center(self):
        # Get the screen's geometry
        screenGeometry = QDesktopWidget().screenGeometry()

        # Get the size of the window
        windowSize = self.geometry()

        # Calculate the center position
        x = int((screenGeometry.width() - windowSize.width()) / 2)
        y = int((screenGeometry.height() - windowSize.height()) / 2)

        # Move the window to the center
        self.move(x, y)

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CenteredWindow()
    sys.exit(app.exec_())
