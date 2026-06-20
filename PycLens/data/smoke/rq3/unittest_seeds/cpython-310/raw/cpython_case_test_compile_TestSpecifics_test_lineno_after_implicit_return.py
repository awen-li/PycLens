# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_lineno_after_implicit_return

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TRUE = True

    def if1(x):
        x()
        if TRUE:
            pass

    def if2(x):
        x()
        if TRUE:
            pass
        else:
            pass

    def if3(x):
        x()
        if TRUE:
            pass
        else:
            return None

    def if4(x):
        x()
        if not TRUE:
            pass
    funcs = [if1, if2, if3, if4]
    lastlines = [3, 3, 3, 2]
    frame = None

    def save_caller_frame():
        nonlocal frame
        frame = sys._getframe(1)
    for (func, lastline) in zip(funcs, lastlines, strict=True):
        with self.subTest(func=func):
            func(save_caller_frame)
            self.assertEqual(frame.f_lineno - frame.f_code.co_firstlineno, lastline)
