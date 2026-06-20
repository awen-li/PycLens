# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pty.py
# case: PtyTest_test_spawn_doesnt_hang

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pty.spawn([sys.executable, '-c', 'print("hi there")'])
