# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_over

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, count, first, last, name) = self.server.group(self.GROUP_NAME)
    start = last - 10
    (resp, lines) = self.server.over((start, None))
    (art_num, art_dict) = lines[0]
    self._check_art_dict(art_dict)
    (resp, lines) = self.server.over((start, last))
    (art_num, art_dict) = lines[-1]
    self.assertGreaterEqual(art_num, start)
    self.assertLessEqual(art_num, last)
    self._check_art_dict(art_dict)
