from weasyprint import HTML, CSS

html_template = get_template('pdf.html')
rendered_html = html_template.render(RequestContext(request, {
    'State': 'ok',
    'RefNum': RefNum,
    'ResNum': ResNum,
    'factor': factor,
    'pCost': pCost,
    'totalCost': totalCost,
    'totalPrice': totalPrice,
    'newOrder': newOrder,
})).encode(encoding="UTF-8")

pdf_file = HTML(string=rendered_html).write_pdf(stylesheets=[
    CSS(settings.STATIC_ROOT + '/css/style.css'),
    CSS(settings.STATIC_ROOT + '/css/fonts.min.css'),
])

# to write
result = open('media/invoices/inv-' + str(newOrder.id) + '.pdf', 'wb')
result.write(pdf_file)
result.close()
