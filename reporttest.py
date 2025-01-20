from reportlab.lib import colors
from reportlab.lib.units import inch, cm, mm
from reportlab.platypus import Image
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Table, 
    TableStyle, 
    Paragraph, 
    PageBreak
)
from reportlab.platypus.flowables import Spacer
from reportlab.lib.styles import getSampleStyleSheet


def header(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 10)
    header_text = "FarmSetu"
    text_width = canvas.stringWidth(header_text, "Helvetica", 10)
    canvas.drawString((A4[0] - text_width) / 2, A4[1] - 0.7 * cm, header_text)
    
    left_header_text = "SPDS"
    canvas.drawString(1 * cm, A4[1] - 0.7 * cm, left_header_text)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 10)
    footer_text = "FarmSetu"
    footer_width = canvas.stringWidth(footer_text, "Helvetica", 10)
    canvas.drawString((A4[0] - footer_width) / 2, 0.7 * cm, footer_text)

    left_footer_text = "TSP"
    canvas.drawString(1 * cm, 0.7 * cm, left_footer_text)

    page_number = f"{doc.page}"
    canvas.drawString(A4[0] - 1 * cm, 0.7 * cm, page_number)
    canvas.restoreState()


def add_page_decorations(canvas, doc):
    header(canvas, doc)
    footer(canvas, doc)


def Smart_Path_Delivery_report_pdf():
    doc = BaseDocTemplate(
        "Smart_Path_Delivery_Report.pdf",
        pagesize=A4,
    )

    frame = Frame(
        2 * cm, 2.5 * cm, A4[0] - 4 * cm, A4[1] - 5 * cm
    )

    template = PageTemplate(id="report_template", frames=frame, onPage=add_page_decorations)
    doc.addPageTemplates([template])

    styles = getSampleStyleSheet()
    paragraph_style = styles['Normal']
    paragraph_style.firstLineIndent = 40
    paragraph_style.leftIndent = 10
    paragraph_style.fontSize = 14

    paragraph1 = Paragraph(
        "This is a report on the smart path delivery system. "
        "This system, likely employing a sophisticated route optimization algorithm, aims to streamline the delivery process by identifying "
        "the most efficient path for a vehicle or courier to traverse multiple destinations. It considers various factors such as distance, "
        "traffic conditions, delivery time windows, and any specific constraints or requirements. By calculating the shortest possible route, "
        "the system minimizes travel time and fuel consumption, leading to significant cost savings and improved operational efficiency. "
        "Moreover, ensuring all destinations are visited guarantees that no deliveries are missed, while the return to the starting point "
        "optimizes the overall journey and allows for efficient resource allocation and scheduling. This type of system is particularly valuable "
        "for businesses with large delivery fleets or those operating in complex urban environments where efficient route planning is crucial "
        "for success. Key aspects highlighted in the paragraph: Route Optimization: The core function of the system is to determine the most efficient path. "
        "Multi-location Delivery: The system caters to scenarios involving multiple delivery points. Shortest Path: The primary objective is to minimize the total distance or travel time. "
        "Delivery Requirements: The system accounts for specific constraints like time windows, delivery priorities, and any special instructions. "
        "Complete Coverage: Ensures all destinations are visited, preventing missed deliveries. Return to Origin: Optimizes the overall journey by returning to the starting point. "
        "Benefits: Cost savings, improved efficiency, optimized resource allocation. Applications: Valuable for businesses with large delivery fleets or those operating in complex environments. "
        "This system has the potential to revolutionize logistics and delivery operations by significantly enhancing efficiency and reducing costs.",
        paragraph_style
    )

    data = [
        ["Vehicle No", "Capacity", "Vehicle Path", "Carrying Weight", "Remaining Weight", "Total Route Distance"],
        ["VH008", "1000", " ORD010 → ORD015 → \n ORD024 → ORD008 ", "999", "1", "646.24 km"],
        ["VH005", "400", " ORD003 ", "400", "0", "84.06 km"],
        ["VH006", "500", " ORD015 → ORD014 → ORD025", "420", "80", "210.16 km"],
        ["VH004", "600", " ORD001 ", "600", "0", "142.38 km"],
        ["VH001", "800", " ORD012 → ORD021 → ORD019 ", "800", "0", "801.60 km"],
        ["VH003", "1000", " ORD009 → ORD016 →ORD005 ", "990", "10", "323.75 km"],
        ["VH002", "1200", " ORD002 → ORD004 → ORD013 \n → ORD027 → ORD006 ", "1160", "40", "648.08 km"],
        ["VH007", "800", "ORD011 → ORD007 ", "760", "40", "114.04 km"]
    ]

    col_widths = [60, 50, 160, 90, 90, 110]

    table = Table(data, colWidths=col_widths)
    style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),     
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),       
    ('FONTSIZE', (0, 0), (-1, -1), 10),                
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),             
    ('GRID', (0, 0), (-1, -1), 1, colors.black),       
    ])

    table.setStyle(style)

    images = [
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-17 104955.png", width=6*cm, height=4*cm),
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-17 004504.png", width=6*cm, height=4*cm),
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-16 170815.png", width=6*cm, height=4*cm),
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-16 170718.png", width=6*cm, height=4*cm),
    ]

    image_data = [
        [images[0], images[1]],
        [images[2], images[3]],
    ]
    image_table = Table(image_data, colWidths=9 * cm, rowHeights=6 * cm)

    styles = getSampleStyleSheet()
    paragraph_style = styles['Normal']
    paragraph_style.firstLineIndent = 40
    paragraph_style.leftIndent = 10
    paragraph_style.fontSize = 14

    paragraph2 = Paragraph(
        "Hi My name is Sumeet Shinde, Welcome to Smart_Path_Delivery Report",
        paragraph_style
    )

    elements = [
        paragraph1,
        Spacer(1, 10* cm),
        table,
        Spacer(1, 0.5 * cm),
        PageBreak(),
        image_table,
        PageBreak(),
        paragraph2
    ]

    doc.build(elements)

if __name__ == '__main__':
    Smart_Path_Delivery_report_pdf()

