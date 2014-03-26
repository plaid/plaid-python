
import webapp2

import plaid


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        w = self.response.write
        w("<html>")
        w("<head>")
        w('<title>Plaid Sample</title>')
        w("</head>")
        w("<body>")
        w("<pre>")
        client = plaid.Client("53237a9b00cdb13908a873d3", "3411JxgdbhkAF_uI4mPikm", 'WyI1MzIzN2E5YjAwY2RiMTM5MDhhODczZDMiLCI1MzMxZTE0ZGJkZjZkOWYxMWExZTllMTIiLCI1MzMxZTE0ZmJkZjZkOWYxMWExZTllMTMiXQ==')
        #res = client.transactions({'pretty': True})
        #print res.content
        w(client.balance({'pretty': True}).content)
        w("</pre>")
        w("</body>")
        w("</html>")


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)