# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBuggyCases_test_findsource_without_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fname in ['', '<string>']:
        co = compile('x=1', fname, 'exec')
        self.assertRaises(IOError, inspect.findsource, co)
        self.assertRaises(IOError, inspect.getsource, co)
