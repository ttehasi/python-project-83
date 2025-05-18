import os

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.exceptions import HTTPException

from page_analyzer.db.utils import (
    add_url,
    add_url_check,
    get_all_urls,
    get_last_url_check_by_id,
    get_url_by_id,
    get_url_by_name,
    get_url_check_by_url_id,
)
from page_analyzer.url_validator import norm_url, validate_url

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    url = {}
    return render_template(
        'index.html',
        url=url
    )
    
    
@app.post('/urls')
def urls_post():
    data = request.form.get('url')
    errors = validate_url(data)
    if errors:
        return render_template(
            'index.html',
            errors=errors,
            url=data,
        ), 422
    normal_url = norm_url(data)
    url = get_url_by_name(normal_url)
    if url is not None:
        flash('Страница уже существует', 'info')
        return redirect(url_for('get_url', id=url.id))
    add_url(name=normal_url)
    id_new = get_url_by_name(normal_url).id
    flash('Страница успешно добавлена', 'success')
    return redirect(url_for('get_url', id=id_new))


@app.route('/urls/<int:id>')
def get_url(id):
    messages = get_flashed_messages(with_categories=True) 
    url = get_url_by_id(id)
    if url is None:
        return render_template(
            '404.html',
        ), 404
    url_checks = get_url_check_by_url_id(id)
    return render_template(
        'url.html',
        messages=messages,
        url=url,
        url_checks=url_checks
    )
    
    
@app.route('/urls')
def get_urls():
    urls = get_all_urls()
    all_about_url = []
    for i in urls:
        all_about_url.append((i, get_last_url_check_by_id(i.id)))
        # all_about_url['url'] = i
        # all_about_url['last_check'] = get_last_url_check_by_id(i.id)
    return render_template(
        'urls.html',
        all_about_url=all_about_url
    )
    
    
@app.route('/urls/<int:id>/check', methods=['POST'])
def check_url(id):
    url = get_url_by_id(id)
    add_url_check(url.id)
    flash('Страница успешно проверена', 'success')
    return redirect(url_for('get_url', id=url.id))


@app.errorhandler(HTTPException)
def error_500(error):
    return render_template(
        '500.html',
    )