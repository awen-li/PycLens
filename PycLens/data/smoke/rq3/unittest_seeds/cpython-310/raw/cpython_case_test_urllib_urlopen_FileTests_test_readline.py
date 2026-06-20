# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_FileTests_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.text, self.returned_obj.readline())
    self.assertEqual(b'', self.returned_obj.readline(), 'calling readline() after exhausting the file did not return an empty string')
