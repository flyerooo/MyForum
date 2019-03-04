from tornado import web
import tornado
from peewee_async import Manager

from MyForum.urls import urlpattern
from MyForum.settings import settings, database





if __name__ == '__main__':
    # 集成json到wtforms
    import wtforms_json
    app = web.Application(urlpattern, debug=True, **settings)

    wtforms_json.init()
    app.listen(8888)

    objects = Manager(database)
    database.set_allow_sync(False)
    app.objects = objects

    tornado.ioloop.IOLoop.current().start()
