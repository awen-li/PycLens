# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_nested_partial_with_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    partial = self.partial

    def foo(bar):
        return bar
    p = partial(foo, 'first')
    p2 = partial(p, 'second')
    p2.new_attr = 'spam'
    self.assertEqual(p2.new_attr, 'spam')
