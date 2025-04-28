from enums import XPos, YPos

class FPDF:
    def __init__(self):
        self.pages = []
        self.fields = []
        self.case_id_counter = 1

    def add_page(self):
        self.pages.append("New page")

    def set_font(self, family, style='', size=12):
        pass

    def cell(self, w, h=0, txt='', border=0, ln=0, align='', fill=False, link='', new_x=None, new_y=None):
        print(f"Cell: {txt}")

    def multi_cell(self, w, h=0, txt='', border=0, align='', fill=False, new_x=None, new_y=None):
        print(f"MultiCell: {txt}")

    def set_auto_page_break(self, auto=True, margin=0):
        self.auto_page_break = auto
        self.b_margin = margin

    def set_margins(self, left, top, right=None):
        self.l_margin = left
        self.t_margin = top
        self.r_margin = right if right is not None else left

    def ln(self, h=None):
        pass

    def output(self, name='', dest=''):
        if not name:
            name = "output.pdf"
        with open(name, "wb") as f:
            f.write(b"%PDF-1.4\n%EOF")
        print(f"✅ PDF saved as {name}")
