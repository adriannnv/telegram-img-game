import sys
from pathlib import Path
from PyQt6.QtWidgets import (
	QApplication, QMainWindow, QGraphicsView,
	QGraphicsPixmapItem, QGraphicsScene, QGraphicsTextItem
)
from PyQt6.QtGui import QColor, QFont, QPixmap
from PyQt6.QtCore import Qt, QFile, QIODevice
class GameScene(QGraphicsScene):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setBackgroundBrush(QColor(30, 30, 30))

		# allocates memory for an empty pixmap container
		self.current_image_item = QGraphicsPixmapItem()
		self.current_image_item.setTransformationMode(Qt.TransformationMode.SmoothTransformation)
		
		self.addItem(self.current_image_item)

		self.hud_text = QGraphicsTextItem()
		self.hud_text.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
		self.hud_text.setDefaultTextColor(QColor(255, 255, 255))
		self.hud_text.setZValue(1)
		
		self.addItem(self.hud_text)
	def load_image(self, file_path: Path):
		if not file_path.exists():
			return False
		
		qt_file = QFile(str(file_path))

		if not qt_file.open(QIODevice.OpenModeFlag.ReadOnly):
			return False

		try:
			image_data = qt_file.readAll()
			
			pixmap = QPixmap()
			pixmap.loadFromData(image_data)

			self.current_image_item.setPixmap(pixmap)
			self.setSceneRect(self.current_image_item.boundingRect())
			
			return True
		finally:
			qt_file.close()
	def update_hud(self, text: str):
		self.hud_text.setPlainText(text)
	
class GameView(QGraphicsView):
	def __init__(self, scene: GameScene, parent=None):
		super().__init__(scene, parent)

		self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		self.setFrameShape(QGraphicsView.Shape.NoFrame)

	def resizeEvent(self, event):
		super().resizeEvent(event)
		if self.scene() and not self.scene().sceneRect().isEmpty():
			self.fitInView(self.scene().sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

class MainDebugWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("CuraGram")
		self.resize(1024, 768)

		self.scene = GameScene()
		self.view = GameView(self.scene)
		self.setCentralWidget(self.view)

		test_img_path = Path("/home/guzun/Downloads/Telegram Desktop/ChatExport_2026-02-15/photos/photo_42@04-02-2024_22-30-22.jpg")
		if (test_img_path.exists()):
			self.scene.load_image(test_img_path)
			self.scene.update_hud("Standard viewer mode")
		else:
			self.scene.update_hud("No image found at path: ", test_img_path)

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainDebugWindow()
	window.show()
	
	sys.exit(app.exec())