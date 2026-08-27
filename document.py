class PDFReport:
    def export(self):
        print("Exporting PDF report...")

class ExcelReport:
    def export(self):
        print("Exporting Excel report...")


def generate_report(report):
    report.export()

generate_report(PDFReport())
generate_report(ExcelReport())
                