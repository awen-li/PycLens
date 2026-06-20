# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_getpager_with_stdin_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    previous_stdin = sys.stdin
    try:
        sys.stdin = None
        pydoc.getpager()
    finally:
        sys.stdin = previous_stdin
