# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_assert_failures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        assert 0, 'msg'
    except AssertionError as e:
        self.assertEqual(e.args[0], 'msg')
    else:
        self.fail('AssertionError not raised by assert 0')
    try:
        assert False
    except AssertionError as e:
        self.assertEqual(len(e.args), 0)
    else:
        self.fail("AssertionError not raised by 'assert False'")
