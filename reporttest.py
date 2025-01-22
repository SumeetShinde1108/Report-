from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Table, 
    TableStyle,
    Image, 
    Paragraph, 
    PageBreak
)
from reportlab.lib.colors import Color 
from reportlab.platypus.flowables import Spacer
from reportlab.lib.styles import getSampleStyleSheet


def header(canvas, doc):
    """Draws the header on each page with a title, left-aligned text, and logos on both sides."""
    canvas.saveState()
    canvas.setFont("Helvetica", 10)

    # Centered header title
    header_text = "FarmSetu Technologies"
    text_width = canvas.stringWidth(header_text, "Helvetica", 10)
    
    # Draws centered text 0.7 cm below the top edge of the A4 page.
    canvas.drawString((A4[0] - text_width) / 2, A4[1] - 0.7 * cm, header_text)

    # Left-aligned logo
    logo_path = "C:\\Users\\mypc\\Downloads\\Farmsetu-Logo-full.png"
    logo = Image(logo_path, width=4 * cm, height=1.5 * cm)
    
    # Draws the logo image 1.6 cm below the top edge and 1 cm from the left edge of the A4 page.
    logo.drawOn(canvas, 1 * cm, A4[1] - 1.6 * cm)

    # Right-aligned logo
    logo_path = "C:\\Users\\mypc\\Downloads\\Farmsetu.webp" 
    logo = Image(logo_path, width=1.3 * cm, height=1.3 * cm)
    
    # Draws the logo image 1.4 cm below the top edge and 1.7 cm from the right edge of the A4 page.
    logo.drawOn(canvas, A4[0] - 1.7 * cm, A4[1] - 1.4 * cm)

    canvas.restoreState()


def footer(canvas, doc):
    """Draws the footer on each page with a title, left-aligned text, and the page number."""
    canvas.saveState()
    canvas.setFont("Helvetica", 10)

    # Centered footer text
    footer_text = "FarmSetu"
    footer_width = canvas.stringWidth(footer_text, "Helvetica", 10)

    # Draws the footer text centered at the bottom of the page, 0.7 cm above the bottom edge.
    canvas.drawString((A4[0] - footer_width) / 2, 0.7 * cm, footer_text)

    # Left-aligned footer text
    left_footer_text = "TSP"

    # Draws the left footer text ("TSP") 0.7 cm above the bottom-left corner of the page.
    canvas.drawString(1 * cm, 0.7 * cm, left_footer_text)

    # Right-aligned page number
    page_number = f"{doc.page}"

    # Draws the page number ("page_number") 0.7 cm above the bottom-right corner of the page.
    canvas.drawString(A4[0] - 1 * cm, 0.7 * cm, page_number)
    canvas.restoreState()


def watermark(canvas, doc):
    """Adds a visually appealing watermark to each page."""
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 25)  
    canvas.setFillColor(Color(0.5, 0.5, 0.5, alpha=0.3))  # Semi-transparent gray

    #for single watermark 
    """
    canvas.translate(A4[0] / 2, A4[1] / 2)
    canvas.rotate(45)
    text_width = canvas.stringWidth("CONFIDENTIAL", "Helvetica-Bold", 50)
    canvas.drawString(-text_width / 2, 0, "CONFIDENTIAL")

    canvas.restoreState()
    """

    # for multiple watermarks 
    # Define the watermark text and spacing
    watermark_text = "FARMSETU"
    text_width = canvas.stringWidth(watermark_text, "Helvetica-Bold", 25)
    text_height = 25  # Font size used as approximate text height

    # Define spacing between watermarks
    horizontal_spacing = 200  # Spacing between watermarks horizontally
    vertical_spacing = 150    # Spacing between watermarks vertically

    # Offset to start grid from center of the page
    x_offset = (A4[0] % horizontal_spacing) / 2  # Center the grid horizontally
    y_offset = (A4[1] % vertical_spacing) / 2   # Center the grid vertically

    # Loop through the page to add watermarks
    for y in range(-vertical_spacing, int(A4[1]) + vertical_spacing):
        for x in range(-horizontal_spacing, int(A4[0]) + horizontal_spacing):
            canvas.saveState()
            canvas.translate(x + x_offset, y + y_offset)  # Center starting position
            canvas.rotate(45)  # Rotate the text at an angle of 45 degrees
            canvas.drawString(-text_width / 2, -text_height / 2, watermark_text)  # Center each watermark
            canvas.restoreState()

    canvas.restoreState()


