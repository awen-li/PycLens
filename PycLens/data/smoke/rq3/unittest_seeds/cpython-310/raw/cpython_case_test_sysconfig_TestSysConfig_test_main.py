# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with captured_stdout() as output:
        _main()
    self.assertTrue(len(output.getvalue().split('\n')) > 0)
