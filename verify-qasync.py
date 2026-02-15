import sys
import asyncio
from PyQt6.QtWidgets import QApplication, QLabel
from qasync import QEventLoop, asyncSlot

app = QApplication(sys.argv)
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

label = QLabel("Async QT Running")
label.show()

with loop:
	loop.run_forever()