def add_page_decorations(canvas, doc):
    """Adds the header and footer to each page."""
    header(canvas, doc)
    footer(canvas, doc)
    watermark(canvas, doc)


def Smart_Path_Delivery_report_pdf():
    """Generates a PDF report for the Smart Path Delivery system with text, tables, images, and page decorations."""
    # Setting up the document with custom margins
    doc = BaseDocTemplate(
        "Smart_Path_Delivery_Report.pdf",
        pagesize=A4,
    )

    # Defining the frame with margins
    # Creates a content frame with 2 cm left/right margins, 2.5 cm top margin, and 5 cm bottom margin, to fit within the A4 page dimensions.
    frame = Frame(
        2 * cm, 2.5 * cm, A4[0] - 4 * cm, A4[1] - 5 * cm
    )

    # Adding the page template
    template = PageTemplate(id="report_template", frames=frame, onPage=add_page_decorations)
    doc.addPageTemplates([template])

    # Style setup for paragraphs
    styles = getSampleStyleSheet()
    paragraph_style = styles['Normal']
    paragraph_style.firstLineIndent = 40  # Indent the first line
    paragraph_style.leftIndent = 10       # Indent the entire paragraph
    paragraph_style.fontSize = 14         # Set font size

    # Main introductory paragraph
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


    # Table data setup
    data = [
        ["Vehicle No", "Capacity", "Vehicle Path", "Carrying Weight", "Remaining Weight", "Total Route Distance"],
        ["VH008", "1000", "ORD010 → ORD015 → \n ORD024 → ORD008", "999", "1", "646.24 km"],
        ["VH005", "400", "ORD003", "400", "0", "84.06 km"],
        ["VH006", "500", "ORD015 → ORD014 → ORD025", "420", "80", "210.16 km"],
        ["VH004", "600", "ORD001", "600", "0", "142.38 km"],
        ["VH001", "800", "ORD012 → ORD021 → ORD019", "800", "0", "801.60 km"],
        ["VH003", "1000", "ORD009 → ORD016 →ORD005", "990", "10", "323.75 km"],
        ["VH002", "1200", "ORD002 → ORD004 → ORD013 \n → ORD027 → ORD006", "1160", "40", "648.08 km"],
        ["VH007", "800", "ORD011 → ORD007", "760", "40", "114.04 km"]
    ]

    # Column widths for the table
    col_widths = [60, 50, 160, 90, 90, 110]

    # Creating the table with styling
    table = Table(data, colWidths=col_widths)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header text color
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),   # Font for entire table
        ('FONTSIZE', (0, 0), (-1, -1), 10),            # Font size
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),         # Center alignm=ent
        ('GRID', (0, 0), (-1, -1), 1, colors.black),   # Gridlines
    ])
    table.setStyle(style)

    # Images for visualization
    images = [
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-17 104955.png", width=6*cm, height=4*cm),
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-17 004504.png", width=6*cm, height=4*cm),
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-16 170815.png", width=6*cm, height=4*cm),
        Image("C:\\Users\\mypc\\Pictures\\Screenshots\\Screenshot 2025-01-16 170718.png", width=6*cm, height=4*cm),
    ]

    # Arranging images in a table
    image_data = [
        [images[0], images[1]],
        [images[2], images[3]],
    ]
    image_table = Table(image_data, colWidths=9 * cm, rowHeights=6 * cm)

    # Final paragraph
    paragraph2 = Paragraph(
        "Hi My name is Sumeet Shinde, Welcome to Smart_Path_Delivery Report",
        paragraph_style
    )

    # Adding elements to the document
    elements = [
        paragraph1,
        Spacer(1, 10 * cm),
        table,
        Spacer(1, 0.5 * cm),
        PageBreak(),
        image_table,
        PageBreak(),
        paragraph2
    ]

    # Building the document
    doc.build(elements)

if __name__ == '__main__':
    Smart_Path_Delivery_report_pdf()
