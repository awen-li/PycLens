# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_reduce

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __reduce__(self):
            c.append(1)
            return ''
    c = []
    x = C()
    y = copy.deepcopy(x)
    self.assertIs(y, x)
    self.assertEqual(c, [1])
