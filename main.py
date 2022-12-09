from fpdf import FPDF
import pandas as pd
from element import footer, make_lines

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)	# size è in pt e non in mm (?)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
    make_lines(pdf)
    footer(pdf, row['Topic'])

    for page in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=24)	# size è in pt e non in mm (?)
        pdf.cell(w=0, h=12, align="L", ln=1, border=0)
        make_lines(pdf)
        footer(pdf, row['Topic'])

pdf.output('output.pdf')