# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_doctest.py
# case: test_hook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    hook = TestHook(pathdir)
    try:
        yield hook
    finally:
        hook.remove()
