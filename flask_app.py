from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Путь к папке со PDF
    pdf_dir = os.path.join(app.root_path, 'static', 'pdfs')

    # Список документов (имя и URL — задаёте вручную)
    documents = [
        {
            'name': 'Расписание заплывов',
            'pdf_url': '/static/pdfs/ScheduleList.pdf'
        },
        {
            'name': 'Стартовые протоколы 1-й день',
            'pdf_url': '/static/pdfs/StartList_1.pdf'
        },
        {
            'name': 'Итоговые протоколы 1-й день',
            'pdf_url': '/static/pdfs/ResultList_1.pdf'
        },
        {
            'name': 'Стартовые протоколы 2-й день',
            'pdf_url': '/static/pdfs/StartList_2.pdf'
        },
        {
            'name': 'Итоговые протоколы 2-й день',
            'pdf_url': '/static/pdfs/ResultList_2.pdf'
        },
        {
            'name': 'Стартовые протоколы 3-й день',
            'pdf_url': '/static/pdfs/StartList_3.pdf'
        },
        {
            'name': 'Итоговые протоколы 3-й день',
            'pdf_url': '/static/pdfs/ResultList_3.pdf'
        },
        {
            'name': 'Стартовые протоколы 4-й день',
            'pdf_url': '/static/pdfs/StartList_4.pdf'
        },
        ###{
        ###    'name': 'Итоговые протоколы 4-й день',
        ###    'pdf_url': '/static/pdfs/ResultList_4.pdf'
        ###},
        ###{
        ###    'name': 'Итоговые протоколы за все дни',
        ###    'pdf_url': '/static/pdfs/ResultList.pdf'
        ###}
    ]

    # Проверяем, существуют ли файлы
    for doc in documents:
        local_path = os.path.join(pdf_dir, os.path.basename(doc['pdf_url']))
        doc['exists'] = os.path.isfile(local_path)

    return render_template('index.html', documents=documents)

if __name__ == '__main__':
    app.run(debug=True)


