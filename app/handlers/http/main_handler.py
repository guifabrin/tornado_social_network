import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../../templates/main_handler.html")
