# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_if_false_in_with

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __enter__(self):
            return self

        def __exit__(*args):
            pass

    def func():
        with C():
            if False:
                pass
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (-5, 'call'), (-4, 'line'), (-4, 'return'), (2, 'line'), (1, 'line'), (-3, 'call'), (-2, 'line'), (-2, 'return'), (1, 'return')])
