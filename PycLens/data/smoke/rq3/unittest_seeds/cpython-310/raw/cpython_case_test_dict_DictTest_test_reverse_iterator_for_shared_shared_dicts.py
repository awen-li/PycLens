# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_reverse_iterator_for_shared_shared_dicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __init__(self, x, y):
            if x:
                self.x = x
            if y:
                self.y = y
    self.assertEqual(list(reversed(A(1, 2).__dict__)), ['y', 'x'])
    self.assertEqual(list(reversed(A(1, 0).__dict__)), ['x'])
    self.assertEqual(list(reversed(A(0, 1).__dict__)), ['y'])
