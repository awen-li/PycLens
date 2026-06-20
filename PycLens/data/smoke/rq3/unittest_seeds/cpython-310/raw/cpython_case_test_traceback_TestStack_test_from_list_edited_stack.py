# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestStack_test_from_list_edited_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = traceback.StackSummary.from_list([('foo.py', 1, 'fred', 'line')])
    s[0] = ('foo.py', 2, 'fred', 'line')
    s2 = traceback.StackSummary.from_list(s)
    self.assertEqual(['  File "foo.py", line 2, in fred\n    line\n'], s2.format())
