# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_early_exit_with

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __enter__(self):
            return self

        def __exit__(*args):
            pass

    def func_break():
        for i in (1, 2):
            with C():
                break
        pass

    def func_return():
        with C():
            return
    self.run_and_compare(func_break, [(0, 'call'), (1, 'line'), (2, 'line'), (-5, 'call'), (-4, 'line'), (-4, 'return'), (3, 'line'), (2, 'line'), (-3, 'call'), (-2, 'line'), (-2, 'return'), (4, 'line'), (4, 'return')])
    self.run_and_compare(func_return, [(0, 'call'), (1, 'line'), (-11, 'call'), (-10, 'line'), (-10, 'return'), (2, 'line'), (1, 'line'), (-9, 'call'), (-8, 'line'), (-8, 'return'), (1, 'return')])
