import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QUrl
from PyQt6.QtQml import QQmlApplicationEngine
import os
import django

def main():
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.backend.settings')
    django.setup()

    # Initialize Qt Application
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Load the main QML file (to be created)
    engine.load(QUrl.fromLocalFile('frontend/views/main.qml'))

    if not engine.rootObjects():
        return -1

    return app.exec()

if __name__ == '__main__':
    sys.exit(main())