def footer(pdf, topic):
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic, align='R')

def make_lines(pdf):
    for i in range(20, 289, 10):
        pdf.line(x1=10, y1=i, x2=200, y2=i) # A4 is 210 mm width
