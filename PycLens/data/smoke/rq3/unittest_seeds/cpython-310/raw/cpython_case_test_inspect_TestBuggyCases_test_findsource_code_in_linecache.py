# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBuggyCases_test_findsource_code_in_linecache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = ['x=1']
    co = compile(lines[0], '_dynamically_created_file', 'exec')
    self.assertRaises(OSError, inspect.findsource, co)
    self.assertRaises(OSError, inspect.getsource, co)
    linecache.cache[co.co_filename] = (1, None, lines, co.co_filename)
    try:
        self.assertEqual(inspect.findsource(co), (lines, 0))
        self.assertEqual(inspect.getsource(co), lines[0])
    finally:
        del linecache.cache[co.co_filename]
