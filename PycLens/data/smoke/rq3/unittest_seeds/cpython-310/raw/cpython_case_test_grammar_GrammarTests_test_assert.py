# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_assert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert 1
    assert 1, 1
    assert lambda x: x
    assert 1, lambda x: x + 1
    try:
        assert True
    except AssertionError as e:
        self.fail("'assert True' should not have raised an AssertionError")
    try:
        assert True, 'this should always pass'
    except AssertionError as e:
        self.fail("'assert True, msg' should not have raised an AssertionError")
