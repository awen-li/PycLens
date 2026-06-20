# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: AppendTest_test_fileobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._create_testtar()
    with open(self.tarname, 'rb') as fobj:
        data = fobj.read()
    fobj = io.BytesIO(data)
    self._add_testfile(fobj)
    fobj.seek(0)
    self._test(names=['foo', 'bar'], fileobj=fobj)
