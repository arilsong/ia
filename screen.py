from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QScrollArea, QLineEdit, QPushButton,
    QLabel, QHBoxLayout
)

import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from prolog import interact

#adicionar mendagen na tela
def add_message(messages_layout, message_text, is_sent=True):
    message_label = QLabel(message_text)
    message_label.setStyleSheet(f"""
        background-color: {'#2ecc71' if is_sent else '#e5e5ea'};
        color: {'white' if is_sent else 'black'};
        padding: 10px;
        border-radius: 10px;
        margin-{'left' if is_sent else 'right'}: 50px;
        margin-bottom: 10px;
        font-size: 15px;
        font-weight: 550;
        max-width: 500px;
        max-height: 100px;
        word-wrap: break-word;
    """)
    message_label.setWordWrap(True)
    message_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    messages_layout.addWidget(message_label)

#enviar mennsagen
def send_message(messages_layout, input_field):
    message_text = input_field.text()
    if message_text.strip():
        add_message(messages_layout, message_text, is_sent=True)
        add_message(messages_layout, interact(message_text), is_sent=False)
        interact(message_text)
        input_field.clear()

def main_screen():
    app = QApplication(sys.argv)

    # Janela principal
    window = QWidget()
    window.setWindowTitle('ChatBot Escola')
    window.setGeometry(100, 100, 400, 600)
    window.setWindowIcon(QIcon("chtBotIcon.png"))

    # Layout principal
    layout = QVBoxLayout()

    # Área de rolagem para mensagens
    scroll_area = QScrollArea()
    scroll_content = QWidget()
    messages_layout = QVBoxLayout(scroll_content)
    scroll_content.setLayout(messages_layout)
    scroll_area.setWidget(scroll_content)
    scroll_area.setWidgetResizable(True)
    layout.addWidget(scroll_area)

    # Área de entrada
    input_layout = QHBoxLayout()

    # Campo de entrada estilizado
    input_field = QLineEdit()
    input_field.setPlaceholderText("Digite algo...")
    input_field.setFixedSize(500, 40)
    input_field.setStyleSheet("""
        QLineEdit {
            background-color: #ecf0f1;
            color: black;
            border-radius: 20px;
            padding: 5px 10px;
            font-size: 14px;
            border: 1px solid #bdc3c7;
        }
    """)

    # Botão estilizado
    button = QPushButton("Enviar")
    button.setFixedSize(100, 40)
    button.setStyleSheet("""
        QPushButton {
            background-color: #2ecc71;
            color: white;
            border-radius: 20px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #27ae60;
        }
    """)
    button.clicked.connect(lambda: send_message(messages_layout, input_field))
    add_message(messages_layout, "Bem-vindo ao ChatBox", is_sent=False)

    input_layout.addWidget(input_field)
    input_layout.addWidget(button)
    layout.addLayout(input_layout)

    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())