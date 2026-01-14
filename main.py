from fpdf import FPDF
pdf=FPDF(orientation='P',unit='pt',format='A4')
pdf.add_page()
pdf.image('tiger.jpeg',w=80,h=50)
pdf.set_font(family='Times',style='B',size=24,align="C")
pdf.cell(w=0,h=50,txt="Malayan Tiger")
pdf.output('output.pdf')