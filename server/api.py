from flask import Flask, Response, json, request
from translator import search, get_langlinks

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello from Wiki Translate!"


@app.route('/search_pages', methods=['GET'])
def search_pages():
    # e.g.: /search_pages?lang=nl&text=comp
    lang = request.args.get('lang', type=str)
    text = request.args.get('text', type=str)

    search_res = search(text, lang)
    print(search_res)

    return json_response(search_res)


@app.route('/get_translations', methods=['GET'])
def get_translations():
    # e.g.: http://127.0.0.1:5000/get_translations?page=Competitiestructuur van het Belgisch voetbal&lang=nl
    page_name = request.args.get('page', type=str)
    source_lang = request.args.get('lang', type=str)

    lang_links = get_langlinks(page_name, source_lang)
    print(lang_links)

    return json_response(lang_links)


def json_response(data):
    response = Response(
        response=json.dumps(data),
        status=200,
        mimetype='application/json',
    )
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', debug=True)
