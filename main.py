from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys

class ToolBar(QWidget):
    def __init__(self):
        super(ToolBar, self).__init__()

        # Window size
        self.w = 400
        self.h = 50
        self.resize(self.w, self.h)

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.w, self.h)

        # Initial
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        radius = self.h / 2
        self.centralwidget.setStyleSheet(
            '''
            background: rgb(0, 0, 0);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            '''.format(radius)
        )

        self.screenSize = QDesktopWidget().screenGeometry(-1)
        self.getCentered = (self.screenSize.width() / 2) -  (self.w / 2)

        self.setGeometry(self.getCentered, 10, self.w, self.h)

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:transparent;color: #FFFFFF;font-family: 'Arial'; font-size: 14px; font-weight: bold; padding: 0;")
        self.label.setGeometry(QRect(345,15,300,18))

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(10)
        
    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm')
        self.label.setText(label_time)
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

      
if __name__ == '__main__':
    app = QApplication([])
    window = ToolBar()
    window.show()
    sys.exit(app.exec_())
