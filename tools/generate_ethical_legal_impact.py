from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = Path(__file__).resolve().parents[1] / "docs" / "ethical-legal-impact.pdf"
NAVY = colors.HexColor("#2C3E50")
GREY = colors.HexColor("#F4F6F8")


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
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=13, firstLineIndent=-9, bulletIndent=0, spaceAfter=4)

    story = [
        Spacer(1, 0.7 * cm), p("Ethical and Legal Impact", title),
        Table([[""]], colWidths=[17.6 * cm], style=TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.6, colors.HexColor("#222222"))])),
        Spacer(1, 8), p("This is the ethical and legal part of the combined statement of social, ethical, legal, global and security impact.", subtitle),
        section("Purpose and scope", h), Spacer(1, 9),
        p("This section assesses the ethical and legal implications of the phase-one Itqan design. It is a design review, not legal advice or a declaration of legal compliance. The assessment reflects the documented system decisions: managed external identity, an auditable consent record, in-memory recitation analysis with no retained audio, and teacher class enrolment through a join code.", body),
        p("The central question is not only whether the platform can identify recitation errors. It is whether it can do so without turning a learner’s voice, religious practice, or school progress into a source of avoidable surveillance, embarrassment, or unfair decision-making. The system design therefore has to be evaluated together with the way it will be operated by schools, teachers, and external service providers.", body),
        section("1. Ethical impact", h), Spacer(1, 9),
        p("Learner wellbeing and feedback quality", h3),
        p("Recitation feedback can affect a learner’s confidence, particularly when it concerns a religious practice. The platform should present AI output as guidance rather than a judgement of ability or religious worth. It should avoid punitive automated outcomes, explain confidence where practical, and let a learner repeat an attempt or seek teacher clarification when feedback is uncertain.", body),
        p("A technically correct prediction can still be harmful when it is expressed without context. Feedback should distinguish a detected pronunciation pattern from a final religious ruling, use supportive language, and avoid public ranking of learners by mistakes. Where the system cannot produce a reliable result, the ethical response is to say so rather than manufacture certainty.", body),
        p("Agency, transparency, and teacher access", h3),
        p("Learners need clear, Arabic-first explanations of what is collected, why it is used, and what an AI result means. Teacher dashboards should expose only the information needed for teaching. A class join code is an enrolment mechanism, not proof of informed consent or guardian authorisation; code sharing should be limited and revocable.", body),
        p("The platform should not make a learner dependent on an opaque score. A learner needs a route to understand an error, retry the exercise, and ask a teacher for help. Teachers should be able to treat the result as one learning signal among others, rather than as an automatic measure of competence or effort.", body),
        p("Children and power imbalance", h3),
        p("Where users are minors, the school or deploying organisation must establish a verified guardian-consent and safeguarding process before collecting evaluation data or enabling teacher access. That requirement is intentionally not represented as already solved by the current data model.", body),
        p("Children may feel unable to refuse collection when an activity is introduced through a school or teacher. Consent material must therefore be understandable, separate from ordinary classroom access where required, and supported by a clear escalation path. A join code should not be distributed as if it were a substitute for a safeguarding decision.", body),
        p("Stewardship of Qur’anic content", h3),
        p("The Qur’anic text must be presented accurately and respectfully. Content provenance, source attribution, and review of display or annotation changes are essential. Automated feedback should be framed as technical learning assistance, with qualified human instruction remaining available for material disputes.", body),
        p("This also means avoiding product language that treats sacred content merely as training data. Any correction rules, transliterations, or visual highlights should be reviewed for accuracy and cultural appropriateness. The team should preserve a clear link from displayed material back to its authorised source and record which version is in use.", body),
        section("2. Legal and data-protection impact", h), Spacer(1, 9),
        p("Personal data and consent", h3),
        p("Saudi Arabia’s Personal Data Protection Law (PDPL) gives individuals rights to be informed, access their personal data, request correction, request destruction in applicable cases, and withdraw consent. Itqan’s <b>CONSENT_RECORD</b> should retain the purpose, version, method, grant/withdrawal status, and timestamp required to demonstrate the user’s choice. Privacy notices and product workflows must make those rights actionable, not merely documented.", body),
        p("For Itqan, personal data can include account identifiers, class membership, progress records, error history, and technical information associated with a learner. The legal analysis must look beyond the database schema: a privacy notice, support process, analytics configuration, and staff access practice can each determine whether the right level of protection is achieved in practice.", body),
        p("Data minimisation and retention", h3),
        p("The current architecture reduces sensitivity by using managed identity (<b>identity_subject</b>) rather than locally stored password hashes and by discarding recitation audio after in-memory analysis. The operational policy must match the design: no audio recordings, raw voice samples, or debug logs containing them should be retained. Retention periods for accounts, consent records, progress data, and backups still need approval and implementation.", body),
        p("Data minimisation should also guide future features. A request to keep recordings for teacher review, train an AI model, or create a public showcase would change the nature of the data being handled and require a new assessment before implementation. It should not be treated as a small extension of the current no-retention design.", body),
        p("External processing and transfers", h3),
        p("If an external AI analysis provider processes personal data outside Saudi Arabia, deployment must not begin until the organisation has completed a PDPL transfer assessment and implemented the required safeguard or lawful mechanism. Data-processing agreements, the provider’s retention terms, and the location of processing must be reviewed before release.", body),
        p("The team must know whether the provider receives only a temporary stream or also metadata, whether it uses customer inputs for model improvement, and how deletion is verified. The same review applies to managed identity, error monitoring, analytics, and backup services. A vendor’s claim of security does not remove the deploying organisation’s responsibility to understand the processing arrangement.", body),
        p("Content and model licensing", h3),
        p("Before public release, the team must confirm permission, attribution, and applicable terms for Qur’anic source material, reciter references, AI models, datasets, and third-party services. Referencing a source does not by itself establish redistribution rights.", body),
        p("Model and dataset licences need particular care because an academic prototype can move into a public product quickly. The team must document the version, source, restrictions, and attribution requirement for every component that is bundled, hosted, or invoked through an API. If a licence is unclear, the component should not be used until the uncertainty is resolved.", body),
        section("3. Operational accountability", h), Spacer(1, 9),
        p("Access, governance, and review", h3),
        p("Ethical safeguards work only when somebody is responsible for operating them. The deploying organisation should define who can view class progress, who can respond to a learner or guardian request, who approves a new external provider, and who can change retention settings. Access should follow the least-privilege principle: a teacher needs the information required for teaching, while administrators need only the information required for support and governance.", body),
        p("This is particularly important where a school uses shared devices or a teacher has multiple classes. The product should not expose one class to another, and an old teacher relationship should not continue to give access after the class ends. Periodic access review is a practical legal and ethical control, not merely an administrative task.", body),
        p("Incident response and honest communication", h3),
        p("A no-audio-retention design reduces risk but does not remove it. Account data, consent history, progress records, and vendor configuration can still be exposed or misused. Before deployment, the team needs a documented incident route: how a concern is reported, who assesses it, how affected people are informed when required, and how the cause is corrected. The route should be tested with a simple scenario rather than written and forgotten.", body),
        p("The platform should also communicate limitations honestly. If the AI analysis is unavailable, uncertain, or unsuitable for a particular recitation pattern, the learner should receive a clear message and a safe fallback. Hiding uncertainty can create both an ethical harm and an inaccurate record of learning progress.", body),
        p("Fairness, accessibility, and evaluation", h3),
        p("The team should evaluate whether feedback quality changes across age groups, reading levels, devices, network conditions, and recognised recitation styles. A model that works well for one group but repeatedly flags another group unfairly can amplify disadvantage even if it has a good overall accuracy score. Evaluation needs representative, lawfully sourced data and review by knowledgeable educators.", body),
        p("Accessibility is part of the same responsibility. Instructions, consent material, error explanations, and teacher-facing controls should remain understandable for users with different levels of digital literacy. A learner who cannot understand why a result was produced cannot meaningfully challenge or learn from it.", body),
        p("Change control", h3),
        p("Privacy and ethical impact should be reassessed when the purpose or data flow changes. Retaining recordings, adding biometric features, training a model on learner interactions, sharing analytics with a partner, or changing from join-code enrolment to another flow are material changes. Each must be reviewed before release, with the relevant notices, consent process, retention rule, and architecture documentation updated together.", body),
        p("This discipline prevents an initially narrow prototype from becoming a broader surveillance system by accident. It also gives the team a clear decision point: a feature that cannot be justified, protected, and explained should not be deployed merely because it is technically possible.", body),
        section("4. Design controls and remaining obligations", h), Spacer(1, 9),
    ]
    rows = [
        [p("Area", small), p("Current design control", small), p("Required before deployment", small)],
        [p("Identity", small), p("Managed identity provider; no local password hash.", small), p("Confirm provider contract, access controls, and privacy notice.", small)],
        [p("Consent", small), p("CONSENT_RECORD captures purpose, version, method, status, and withdrawal.", small), p("Implement consent UI, withdrawal workflow, and rights-request handling.", small)],
        [p("Recitation data", small), p("Audio is analysed in memory and not stored.", small), p("Verify logs, monitoring, backups, and vendors do not retain audio.", small)],
        [p("Classes", small), p("Join code supports enrolment without invitation links.", small), p("Protect code disclosure; establish verified guardian/school process for minors.", small)],
        [p("AI service", small), p("External analysis may be used for feedback.", small), p("Complete transfer, vendor, accuracy, and human-escalation review.", small)],
        [p("Qur’anic content", small), p("Source provenance is documented.", small), p("Validate attribution, terms, and release permissions.", small)],
    ]
    table = Table(rows, colWidths=[3.0 * cm, 6.0 * cm, 7.0 * cm], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B9C5D1")),
        ("BACKGROUND", (0, 1), (-1, -1), GREY), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [GREY, colors.white]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [table, section("5. Conclusion", h), Spacer(1, 9),
              p("Itqan’s phase-one choices reduce several major risks: it avoids local passwords, keeps a consent history, and does not retain recitation audio. These controls are not sufficient on their own for deployment. The open obligations above—especially minors’ safeguarding, operational deletion controls, vendor/transfer review, and content licensing—must be completed before handling real learner data.", body),
              section("References", h), Spacer(1, 9),
              p("Saudi Data & AI Authority (SDAIA), <i>Personal Data Protection Law and Regulations</i>: https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx", small),
              p("SDAIA, <i>Data Subject Rights under the PDPL</i>: https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPLCP/", small),
              p("SDAIA, <i>Standard Contractual Clauses for Personal Data Transfer</i>: https://sdaia.gov.sa/Documents/StandardContractualClausesForPersonalDataTransferEN.pdf", small),
              p("King Fahd Glorious Qur’an Printing Complex, <i>Vision</i>: https://qurancomplex.gov.sa/en/kfgqpc/vision/", small),
              Spacer(1, 7), p("Prepared for the Itqan graduation project. Legal applicability and compliance decisions require review by the deploying organisation and qualified legal counsel.", small)]

    doc.build(story)


if __name__ == "__main__":
    main()
