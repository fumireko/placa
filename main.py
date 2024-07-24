from flask import Flask, jsonify, request
import json
import cloudscraper
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/api/<placa>', methods=['GET'])
def get_placa_info(placa):
    url = f"https://www.keplaca.com/placa?placa-fipe={placa}#"
    scraper = cloudscraper.create_scraper()

    try:
        response = scraper.get(url, timeout=5)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table', {'class': 'fipeTablePriceDetail'})
            if not table:
                return jsonify({'error': 'Dados nÃ£o encontrados para a placa.'}), 404

            data = {}
            for row in table.find_all('tr'):
                cols = row.find_all('td')
                key = cols[0].text.strip().replace(':', '')
                value = cols[1].text.strip()
                if key == 'Importado':
                    value = value == 'Sim'
                data[key.lower()] = value

            table_mobile = soup.find('table', {'class': 'fipe-desktop'})
            fipe_data = []
            if table_mobile:
                for row in table_mobile.find_all('tr')[1:]:
                    cols = row.find_all('td')
                    fipe_data.append({
                        'codigo_fipe': cols[0].text.strip(),
                        'modelo': cols[1].text.strip(),
                        'valor': float(cols[2].text.strip().replace('R$', '').replace('.', '').replace(',', '.'))
                    })

            output = {
                'placa': placa,
                'marca': data.get('marca'),
                'modelo': data.get('modelo'),
                'ano': int(data.get('ano', 0)),
                'importado': data.get('importado', False),
                'cor': data.get('cor'),
                'cilindrada': int(data.get('cilindrada', '0 cc').replace(' cc', '')),
                'potencia': int(data.get('potencia', '0 cv').replace(' cv', '')),
                'combustivel': data.get('combustível'),
                'chassi': data.get('chassi'),
                'motor': data.get('motor'),
                'UF': data.get('uf'),
                'municipio': data.get('município'),
                'segmento': data.get('segmento'),
                'especie': data.get('especie veiculo'),
                'fipe': fipe_data
            }

            return jsonify(output)
        else:
            return jsonify({'error': 'Erro ao fazer o request'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

