# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_xover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, count, first, last, name) = self.server.group(self.GROUP_NAME)
    (resp, lines) = self.server.xover(last - 5, last)
    if len(lines) == 0:
        self.skipTest('no articles retrieved')
    (art_num, art_dict) = lines[0]
    self.assertGreaterEqual(art_num, last - 5)
    self.assertLessEqual(art_num, last)
    self._check_art_dict(art_dict)
