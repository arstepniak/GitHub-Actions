import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello!"

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
