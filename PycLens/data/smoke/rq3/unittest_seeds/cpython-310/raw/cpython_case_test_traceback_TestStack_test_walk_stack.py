# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestStack_test_walk_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def deeper():
        return list(traceback.walk_stack(None))
    s1 = list(traceback.walk_stack(None))
    s2 = deeper()
    self.assertEqual(len(s2) - len(s1), 1)
    self.assertEqual(s2[1:], s1)
