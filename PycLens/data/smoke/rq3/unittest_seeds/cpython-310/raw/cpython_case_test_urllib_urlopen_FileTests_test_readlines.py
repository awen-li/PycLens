# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_FileTests_test_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines_list = self.returned_obj.readlines()
    self.assertEqual(len(lines_list), 1, 'readlines() returned the wrong number of lines')
    self.assertEqual(lines_list[0], self.text, 'readlines() returned improper text')
