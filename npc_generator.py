import json
import sys

from PySide2 import QtWidgets

from src.main_window import MainWindow

if __name__ == '__main__':
    with open("./settings.json", encoding='utf-8') as json_data_file:
        config = json.load(json_data_file)
    app = QtWidgets.QApplication(sys.argv)
    pnj_generator = MainWindow(config)
    pnj_generator.show()
    sys.exit(app.exec_())
