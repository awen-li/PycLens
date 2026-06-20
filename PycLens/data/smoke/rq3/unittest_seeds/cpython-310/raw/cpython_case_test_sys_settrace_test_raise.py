# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: test_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    try:
        raises()
    except Exception:
        pass
