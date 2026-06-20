# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_new_style_iter_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class IterClass(object):

        def __iter__(self):
            return self
    self.assertRaises(TypeError, iter, IterClass())
