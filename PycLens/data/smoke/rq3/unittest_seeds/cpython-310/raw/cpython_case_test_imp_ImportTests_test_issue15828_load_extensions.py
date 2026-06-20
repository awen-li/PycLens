# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue15828_load_extensions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = '_heapq'
    x = imp.find_module(example)
    file_ = x[0]
    if file_ is not None:
        self.addCleanup(file_.close)
    mod = imp.load_module(example, *x)
    self.assertEqual(mod.__name__, example)
