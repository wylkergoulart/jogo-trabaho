from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Modelo do banco de dados
class PollutionReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image_filename = db.Column(db.String(100))


# Rota para exibir o formulário de relatório de poluição
@app.route('/report_pollution', methods=['GET'])
def report_pollution_form():
    return render_template('report_pollution.html')


# Rota para processar o envio do relatório de poluição
@app.route('/submit_report', methods=['POST'])
def submit_report():
    location = request.form['location']
    description = request.form['description']
    image = request.files.get('image')

    image_filename = None
    if image:
        image_filename = image.filename
        image.save(os.path.join('static/images', image_filename))  # Salva a imagem em um diretório estático

    # Cria um novo relatório de poluição
    report = PollutionReport(location=location, description=description, image_filename=image_filename)
    db.session.add(report)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Relatório de poluição enviado com sucesso!'})


# Rota para listar todos os relatórios
@app.route('/reports', methods=['GET'])
def list_reports():
    reports = PollutionReport.query.all()
    return jsonify(
        [{'id': r.id, 'location': r.location, 'description': r.description, 'image_filename': r.image_filename} for r in
         reports])


if __name__ == '__main__':
    db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
