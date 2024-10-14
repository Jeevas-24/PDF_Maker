from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    # set the header
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=24, txt=row['Topic'], ln=1, align='L', border=0)
    pdf.line(x1=10, y1=27,x2=200,y2=27)

    pdf.ln(252)

    # set footer text
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], ln=1, align='R', border=0)

    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(277)
        # set footer text
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], ln=1, align='R', border=0)

pdf.output('output.pdf')
