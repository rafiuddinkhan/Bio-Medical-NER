from flask import Flask, request, jsonify
from bio_medical_ner_parser import BioMedicalParser 

import logging


# Configure logging
logging.basicConfig(filename='bio_medical_ner.log', level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


app = Flask(__name__)

bio_medical_parser = BioMedicalParser()


@app.route('/health', methods=['GET'])
def health_check():
    #Is api active
    status = {'status': 'Bio-Medical-NER API is Live'}
    return jsonify(status), 200

@app.route('/bio-medical-ner/query', methods=['POST'])
def handle_bio_medical_ner_query():
    try:
        query = request.form.get('input_text')
        response=bio_medical_parser.extract_biomedical_entities(query)
        return jsonify({'response': response})
    except Exception as e:
        app.logger.error(f'Error handling query: {str(e)}')
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0",port=5000)
