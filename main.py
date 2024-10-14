from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=24, txt=row['Topic'], ln=1, align='L', border=0)
    pdf.line(x1=10, y1=27,x2=200,y2=27)

pdf.output('output.pdf')
