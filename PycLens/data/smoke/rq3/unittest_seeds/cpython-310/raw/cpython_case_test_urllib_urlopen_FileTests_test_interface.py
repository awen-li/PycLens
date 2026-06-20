# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_FileTests_test_interface

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for attr in ('read', 'readline', 'readlines', 'fileno', 'close', 'info', 'geturl', 'getcode', '__iter__'):
        self.assertTrue(hasattr(self.returned_obj, attr), 'object returned by urlopen() lacks %s attribute' % attr)
