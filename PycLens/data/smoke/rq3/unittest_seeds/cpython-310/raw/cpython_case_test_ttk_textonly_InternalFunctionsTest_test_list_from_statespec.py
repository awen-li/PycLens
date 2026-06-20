# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_list_from_statespec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test_it(sspec, value, res_value, states):
        self.assertEqual(ttk._list_from_statespec((sspec, value)), [states + (res_value,)])
    states_even = tuple(('state%d' % i for i in range(6)))
    statespec = MockStateSpec(*states_even)
    test_it(statespec, 'val', 'val', states_even)
    test_it(statespec, MockTclObj('val'), 'val', states_even)
    states_odd = tuple(('state%d' % i for i in range(5)))
    statespec = MockStateSpec(*states_odd)
    test_it(statespec, 'val', 'val', states_odd)
    test_it(('a', 'b', 'c'), MockTclObj('val'), 'val', ('a', 'b', 'c'))
