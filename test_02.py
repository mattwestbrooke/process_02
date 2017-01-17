# import threading
#
# def worker():
#     """thread worker function"""
#     print 'Worker'
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()



# from PySide import QtGui, QtCore
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def __init__(self, *args):
#         threading.Thread.__init__(self, *args)
#
#         self.job_done = threading.Event()
#         self.qt_object = QtCore.QObject()
#
#     def end_job(self):
#         self.job_done.set()
#
#     def run(self):
#         while not self.job_done.is_set():
#             time.sleep(1)
#
#         QtCore.QObject.emit(self.qt_object, QtCore.SIGNAL("job_done"))
#
#
# th = MyThread()
# th.start()
#
# app = QtGui.QApplication([])
#
# w = QtGui.QWidget()
# btn = QtGui.QPushButton('click me to exit', w)
# QtGui.QVBoxLayout(w)
# w.layout().addWidget(btn)
#
# def btn_clicked():
#     th.end_job()
#
# QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), btn_clicked)
#
# QtCore.QObject.connect(th.qt_object, QtCore.SIGNAL("job_done"), w.close)
#
# w.show()
#
# app.exec_()

#http://stackoverflow.com/questions/20657753/python-pyside-and-progress-bar-threading

from PySide import QtCore, QtGui
import time


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 133)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 10, 361, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 361, 61))
        self.pushButton.setObjectName("pushButton")

        self.worker = Worker()
        self.worker.updateProgress.connect(self.setProgress)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.progressBar.minimum = 1
        self.progressBar.maximum = 100

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.worker.start)

    def setProgress(self, progress):
        self.progressBar.setValue(progress)

#Inherit from QThread
class Worker(QtCore.QThread):

    #This is the signal that will be emitted during the processing.
    #By including int as an argument, it lets the signal know to expect
    #an integer argument when emitting.
    updateProgress = QtCore.Signal(int)

    #You can do any extra things in this init you need, but for this example
    #nothing else needs to be done expect call the super's init
    def __init__(self):
        QtCore.QThread.__init__(self)

    #A QThread is run by calling it's start() function, which calls this run()
    #function in it's own "thread".
    def run(self):
        #Notice this is the same thing you were doing in your progress() function
        for i in range(1, 101):
            #Emit the signal so it can be received on the UI side.
            self.updateProgress.emit(i)
            time.sleep(0.1)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# class MyThread(QtCore.QThread):
#     sig = QtCore.Signal(object)
#
#     def __init__(self, parent=None):
#         QtCore.QThread.__init__(self, parent)
#         self.exiting = 10
#     ...
#
#     def run(self):
#         ...
#         self.sig.emit(market_book_result)
#     ...

