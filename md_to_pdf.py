import markdown
import pdfkit

# Read the Markdown file
with open('cv.md', 'r', encoding='utf-8') as md_file:
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
pdfkit.from_string(html_content, 'cv.pdf', options=options)