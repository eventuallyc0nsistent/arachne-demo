from datetime import datetime
from twisted.web import http
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor
from arachne import Arachne

# testing Arachne
app = Arachne(__name__)

resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource,
            logFormatter=http.combinedLogFormatter,
            logPath="logs/"+datetime.now().strftime("%Y-%m-%d.web.log"))
reactor.listenTCP(8080, site)

if __name__ == '__main__':
    reactor.run()
