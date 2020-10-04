import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QFileDialog
from PyQt5.QtCore import Qt

#QWidget 을 상속받아 애플리케이션의 틀 만들기
class MainWindow(QWidget):
	zoom_rate = 0
	# 창의 위치와 크기 정하기 위한 변수
	top		= 200
	left	= 400
	width	= 300
	height	= 300

	def __init__(self):	#창의 초기값 설정
		super().__init__()

		#창의 제목 정해주기
		self.setWindowTitle("사진속 얼굴 태깅 App[송창준]")

		# 창의 위치 및 크기 정하기
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.btn_upload = QPushButton("사진 업로드", self)
		self.btn_upload.clicked.connect(self.getPhotoPath)

		self.btn_zoomin	= QPushButton("+", self)
		self.btn_zoomin.clicked.connect(self.zoom_in_img)

		self.btn_zoomout= QPushButton("-", self)
		self.btn_zoomout.clicked.connect(self.zoom_out_img)

		self.btn_edit	= QPushButton("사진 편집", self)
		self.btn_find	= QPushButton("얼굴 찾기", self)
		self.btn_sel	= QPushButton("얼굴 선택", self)
		self.btn_tag	= QPushButton("얼굴 태깅", self)
		self.btn_save   = QPushButton("사진 저장", self)
		# self.btn_close  = QPushButton("닫기", self)
		# self.btn_close.clicked.connect(self.app_exit)

		btn_box = QHBoxLayout()	# 버튼의 위치를 자동 배열하기 위한 QHBoxLayout 객체 만들기
		# 버튼 위젯 등록하기
		btn_box.addWidget(self.btn_upload)
		btn_box.addWidget(self.btn_edit)
		btn_box.addWidget(self.btn_zoomin)
		btn_box.addWidget(self.btn_zoomout)
		btn_box.addWidget(self.btn_find)
		btn_box.addWidget(self.btn_sel)
		btn_box.addWidget(self.btn_tag)
		btn_box.addWidget(self.btn_save)
#		btn_box.addWidget(self.btn_close)
		self.setLayout(btn_box)

		# QVBoxLayout을 위젯화 시키기
		btns_widget = QWidget()
		btns_widget.setLayout(btn_box)

		self.label = QLabel("여기에 사진이 표시 됩니다.", self)
		self.label.setAlignment(Qt.AlignCenter)
		self.label2 = QLabel("배율" + str(self.zoom_rate), self)
		self.label2.setAlignment(Qt.AlignCenter)
		obj_box = QVBoxLayout()         # QVBoxLayout 객체 만들기
		obj_box.addWidget(btns_widget)  	#위젯화된 버튼박스 레이아웃을 BoxLayout에 등록하기
		obj_box.addWidget(self.label)      # QLabel 객체를 추가
		obj_box.addWidget(self.label2)      # QLabel 객체를 추가
		self.setLayout(obj_box)

	def getPhotoPath(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', './img/*.jpg')
		self.imgpath = fname[0]
		self.loadimg()

	def loadimg(self):
		self.zoom_rate = 1
		self.label2.setText( "배율: " + str(self.zoom_rate*100)+"%")
		self.pixmap = QPixmap(self.imgpath)
		pixmap_resized = self.pixmap.scaled(self.pixmap.width(), self.pixmap.height())
		self.label.setPixmap(pixmap_resized)
		self.label.setAlignment(Qt.AlignCenter)

	def zoom_out_img(self):
		if self.zoom_rate > 0.2 :
			self.zoom_rate = self.zoom_rate - 0.1
			self.setGeometry(self.left, self.top, self.width, self.height)
			self.label2.setText( "배율: " + str(int(self.zoom_rate*100))+"%")
			pixmap_resized = self.pixmap.scaled(int(self.pixmap.width() * self.zoom_rate), int(self.pixmap.height()* self.zoom_rate))
			self.label.setPixmap(pixmap_resized)

	def zoom_in_img(self):
		if self.zoom_rate > 0.1 and self.zoom_rate < 1.9 :
			self.zoom_rate = self.zoom_rate + 0.1
			self.label2.setText("배율: " + str(int(self.zoom_rate*100))+"%")
			pixmap_resized = self.pixmap.scaled(int(self.pixmap.width() * self.zoom_rate), int(self.pixmap.height()* self.zoom_rate))
			self.label.setPixmap(pixmap_resized)

def main():
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	app.exec_()

if __name__ == '__main__':
	main()
