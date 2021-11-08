from src.npc import Npc


class TextExporter:
    def __init__(self):
        self.text_template = "Physique:\n{physique}\n\nCaractère:\n{character}\n\n" \
               "Relation:\n{relationships}\n\nIntrigue\n{plot_hook}"

    def export(self, npc: Npc, filename: str):
        text = self.text_template.format(physique=npc.get_physical_description(), character=npc.get_character_description(), relationships=npc.get_relationships(), plot_hook=npc.get_plot_hook())
        with open(filename, 'w',  encoding='utf-8') as file:
            file.write(text)
