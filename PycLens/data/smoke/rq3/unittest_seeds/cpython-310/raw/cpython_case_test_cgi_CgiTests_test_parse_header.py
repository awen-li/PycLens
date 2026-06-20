# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_parse_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(cgi.parse_header('text/plain'), ('text/plain', {}))
    self.assertEqual(cgi.parse_header('text/vnd.just.made.this.up ; '), ('text/vnd.just.made.this.up', {}))
    self.assertEqual(cgi.parse_header('text/plain;charset=us-ascii'), ('text/plain', {'charset': 'us-ascii'}))
    self.assertEqual(cgi.parse_header('text/plain ; charset="us-ascii"'), ('text/plain', {'charset': 'us-ascii'}))
    self.assertEqual(cgi.parse_header('text/plain ; charset="us-ascii"; another=opt'), ('text/plain', {'charset': 'us-ascii', 'another': 'opt'}))
    self.assertEqual(cgi.parse_header('attachment; filename="silly.txt"'), ('attachment', {'filename': 'silly.txt'}))
    self.assertEqual(cgi.parse_header('attachment; filename="strange;name"'), ('attachment', {'filename': 'strange;name'}))
    self.assertEqual(cgi.parse_header('attachment; filename="strange;name";size=123;'), ('attachment', {'filename': 'strange;name', 'size': '123'}))
    self.assertEqual(cgi.parse_header('form-data; name="files"; filename="fo\\"o;bar"'), ('form-data', {'name': 'files', 'filename': 'fo"o;bar'}))
