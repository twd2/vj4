from er import app
from er import template
from er.handler import base
from er.util import misc


@app.route('/preview', 'preview')
class PreviewHandler(base.Handler):
  @base.post_argument
  @base.sanitize
  async def post(self, *, text: str):
    self.response.content_type = 'text/html'
    self.response.text = misc.markdown(text)
