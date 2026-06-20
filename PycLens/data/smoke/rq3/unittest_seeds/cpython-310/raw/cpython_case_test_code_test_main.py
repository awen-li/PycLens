# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    from test import test_code
    run_doctest(test_code, verbose)
    tests = [CodeTest, CodeConstsTest, CodeWeakRefTest]
    if check_impl_detail(cpython=True) and ctypes is not None:
        tests.append(CoExtra)
    run_unittest(*tests)
