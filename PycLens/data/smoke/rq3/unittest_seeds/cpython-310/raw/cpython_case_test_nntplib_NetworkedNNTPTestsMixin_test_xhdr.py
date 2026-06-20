# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_xhdr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, count, first, last, name) = self.server.group(self.GROUP_NAME)
    (resp, lines) = self.server.xhdr('subject', last)
    for line in lines:
        self.assertEqual(str, type(line[1]))
