# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBoundArguments_test_signature_bound_arguments_unhashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a):
        pass
    ba = inspect.signature(foo).bind(1)
    with self.assertRaisesRegex(TypeError, 'unhashable type'):
        hash(ba)
