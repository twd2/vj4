from er import app
from er import template
from er.handler import base


@app.route('/', 'main')
class MainHandler(base.Handler):
  @base.sanitize
  async def get(self):
    self.render('main.html')
