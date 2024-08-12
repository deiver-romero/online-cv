import markdown
import pdfkit

def generate_pdf_from_markdown(md_file_path, pdf_file_path):
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Define options for PDF generation
    options = {
        'page-size': 'A4',
        'margin-top': '10mm',
        'margin-right': '10mm',
        'margin-bottom': '10mm',
        'margin-left': '10mm',
        'encoding': "UTF-8",
    }

    # Convert HTML to PDF
    pdfkit.from_string(html_content, pdf_file_path, options=options)

# Generate PDFs for both English and Spanish CVs
generate_pdf_from_markdown('cv.md', 'cv.pdf')
generate_pdf_from_markdown('cv-es.md', 'cv-es.pdf')