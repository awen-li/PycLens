# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_docxmlrpc.py
# case: DocXMLRPCHTTPGETServer_test_server_title_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.serv.set_server_title('test_title<script>')
    self.serv.set_server_documentation('test_documentation<script>')
    self.assertEqual('test_title<script>', self.serv.server_title)
    self.assertEqual('test_documentation<script>', self.serv.server_documentation)
    generated = self.serv.generate_html_documentation()
    title = re.search('<title>(.+?)</title>', generated).group()
    documentation = re.search('<p><tt>(.+?)</tt></p>', generated).group()
    self.assertEqual('<title>Python: test_title&lt;script&gt;</title>', title)
    self.assertEqual('<p><tt>test_documentation&lt;script&gt;</tt></p>', documentation)
