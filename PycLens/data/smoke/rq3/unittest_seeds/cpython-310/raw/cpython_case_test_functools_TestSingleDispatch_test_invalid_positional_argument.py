# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_invalid_positional_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def f(*args):
        pass
    msg = 'f requires at least 1 positional argument'
    with self.assertRaisesRegex(TypeError, msg):
        f()
