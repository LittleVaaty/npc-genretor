import json
import sys

from PySide2 import QtWidgets

from src.data_loader import DataLoader
from src.npc import Npc


class MainWindow(QtWidgets.QWidget):
    def __init__(self, settings, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.generated_values = {}
        self.data_loader = DataLoader(settings)
        self.npc = None

        self.setWindowTitle('NPyC Generator')
        self.resize(800, 600)

        self.physical_widget = QtWidgets.QLabel()
        self.physical_widget.setWordWrap(True)
        self.character_widget = QtWidgets.QLabel()
        self.character_widget.setWordWrap(True)
        self.plothook_widget = QtWidgets.QLabel()
        self.plothook_widget.setWordWrap(True)
        self.relationships_widget = QtWidgets.QLabel()
        self.relationships_widget.setWordWrap(True)
        self.generate_btn = QtWidgets.QPushButton('Generate (㇏(•̀ᵥᵥ•́)ノ)')
        self.export_btn = QtWidgets.QPushButton('Export')

        self.generate()
        self._set_layout()
        self._connection()

    def _set_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        hor_layout1 = QtWidgets.QHBoxLayout()
        hor_layout2 = QtWidgets.QHBoxLayout()

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

        # Plot hook
        plothook_grp_cont_widget = QtWidgets.QGroupBox('Plot Hook')
        plothook_grp_cont_layout = QtWidgets.QVBoxLayout()
        plothook_grp_cont_widget.setLayout(plothook_grp_cont_layout)
        plothook_grp_cont_layout.addWidget(self.plothook_widget)

        # Relationships
        relationships_grp_cont_widget = QtWidgets.QGroupBox('Relationships')
        relationships_grp_cont_layout = QtWidgets.QVBoxLayout()
        relationships_grp_cont_widget.setLayout(relationships_grp_cont_layout)
        relationships_grp_cont_layout.addWidget(self.relationships_widget)

        hor_layout1.addWidget(physical_grp_cont_widget)
        hor_layout1.addWidget(character_grp_cont_widget)

        hor_layout2.addWidget(plothook_grp_cont_widget)
        hor_layout2.addWidget(relationships_grp_cont_widget)

        main_layout.addLayout(hor_layout1)
        main_layout.addLayout(hor_layout2)
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
        self.plothook_widget.setText(self.npc.get_plot_hook())
        self.relationships_widget.setText(self.npc.get_relationships())

    def export(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "", ".json")
        filename = "%s%s" % (filename[0], filename[1])
        with open(filename, 'w',  encoding='utf-8') as outfile:
            json.dump(self.generated_values, outfile, ensure_ascii=False, indent=2)
