from tornado import web
import tornado

from MyForum.urls import urlpattern
from MyForum.settings import settings





if __name__ == '__main__':
    app = web.Application(urlpattern, debug=True, **settings)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
