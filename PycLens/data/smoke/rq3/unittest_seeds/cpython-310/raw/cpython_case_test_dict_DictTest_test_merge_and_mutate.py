# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_merge_and_mutate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __hash__(self):
            return 0

        def __eq__(self, o):
            other.clear()
            return False
    l = [(i, 0) for i in range(1, 1337)]
    other = dict(l)
    other[X()] = 0
    d = {X(): 0, 1: 1}
    self.assertRaises(RuntimeError, d.update, other)
