# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_exec_redirected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    savestdout = sys.stdout
    sys.stdout = None
    try:
        exec('a')
    except NameError:
        pass
    finally:
        sys.stdout = savestdout
