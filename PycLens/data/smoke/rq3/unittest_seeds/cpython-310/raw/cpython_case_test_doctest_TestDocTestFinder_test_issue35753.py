# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_doctest.py
# case: TestDocTestFinder_test_issue35753

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from unittest.mock import call
    dummy_module = types.ModuleType('dummy')
    dummy_module.__dict__['inject_call'] = call
    try:
        support.run_doctest(dummy_module, verbosity=True)
    except ValueError as e:
        raise support.TestFailed('Doctest unwrap failed') from e
