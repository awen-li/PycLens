# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3Class_test_top

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = (b'+OK 116 bytes', [b'From: postmaster@python.org', b'Content-Type: text/plain', b'MIME-Version: 1.0', b'Subject: Dummy', b'', b'line1', b'line2', b'line3'], 113)
    self.assertEqual(self.client.top(1, 1), expected)
