from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = Path(__file__).resolve().parents[1] / "docs" / "social-global-impact.pdf"
NAVY = colors.HexColor("#2C3E50")


def p(text, style):
    return Paragraph(text, style)


def section(text, style):
    table = Table([[p(text, style)]], colWidths=[17.6 * cm])
    table.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.8, colors.HexColor("#A7A7A7")),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    return table


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=1.7 * cm, leftMargin=1.7 * cm,
                            topMargin=1.5 * cm, bottomMargin=1.5 * cm)
    styles = getSampleStyleSheet()
    title = ParagraphStyle("Title", parent=styles["Title"], fontName="Times-Bold", fontSize=22,
                           leading=26, textColor=colors.HexColor("#222222"), alignment=0, spaceAfter=12)
    subtitle = ParagraphStyle("Subtitle", parent=styles["Normal"], fontName="Times-Italic", fontSize=11,
                              leading=15, textColor=colors.HexColor("#4A4A4A"), spaceAfter=19)
    h = ParagraphStyle("Heading", parent=styles["Heading2"], fontName="Times-Bold", fontSize=14,
                       leading=17, textColor=colors.HexColor("#222222"), spaceBefore=14, spaceAfter=0)
    h3 = ParagraphStyle("Heading3", parent=styles["Heading3"], fontName="Times-Bold", fontSize=11,
                        leading=14, textColor=colors.HexColor("#1A1A1A"), spaceBefore=9, spaceAfter=3)
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Times-Roman", fontSize=11,
                          leading=15.5, spaceAfter=10, textColor=colors.HexColor("#1A1A1A"))
    small = ParagraphStyle("Small", parent=body, fontSize=8.5, leading=11, spaceAfter=3)

    story = [
        Spacer(1, 0.7 * cm), p("Social and Global Impact", title),
        Table([[""]], colWidths=[17.6 * cm], style=TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.6, colors.HexColor("#222222"))])),
        Spacer(1, 8), p("This is the social and global part of the combined statement of social, ethical, legal, global and security impact.", subtitle),
        section("Purpose and scope", h), Spacer(1, 9),
        p("This section considers how phase-one Itqan may affect learners, teachers, families, and wider communities. Itqan is an AI-assisted Qur’an recitation learning platform: it provides guided practice, feedback, progress information, teacher-class support, and source-aware Qur’anic content. Its impact depends as much on access, language, and classroom use as on technical accuracy.", body),
        p("The analysis avoids claiming that software alone solves an educational or social need. The platform can support practice and extend access to structured feedback, but it cannot replace a qualified teacher, a supportive family environment, or an inclusive learning setting. Success means improving learning opportunities without creating a new barrier for learners who have less connectivity, confidence, or digital access.", body),
        section("1. Social impact", h), Spacer(1, 9),
        p("Supporting practice between lessons", h3),
        p("Itqan can give learners an opportunity to practise recitation outside a scheduled lesson and receive immediate, structured feedback. That may be particularly useful where a teacher has limited time with each learner or where a learner is reluctant to make mistakes in front of a group. Progress history can help a learner see improvement over time rather than treating one imperfect attempt as failure.", body),
        p("The social value comes from practice being more available, not from replacing human teaching. Teacher review, encouragement, and context remain essential. The product should therefore describe itself as a learning aid and make it easy for a teacher to interpret results alongside observation, not as a system that assigns a final ability label.", body),
        p("Language, culture, and belonging", h3),
        p("Arabic-first interaction is important because the platform concerns Qur’anic learning and is intended for users who may prefer Arabic explanations. Labels, feedback, help content, and consent material should be understandable in the learner’s language rather than relying on a translated technical interface. Clear wording also reduces the risk that an error message is experienced as criticism of the learner or of their religious identity.", body),
        p("Respectful presentation of Qur’anic material contributes to cultural continuity. Source attribution and accurate text presentation allow learners to connect the digital experience to trusted scholarship rather than to an anonymous automated system. The product must not present a single technical output as more authoritative than qualified instruction or established recitation practice.", body),
        p("Teacher and family relationships", h3),
        p("Class features can support teachers by showing patterns that may deserve attention, such as a repeated difficulty with an exercise. They should not create a pressure to monitor every learner continuously. A useful dashboard prioritises teaching actions, minimises unnecessary comparison, and avoids public leaderboards that can shame a learner who is progressing more slowly.", body),
        p("Family involvement can be positive when it encourages practice, but the product should not assume every learner has equal support at home. Where minors use the platform, schools and families need an agreed safeguarding and communication process. A class join code enables enrolment; it does not prove that a guardian has understood the data use or agreed to it.", body),
        p("Inclusion and the digital divide", h3),
        p("A digital learning tool can widen inequality if it assumes that every household has a recent device, reliable connectivity, private space to practise, or a digitally confident adult. The platform should remain usable on common devices, avoid unnecessary bandwidth use, and provide a clear fallback when analysis cannot run. Schools should avoid making home access a hidden requirement for participation or assessment.", body),
        p("Inclusion also includes learners with different reading needs, levels of Arabic literacy, and confidence with technology. Short instructions, meaningful error explanations, consistent controls, and teacher-supported alternatives make the benefit more evenly available. Usage data should never be used to infer that a learner is less committed simply because they have fewer opportunities to connect.", body),
        section("2. Global impact", h), Spacer(1, 9),
        p("Contribution to inclusive learning", h3),
        p("The United Nations Sustainable Development Goal 4 calls for inclusive and equitable quality education and recognises that access gaps connected to location, income, disability, and connectivity remain significant. Itqan can contribute in a limited but practical way by making structured practice material and feedback more portable. It should make that contribution without claiming to solve wider educational inequality.", body),
        p("A global-ready product is not simply one that can be opened in many countries. It must be understandable across different educational settings, account for unequal access to devices and networks, and avoid assuming that one classroom practice is universal. Deployment beyond the original context should be gradual, with local educator input rather than a one-size-fits-all rollout.", body),
        p("Cultural reach and local adaptation", h3),
        p("Qur’anic learning connects communities across countries, languages, and educational traditions. That reach creates an opportunity to support learners who do not have easy access to structured practice, but it also creates a responsibility to avoid flattening cultural differences. Examples, terminology, explanatory content, and feedback language should be reviewed with educators familiar with the intended community.", body),
        p("The system should be designed for adaptation without silently changing the underlying content source or feedback rules. A localised interface must preserve provenance and make clear what has changed: language, examples, teaching guidance, or the technical model. Where the platform cannot support a local requirement reliably, it should say so rather than imply universal suitability.", body),
        p("Environmental and operational footprint", h3),
        p("The platform’s direct environmental impact is modest at prototype scale, but AI analysis, cloud hosting, and repeated media processing still consume energy. The existing decision not to store recitation audio reduces storage demand and unnecessary duplication. Efficient processing, sensible retry limits, and avoiding collection that is not needed for learning are practical ways to keep the system proportionate as it grows.", body),
        p("Global operation also creates dependency on external platforms. Managed identity and external analysis can improve reliability, but they can create outages, cost changes, and cross-border data concerns. The product should retain clear ownership of its core learning records, document each dependency, and communicate service limitations rather than hiding them from schools or learners.", body),
        section("3. Responsible deployment", h), Spacer(1, 9),
        p("Evidence before broad claims", h3),
        p("Before promoting Itqan as improving outcomes, the team should test it with representative learners and educators. Evaluation should look beyond technical error detection to questions such as: Does it help a learner practise with more confidence? Can teachers understand the feedback? Does it create a disadvantage for learners with poorer devices or networks? The answers should guide improvement and should not be inferred from usage counts alone.", body),
        p("Any research activity involving children, classroom data, or recorded interactions needs its own ethics and consent process. Academic evaluation is not automatically covered by ordinary product enrolment. The team should publish only aggregated, non-identifying findings and should avoid presenting early prototype results as evidence of broad social benefit.", body),
        p("Community accountability", h3),
        p("Feedback from learners, teachers, parents, and qualified Qur’an educators should be treated as part of the product’s quality process. A simple route to report confusing feedback, cultural concerns, or accessibility barriers gives affected people a way to influence the system. Reports should be reviewed, categorised, and linked to a decision rather than collected without response.", body),
        p("The strongest global posture is humility: deploy where the team can provide support, listen to local feedback, and correct problems. Expansion should pause if the platform cannot safeguard learners, explain its data practices, or obtain appropriate educational and cultural review in the new context.", body),
        section("4. Design controls and remaining obligations", h), Spacer(1, 9),
    ]
    rows = [
        [p("Area", small), p("Potential contribution", small), p("Required before deployment", small)],
        [p("Learning practice", small), p("Guided practice and feedback between lessons.", small), p("Keep teacher review and a learner retry/escalation path.", small)],
        [p("Language and culture", small), p("Arabic-first, source-aware learning experience.", small), p("Review wording and content with qualified educators.", small)],
        [p("Access", small), p("Portable support on common devices.", small), p("Test low-bandwidth and school-supported alternatives.", small)],
        [p("Classes", small), p("Teacher insight into practice patterns.", small), p("Avoid ranking; protect code sharing and minor safeguarding.", small)],
        [p("Global use", small), p("Potential access across communities.", small), p("Use local review and validate language, data, and support needs.", small)],
        [p("Evaluation", small), p("Evidence for iterative improvement.", small), p("Obtain separate ethics approval and publish aggregate findings only.", small)],
    ]
    table = Table(rows, colWidths=[3.0 * cm, 6.0 * cm, 7.0 * cm], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B9C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F4F6F8"), colors.white]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [table, section("5. Conclusion", h), Spacer(1, 9),
              p("Itqan can support more flexible, respectful Qur’an recitation practice, but the benefit is conditional. It must remain accessible, Arabic-first, teacher-supported, culturally accountable, and honest about its limitations. The design choices that reduce data collection and avoid automatic judgement are also social choices: they help keep the platform focused on learning rather than surveillance or ranking.", body),
              section("References", h), Spacer(1, 9),
              p("United Nations, <i>Sustainable Development Goal 4: Quality Education</i>: https://sdgs.un.org/goals/goal4", small),
              p("UNESCO Global Education Monitoring Report, <i>Technology in Education</i>: https://www.unesco.org/gem-report/en/publication/technology", small),
              p("King Fahd Glorious Qur’an Printing Complex, <i>Vision</i>: https://qurancomplex.gov.sa/en/kfgqpc/vision/", small),
              Spacer(1, 7), p("Prepared for the Itqan graduation project. This assessment describes intended impacts and deployment conditions; it does not claim measured educational outcomes.", small)]
    doc.build(story)


if __name__ == "__main__":
    main()
