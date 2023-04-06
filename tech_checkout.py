import PyPDF2
from fpdf import FPDF
import sys, os
from excel_utils import write_to_excel

student_name = ''
grade = ''
school = 'FA'
student_no = ''
homeroom_teacher = ''

if len(sys.argv) > 1:
    i = 1
    i = i+1 if sys.argv[0] == 'Name' else 2
    
    last_name = ''
    while sys.argv[i][-1] != ',':
        last_name += sys.argv[i] + ' '
        i += 1
    last_name += sys.argv[i][0:-1]
    i += 1
    student_name = f"{sys.argv[i]} {last_name}"

    for x in range(i+1, len(sys.argv) - 1):
        if sys.argv[x] == 'Grade:':
            x += 1
            grade = sys.argv[x]

        if sys.argv[x] == 'No:':
            x += 1
            student_no = sys.argv[x]

        if sys.argv[x] == 'Teacher:':
            if sys.argv[x+1][-1] == '~':
                homeroom_teacher = sys.argv[x+1] + ' ' + sys.argv[x+2][0:-1]
            else:
                homeroom_teacher = sys.argv[x+1] + ' ' + sys.argv[x+2]
            break

asset_id = input('Enter Asset ID: ')

# Creating a PDF w/FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=11)

pdf.text(40,73, student_name)
pdf.text(130,73, student_no)
pdf.text(35,83, 'FA')
pdf.text(93,83, homeroom_teacher)
pdf.text(160,83, grade)
pdf.text(29, 280, asset_id)

pdf.output("filled_form.pdf")

# Where we merge both PDFs together with PyPDF2
checkout_form = open('Tech Checkout.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(checkout_form)
checkout_form_first_page = pdfReader.getPage(0)

created_pdf = open('filled_form.pdf', 'rb')
pdfStudentInfoReader = PyPDF2.PdfFileReader(created_pdf)
checkout_form_first_page.mergePage(pdfStudentInfoReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(checkout_form_first_page)

filleCheckoutForm = open('tech_filled_form.pdf', 'wb')
pdfWriter.write(filleCheckoutForm)

# Write data to Excel
data = [student_no, student_name, 'FA', homeroom_teacher, grade, asset_id]
write_to_excel('student_info.xlsx', 'Student Info', data)

# Clean up
checkout_form.close()
filleCheckoutForm.close()
created_pdf.close()
os.remove(os.path.abspath('filled_form.pdf'))
