from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QWidget, QStackedWidget, QLabel
)
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSize
import google.generativeai as genai
from dotenv import load_dotenv
from home import Homepage
from sett import SettingsPage as sett
from search import ModelSearchApp
from chat import ChatRoom

# 加載環境變數
ENV_FILE = ".env"
load_dotenv(ENV_FILE)
cuda = False


class SidebarButton(QPushButton):
    def __init__(self, icon_path, page_index, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(64, 64))
        self.setStyleSheet("""
            QPushButton {
                background-color: #4b4b4b;
                color: #CCCCCC;
                border: none;
                padding: 10px 15px;
                text-align: left;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QPushButton:pressed {
                background-color: #888888;
            }
        """)
        self.page_index = page_index
        self.setFixedHeight(80)
        self.clicked.connect(self.on_click)

    def on_click(self):
        self.parent().switch_page(self.page_index)


class Sidebar(QWidget):
    def __init__(self, parent, stacked_widget):
        super().__init__(parent)
        self.stacked_widget = stacked_widget
        self.setStyleSheet("""
            background-color: #4b4b4b;
            border-right: 1px solid #666666;
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.setFixedWidth(125)

        # 按鈕列表及圖標
        buttons = [
            {"icon": "assets/home.svg", "page_index": 0},
            {"icon": "assets/search.svg", "page_index": 1},
            {"icon": "assets/chat.svg", "page_index": 2},
        ]

        # 創建按鈕並添加到佈局中
        for btn_data in buttons:
            button = SidebarButton(btn_data["icon"], btn_data["page_index"], parent=self)
            layout.addWidget(button)

        # 設置底部設定按鈕
        settings_btn = self.create_settings_button()
        layout.addStretch()  # 使按鈕固定於底部
        layout.addWidget(settings_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def create_settings_button(self):
        settings_btn = QPushButton()
        settings_btn.setIcon(QIcon("assets/setting.svg"))
        settings_btn.setIconSize(QSize(48, 48))
        settings_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #444444;
                border-radius: 10px;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """)
        settings_btn.setFixedSize(50, 50)
        settings_btn.clicked.connect(lambda: self.switch_page(3))
        return settings_btn
# 設定 API Keys（請替換成你的 API Key）

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

class WIPPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("WIP")
        label.setFont(QFont("Segoe UI", 24, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
        self.setStyleSheet("""
            background-color: #1E1E1E;
            border-right: 1px solid #3E3E3E;
        """)
        
        
class FluentUIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Designer")
        self.setGeometry(100, 100, 1400, 800)
        self.setStyleSheet("background-color: #4b4b4b; color: #CCCCCC;")  # 設定整體背景顏色

        # 中央區域佈局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # 堆疊小部件與側邊欄
        self.main_content = QStackedWidget()
        self.sidebar = Sidebar(parent=self, stacked_widget=self.main_content)
        self.main_content.addWidget(Homepage())
        self.main_content.addWidget(ModelSearchApp())
        self.main_content.addWidget(ChatRoom())
        self.main_content.addWidget(sett())
        # 添加側邊欄和主內容區
        main_layout.addWidget(self.sidebar, 1)
        main_layout.addWidget(self.main_content, 4)


if __name__ == "__main__":
    app = QApplication([])
    window = FluentUIApp()
    window.show()
    app.exec()
