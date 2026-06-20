# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getframeinfo_get_first_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    frame_info = inspect.getframeinfo(self.fodderModule.fr, 50)
    self.assertEqual(frame_info.code_context[0], '# line 1\n')
    self.assertEqual(frame_info.code_context[1], "'A module docstring.'\n")
