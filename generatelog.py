from fpdf import FPDF, XPos, YPos
import datetime
import os

class FillableEthicalLog(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(15, 15, 15)
        self.set_font("Helvetica", size=12)
        self.today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.case_id = self.generate_case_id()

    def generate_case_id(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        counter = 1
        base_name = f"DISCOVERY-{today}"
        while os.path.exists(f"logs/{base_name}-{counter:04}.pdf"):
            counter += 1
        return f"{base_name}-{counter:04}"

    def add_title(self, text):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, text, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)
        self.set_font("Helvetica", size=12)

    def draw_label_and_box(self, label, value):
        self.cell(0, 8, f"{label}:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)
        x = self.get_x()
        y = self.get_y()
        box_width = 180  # A4 width minus margins
        box_height = 10

        self.rect(x, y, box_width, box_height)
        self.set_xy(x + 2, y + 2)
        self.cell(box_width - 4, box_height - 4, value, align="L")
        self.ln(box_height + 2)  # Move cursor down for next field

    def generate_log(self):
        self.add_title(f"ETHICAL REPORT CASE ID: {self.case_id}")

        fields = [
            ("Date of Discovery", self.today),
            ("Time (optional)", "Lorem"),
            ("Asset Discovered", "Lorem"),
            ("Discovery Method", "Lorem"),
            ("Description", "Lorem"),
            ("Action Taken", "Lorem"),
            ("Intent", "Lorem"),
            ("Contact Info (optional)", "Lorem"),
            ("Signature (optional)", "Lorem"),
        ]

        for label, value in fields:
            self.draw_label_and_box(label, value)

        self.ln(5)
        self.cell(0, 8, "Ethical Confirmation Checklist:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        checklist = [
            "No unauthorized access performed",
            "No data stolen, viewed, or modified",
            "No damage, harm, or disruption caused",
            "Purpose was strictly educational, ethical, and protective",
        ]

        for item in checklist:
            self.cell(0, 6, f"[ ] {item}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def save(self):
        filename = f"logs/{self.case_id}.pdf"
        self.output(filename)
        print(f"✅ Ethical Discovery Log saved as {filename}")

if __name__ == "__main__":
    pdf = FillableEthicalLog()
    pdf.generate_log()
    pdf.save()
