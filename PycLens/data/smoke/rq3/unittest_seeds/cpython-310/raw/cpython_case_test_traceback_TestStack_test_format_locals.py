# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestStack_test_format_locals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def some_inner(k, v):
        a = 1
        b = 2
        return traceback.StackSummary.extract(traceback.walk_stack(None), capture_locals=True, limit=1)
    s = some_inner(3, 4)
    self.assertEqual(['  File "%s", line %d, in some_inner\n    return traceback.StackSummary.extract(\n    a = 1\n    b = 2\n    k = 3\n    v = 4\n' % (__file__, some_inner.__code__.co_firstlineno + 3)], s.format())
