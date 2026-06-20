# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_html.py
# case: HtmlTests_test_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(html.escape('\'<script>"&foo;"</script>\''), '&#x27;&lt;script&gt;&quot;&amp;foo;&quot;&lt;/script&gt;&#x27;')
    self.assertEqual(html.escape('\'<script>"&foo;"</script>\'', False), '\'&lt;script&gt;"&amp;foo;"&lt;/script&gt;\'')
