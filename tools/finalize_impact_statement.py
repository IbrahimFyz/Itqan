from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
CORRECTION = ROOT / "docs" / "security-impact-correction.pdf"
COMBINED = ROOT / "docs" / "combined-impact-statement.pdf"


def paragraph(text, style):
    return Paragraph(text, style)


def section(text, style):
    table = Table([[paragraph(text, style)]], colWidths=[17.6 * cm])
    table.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.8, colors.HexColor("#A7A7A7")),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    return table


def create_correction():
    doc = SimpleDocTemplate(str(CORRECTION), pagesize=A4, rightMargin=1.7 * cm, leftMargin=1.7 * cm,
                            topMargin=1.5 * cm, bottomMargin=1.5 * cm)
    styles = getSampleStyleSheet()
    title = ParagraphStyle("Title", parent=styles["Title"], fontName="Times-Bold", fontSize=22,
                           leading=26, textColor=colors.HexColor("#222222"), alignment=0, spaceAfter=12)
    subtitle = ParagraphStyle("Subtitle", parent=styles["Normal"], fontName="Times-Italic", fontSize=11,
                              leading=15, textColor=colors.HexColor("#4A4A4A"), spaceAfter=19)
    h = ParagraphStyle("Heading", parent=styles["Heading2"], fontName="Times-Bold", fontSize=14,
                       leading=17, textColor=colors.HexColor("#222222"), spaceBefore=14, spaceAfter=0)
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Times-Roman", fontSize=11,
                          leading=15.5, spaceAfter=10, textColor=colors.HexColor("#1A1A1A"))
    rows = [
        [paragraph("Earlier wording", body), paragraph("Final phase-one design", body)],
        [paragraph("A learner or guardian accepts an invitation.", body), paragraph("A learner joins a class using its join code. There are no invitation links in the phase-one model.", body)],
        [paragraph("The system collects age to determine guardian consent and verifies the guardian.", body), paragraph("No age or guardian relationship is represented in the current model. A deploying school must establish verified guardian consent and safeguarding before enabling minor access or evaluation.", body)],
        [paragraph("Teacher access rests on guardian acceptance.", body), paragraph("Teacher access rests on the learner’s active class enrolment and role-based authorisation. A join code is not evidence of consent.", body)],
        [paragraph("The analysis service runs outside Saudi Arabia.", body), paragraph("External processing remains a deployment decision. It must not begin until the transfer and vendor review required by the PDPL has been completed.", body)],
    ]
    table = Table(rows, colWidths=[8.8 * cm, 8.8 * cm], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2C3E50")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B9C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F4F6F8"), colors.white]),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story = [Spacer(1, 0.7 * cm), paragraph("Security Impact — Design Correction", title),
             Table([[""]], colWidths=[17.6 * cm], style=TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.6, colors.HexColor("#222222"))])),
             Spacer(1, 8), paragraph("This correction supersedes the listed passages in the earlier Security Impact section.", subtitle),
             section("Final architecture decisions", h), Spacer(1, 9),
             paragraph("The class-enrolment and consent wording in the original security report pre-dated the final ERD and class-diagram decisions. This page makes the final system boundary explicit. All other security positions—including managed identity, no retained recitation audio, access authorisation, and the need for deployment controls—remain unchanged.", body),
             table,
             section("Use in the combined report", h), Spacer(1, 9),
             paragraph("Read this page as part of the Security Impact section. It resolves the contradictions without claiming that guardian verification, cross-border processing, or vendor contracts are already implemented in the phase-one prototype.", body)]
    doc.build(story)


def merge():
    writer = PdfWriter()
    for path in [ROOT / "docs" / "ethical-legal-impact.pdf", CORRECTION, ROOT / "docs" / "security-impact.pdf", ROOT / "docs" / "social-global-impact.pdf"]:
        writer.append(PdfReader(path))
    with COMBINED.open("wb") as out:
        writer.write(out)


if __name__ == "__main__":
    create_correction()
    merge()
