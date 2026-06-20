# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: RaisingTraceFuncTestCase_test_trash_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        for i in range(5):
            print(i)

    def g(frame, why, extra):
        if why == 'line' and frame.f_lineno == f.__code__.co_firstlineno + 2:
            raise RuntimeError('i am crashing')
        return g
    sys.settrace(g)
    try:
        f()
    except RuntimeError:
        import gc
        gc.collect()
    else:
        self.fail('exception not propagated')
