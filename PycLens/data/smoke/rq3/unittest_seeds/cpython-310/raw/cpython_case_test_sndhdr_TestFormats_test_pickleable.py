# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sndhdr.py
# case: TestFormats_test_pickleable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = findfile('sndhdr.aifc', subdir='sndhdrdata')
    what = sndhdr.what(filename)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        dump = pickle.dumps(what, proto)
        self.assertEqual(pickle.loads(dump), what)
