from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QWidget
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from dotenv import dotenv_values, set_key
import os

ENV_FILE = ".env"


class SettingsPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 600, 600)
        self.setStyleSheet("background-color: #2B2A2A; color: white;")

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setSpacing(15)  # Improve spacing

        # Settings title
        title_label = QLabel("Settings")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # API Input Fields
        layout.addWidget(self.create_label("ChatGPT API"))
        self.chatgpt_input = self.create_input("Enter ChatGPT API key")
        layout.addWidget(self.chatgpt_input)

        layout.addWidget(self.create_label("Gemini API"))
        self.gemini_input = self.create_input("Enter Gemini API key")
        layout.addWidget(self.gemini_input)

        layout.addWidget(self.create_label("Hugging Face Token"))
        self.hf_token_input = self.create_input("Enter Hugging Face Token")
        layout.addWidget(self.hf_token_input)

        # Multi-model Hugging Face Repo Input
        layout.addWidget(self.create_label("Hugging Face Model Repositories (one per line)"))
        self.hf_model_input = self.create_textarea("Enter model repos, one per line")
        layout.addWidget(self.hf_model_input)

        # Save Button
        self.set_button = QPushButton("Save Settings")
        self.set_button.setStyleSheet("""
            QPushButton {
                background-color: #4B4B4B;
                color: white;
                padding: 12px;
                font-size: 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #5E5E5E;
            }
            QPushButton:pressed {
                background-color: #737373;
            }
        """)
        self.set_button.setFixedHeight(50)
        self.set_button.clicked.connect(self.set_key)
        layout.addWidget(self.set_button)

        # Success message label (Hidden by default)
        self.success_label = QLabel("Settings have been successfully updated.")
        self.success_label.setFont(QFont("Segoe UI", 12))
        self.success_label.setStyleSheet("color: #00FF7F;")  # Green success color
        self.success_label.setAlignment(Qt.AlignCenter)
        self.success_label.setVisible(False)
        layout.addWidget(self.success_label)

        # Footer
        footer_label = QLabel("©2025 Tudo Tech. All rights reserved.")
        footer_label.setFont(QFont("Segoe UI", 10))
        footer_label.setStyleSheet("color: #CCCCCC;")
        footer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer_label)

        # Load existing .env values
        self.load_existing_values()

        # Set layout
        central_widget.setLayout(layout)

    def create_label(self, text):
        """ Create a styled QLabel for input labels """
        label = QLabel(text)
        label.setFont(QFont("Segoe UI", 16))
        label.setStyleSheet("color: white;")
        return label

    def create_input(self, placeholder):
        """ Create a styled QLineEdit input field """
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setStyleSheet("""
            background-color: #4B4B4B;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 14px;
        """)
        input_field.setFixedHeight(40)
        return input_field

    def create_textarea(self, placeholder):
        """ Create a styled QTextEdit for multi-line input """
        text_area = QTextEdit()
        text_area.setPlaceholderText(placeholder)
        text_area.setStyleSheet("""
            background-color: #4B4B4B;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 14px;
        """)
        text_area.setFixedHeight(100)
        return text_area

    def load_existing_values(self):
        """ Load existing .env values into the input fields """
        env_values = dotenv_values(ENV_FILE)

        self.chatgpt_input.setText(env_values.get("OPENAI_API_KEY", ""))
        self.gemini_input.setText(env_values.get("GOOGLE_API_KEY", ""))
        self.hf_token_input.setText(env_values.get("HUGGINGFACEHUB_API_TOKEN", ""))

        hf_repos = env_values.get("HF_MODEL_REPO", "")
        if hf_repos:
            self.hf_model_input.setPlainText(hf_repos.replace(",", "\n"))

    def set_key(self):
        """ Save API keys and HF model repositories to .env file (update only existing values) """
        keys_to_update = {
            "OPENAI_API_KEY": self.chatgpt_input.text(),
            "GOOGLE_API_KEY": self.gemini_input.text(),
            "HUGGINGFACEHUB_API_TOKEN": self.hf_token_input.text(),
            "HF_MODEL_REPO": self.hf_model_input.toPlainText().strip().replace("\n", ",")
        }

        # Update only if the value is not empty
        for key, value in keys_to_update.items():
            if value:
                set_key(ENV_FILE, key, value)

        # Show success message
        self.success_label.setVisible(True)


if __name__ == "__main__":
    app = QApplication([])
    window = SettingsPage()
    window.show()
    app.exec()
