# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_new_builtins_issue_43102

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = namedtuple('C', ())
    new_func = obj.__new__
    self.assertEqual(new_func.__globals__['__builtins__'], {})
    self.assertEqual(new_func.__builtins__, {})
