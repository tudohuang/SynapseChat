from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtCore import Qt


class Homepage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("SynapseTalk")
        self.setStyleSheet("background-color: #2B2A2A;")
        self.setGeometry(100, 100, 800, 600)
        
        # Set background color to dark
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#2B2A2A"))
        self.setPalette(palette)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Add stretchable space before the title to center it vertically
        layout.addStretch()

        # Title text: "SynapseTalk"
        title_label = QLabel("SynapseTalk")
        title_label.setFont(QFont("Arial", 40, QFont.Bold))
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Add another stretchable space after the title to center it vertically
        layout.addStretch()


        # Add a spacer to push the footer to the bottom
        layout.addStretch()

        # Footer text
        footer_label = QLabel("©2025 Tudo Tech. All rights reserved.")
        footer_label.setFont(QFont("Arial", 10))
        footer_label.setStyleSheet("color: #CCCCCC;")
        footer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer_label)

        # Set layout
        central_widget.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = Homepage()
    window.show()
    app.exec()
