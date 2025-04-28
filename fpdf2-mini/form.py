class FPDFForm:
    def form_text_field(self, name, x=0, y=0, width=40, height=10):
        print(f"Form Text Field [{name}] at ({x},{y}) size ({width}x{height})")

    def form_checkbox(self, name, x=0, y=0, width=4, height=4):
        print(f"Checkbox [{name}] at ({x},{y}) size ({width}x{height})")
