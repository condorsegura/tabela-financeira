# trabalho financeiro 
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont

class MeuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Plataforma Desktop")  # Título da Janela
        self.setGeometry(500, 500, 500, 500)  # Posição e tamanho da janela

        # Criar botão
        botao = QPushButton("Clique Aqui", self)
        botao.setFont(QFont("Arial", 14))
        botao.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(botao)
        self.setLayout(layout)

# Inicializa aplicação
app = QApplication(sys.argv)
janela = MeuApp()
janela.show()
sys.exit(app.exec())
