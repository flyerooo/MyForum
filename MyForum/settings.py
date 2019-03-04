import peewee_async

settings = {
    'static_path': './static',
    'static_url_prefix': '/static/',
    'template_path': 'templates',
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '',
        'name': 'message',
        'charset': 'utf8mb4'
    },
    "redis": {
        "host": "127.0.0.1"
    }
}

database = peewee_async.MySQLDatabase(
    'MyForum', host="127.0.0.1", port=3306, user="root", password="p2pdev"
)
