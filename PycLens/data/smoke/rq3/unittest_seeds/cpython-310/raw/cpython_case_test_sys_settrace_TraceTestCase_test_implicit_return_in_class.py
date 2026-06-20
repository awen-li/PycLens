# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_implicit_return_in_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():

        class A:
            if 3 < 9:
                a = 1
            else:
                a = 2
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (1, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (3, 'return'), (1, 'return')])
