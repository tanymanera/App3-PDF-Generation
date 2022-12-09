from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)	# size è in pt e non in mm (?)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
    pdf.line(x1=10, y1=22, x2=200, y2=22)   # A4 is 210 mm width

    for page in range(row['Pages'] - 1):
        pdf.add_page()

pdf.output('output.pdf')