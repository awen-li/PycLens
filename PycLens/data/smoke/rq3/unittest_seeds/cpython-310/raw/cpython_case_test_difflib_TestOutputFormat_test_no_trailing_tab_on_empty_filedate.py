# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestOutputFormat_test_no_trailing_tab_on_empty_filedate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = ['one', 'two', 'Original', 'Current']
    ud = difflib.unified_diff(*args, lineterm='')
    self.assertEqual(list(ud)[0:2], ['--- Original', '+++ Current'])
    cd = difflib.context_diff(*args, lineterm='')
    self.assertEqual(list(cd)[0:2], ['*** Original', '--- Current'])
