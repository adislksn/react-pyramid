from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import pymysql
from wsgicors import CORS

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='product',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@view_config(route_name='hello', request_method='GET', renderer='json')
def hello_world(request):
    print('Incoming request')
    data = [{'id': 1, 'name': 'product 1'}, {'id': 2, 'name': 'product 2'}]
    return {'data': data}

@view_config(route_name='product', request_method='GET', renderer='json')
def product(request):
    '''Create a hello view to get'''
    # show from table movies
    with connection.cursor() as cursor:
        sql = "SELECT * FROM assets"
        cursor.execute(sql)
        result = cursor.fetchall()
    
    print(result)
    data = []
    for item in result:
        data.append({
            'fitra': item['id'],
            'nama_produk': item['product_name'],
            'harga_produk': item['product_price'],
            'stok': item['supply'],
        })
    return {
        'greet': 'ok',
        'data_ori' : result, 
        'data': data
        }

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_route('product', '/product')
        config.scan()
        config.add_static_view(name='static', path='static')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)