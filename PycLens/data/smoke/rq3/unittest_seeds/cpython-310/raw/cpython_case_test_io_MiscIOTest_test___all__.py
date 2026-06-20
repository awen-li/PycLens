# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test___all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in self.io.__all__:
        obj = getattr(self.io, name, None)
        self.assertIsNotNone(obj, name)
        if name in ('open', 'open_code'):
            continue
        elif 'error' in name.lower() or name == 'UnsupportedOperation':
            self.assertTrue(issubclass(obj, Exception), name)
        elif not name.startswith('SEEK_'):
            self.assertTrue(issubclass(obj, self.IOBase))
