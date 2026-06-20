# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: UnawaitedWarningDuringShutdownTest_test_unawaited_warning_during_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import asyncio\nasync def f(): pass\nasync def t(): asyncio.gather(f())\nasyncio.run(t())\n'
    assert_python_ok('-c', code)
    code = 'import sys\nasync def f(): pass\nsys.coro = f()\n'
    assert_python_ok('-c', code)
    code = 'import sys\nasync def f(): pass\nsys.corocycle = [f()]\nsys.corocycle.append(sys.corocycle)\n'
    assert_python_ok('-c', code)
