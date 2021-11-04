import json
import sys

from PySide2 import QtWidgets

from src.Domain.data_loader import DataLoader
from src.Domain.npc import Npc


class PnjGenerator(QtWidgets.QWidget):
    def __init__(self, settings, parent=None):
        super(PnjGenerator, self).__init__(parent=parent)
        self.generated_values = {}
        self.data_loader = DataLoader(settings)
        self.npc = Npc.create_random(self.data_loader)

        self.setWindowTitle('Pnj Generator')
        self.resize(800, 600)

        self.physical_widget = QtWidgets.QLabel(self.npc.get_physical_description())
        self.physical_widget.setWordWrap(True)
        self.character_widget = QtWidgets.QLabel(self.npc.get_character_description())
        self.character_widget.setWordWrap(True)
        self.generate_btn = QtWidgets.QPushButton('Generate (㇏(•̀ᵥᵥ•́)ノ)')
        self.export_btn = QtWidgets.QPushButton('Export')

        self._set_layout()
        self._connection()

    def _set_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        hor_layout = QtWidgets.QHBoxLayout()

        # Physique
        physical_grp_cont_widget = QtWidgets.QGroupBox('Physique')
        physical_grp_cont_layout = QtWidgets.QVBoxLayout()
        physical_grp_cont_widget.setLayout(physical_grp_cont_layout)
        physical_grp_cont_layout.addWidget(self.physical_widget)

        # Character
        character_grp_cont_widget = QtWidgets.QGroupBox('Character')
        character_grp_cont_layout = QtWidgets.QVBoxLayout()
        character_grp_cont_widget.setLayout(character_grp_cont_layout)
        character_grp_cont_layout.addWidget(self.character_widget)

        hor_layout.addWidget(physical_grp_cont_widget)
        hor_layout.addWidget(character_grp_cont_widget)

        main_layout.addLayout(hor_layout)
        main_layout.addWidget(self.generate_btn)
        main_layout.addWidget(self.export_btn)
        self.setLayout(main_layout)

    def _connection(self):
        self.generate_btn.clicked.connect(self.generate)
        self.export_btn.clicked.connect(self.export)

    def generate(self):
        self.npc = Npc.create_random(self.data_loader)
        self.physical_widget.setText(self.npc.get_physical_description())
        self.character_widget.setText(self.npc.get_character_description())

    def export(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "", ".json")
        filename = "%s%s" % (filename[0], filename[1])
        with open(filename, 'w',  encoding='utf-8') as outfile:
            json.dump(self.generated_values, outfile, ensure_ascii=False, indent=2)


def main():
    with open("./settings.json", encoding='utf-8') as json_data_file:
        config = json.load(json_data_file)
    app = QtWidgets.QApplication(sys.argv)
    pnj_generator = PnjGenerator(config)
    pnj_generator.show()
    sys.exit(app.exec_())



