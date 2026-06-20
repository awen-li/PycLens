# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with captured_stderr() as error_stringio:
        s = self.run_main(switches=['1/0'])
    self.assert_exc_string(error_stringio.getvalue(), 'ZeroDivisionError')
