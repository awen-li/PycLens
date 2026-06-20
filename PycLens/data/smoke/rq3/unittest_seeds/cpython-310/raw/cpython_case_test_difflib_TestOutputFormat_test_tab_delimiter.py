# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestOutputFormat_test_tab_delimiter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = ['one', 'two', 'Original', 'Current', '2005-01-26 23:30:50', '2010-04-02 10:20:52']
    ud = difflib.unified_diff(*args, lineterm='')
    self.assertEqual(list(ud)[0:2], ['--- Original\t2005-01-26 23:30:50', '+++ Current\t2010-04-02 10:20:52'])
    cd = difflib.context_diff(*args, lineterm='')
    self.assertEqual(list(cd)[0:2], ['*** Original\t2005-01-26 23:30:50', '--- Current\t2010-04-02 10:20:52'])
