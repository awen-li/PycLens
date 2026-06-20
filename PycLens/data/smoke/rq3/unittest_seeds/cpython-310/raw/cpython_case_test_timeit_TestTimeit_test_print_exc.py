# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_print_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = io.StringIO()
    t = timeit.Timer('1/0')
    try:
        t.timeit()
    except:
        t.print_exc(s)
    self.assert_exc_string(s.getvalue(), 'ZeroDivisionError')
