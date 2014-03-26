
import webapp2

import plaid

# need to fill these first
CLIENT = ""   # as given by Plaid
SECRET = ""   # as given by Plaid
ACCESS_TOKEN = ""  # I assume here that you have already created this

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
        client = plaid.Client(CLIENT, SECRET, ACCESS_TOKEN)
        #res = client.transactions({'pretty': True})
        #print res.content
        w(client.balance({'pretty': True}).content)
        w("</pre>")
        w("</body>")
        w("</html>")


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)