from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
ARCHITECTURE = ROOT / "docs" / "system-architecture.pdf"
CORRECTION = ROOT / "docs" / "system-architecture-correction.pdf"


def p(text, style):
    return Paragraph(text, style)


def section(text, style):
    table = Table([[p(text, style)]], colWidths=[17.6 * cm])
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
        [p("Architecture area", body), p("Final phase-one decision", body)],
        [p("Identity", body), p("Authentication is delegated to a managed identity provider. USER stores the provider-issued <b>identity_subject</b>; no local password hash is stored.", body)],
        [p("Consent", body), p("CONSENT_RECORD records the user, purpose, policy version, method, granted/withdrawn status, and timestamp. Consent is an auditable history, not a single account flag.", body)],
        [p("Class enrolment", body), p("A learner joins a LEARNING_CLASS with its <b>join_code</b>. The phase-one design has no invitation-link entity or acceptance flow.", body)],
        [p("Teacher access", body), p("Access is role-based and limited to active class enrolment. The system uses learner terminology outside teacher-facing copy.", body)],
        [p("Audio and external analysis", body), p("Recitation audio remains in memory for analysis and is not retained. External processing is not a deployment assumption: it requires a completed vendor and PDPL transfer review before use.", body)],
    ]
    table = Table(rows, colWidths=[5.1 * cm, 12.5 * cm], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2C3E50")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B9C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F4F6F8"), colors.white]),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story = [Spacer(1, 0.7 * cm), p("System Architecture — Final Design Correction", title),
             Table([[""]], colWidths=[17.6 * cm], style=TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.6, colors.HexColor("#222222"))])),
             Spacer(1, 8), p("This correction is the authoritative phase-one data and access boundary for the System Architecture and Technology Stack document.", subtitle),
             section("Final architecture decisions", h), Spacer(1, 9),
             p("The original architecture PDF is retained because its authoring source is not tracked in the repository. This page is inserted as its first page and supersedes any earlier wording that conflicts with the ERD, relational schema, class diagrams, or requirements traceability artifacts.", body), table,
             section("Submission use", h), Spacer(1, 9),
             p("Read this correction together with the architecture document. It preserves the existing component, data-flow, and no-audio-retention design while resolving the final identity, consent, enrolment, terminology, and external-processing decisions.", body)]
    doc.build(story)


def rebuild():
    reader = PdfReader(ARCHITECTURE)
    if any("Final Design Correction" in (page.extract_text() or "") for page in reader.pages):
        return
    writer = PdfWriter()
    writer.append(PdfReader(CORRECTION))
    writer.append(reader)
    temporary = ARCHITECTURE.with_suffix(".rebuilt.pdf")
    with temporary.open("wb") as output:
        writer.write(output)
    temporary.replace(ARCHITECTURE)


if __name__ == "__main__":
    create_correction()
    rebuild()
