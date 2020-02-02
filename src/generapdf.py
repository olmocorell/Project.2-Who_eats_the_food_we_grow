from fpdf import FPDF
titulo = "Informe de producción de alimentos en España"

def creaPDF2():
    pdf2 = FPDF('P','mm','A4')
    pdf2.add_page()
    pdf2.set_font('Arial', 'B', 16)
    pdf2.cell(190, 10, f"{titulo}",1,1,'C')
    pdf2.set_font('Courier', '',10)
    pdf2.cell(190, 10, 'Datos de la Organización de las Naciones Unidas para la Agricultura y la Alimentación','',1,'C')
    pdf2.text(10,110,'En los siguientes gráficos vemos la evolución de producción de producto y de población')
    pdf2.image('portada.jpg',x=50, y=30, w=100)
    pdf2.set_font('Courier', '',13)
    pdf2.text(55,70,'¿Quién se come lo que cultivamos?')
    pdf2.image('graficodatos.png',x=5, y=73, w=100)
    pdf2.image('graficopoblacion.png', x=100, y=73,w=100)
    pdf2.set_font('Courier', '',10)
    pdf2.text(10,155,'En los siguientes gráficos vemos la evolución de producción de producto y de población')
    pdf2.image('graficodatosbonus.png',x=5, y=160, w=100)
    pdf2.image('graficopoblacionbonus.png', x=100, y=160,w=100)
    pdf2.output("archivo.pdf")