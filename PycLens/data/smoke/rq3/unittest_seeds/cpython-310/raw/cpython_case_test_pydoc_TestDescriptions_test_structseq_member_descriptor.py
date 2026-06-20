# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_structseq_member_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self._get_summary_line(type(sys.hash_info).width), 'width')
    self.assertEqual(self._get_summary_line(type(sys.flags).debug), 'debug')
    self.assertEqual(self._get_summary_line(type(sys.version_info).major), 'major')
    self.assertEqual(self._get_summary_line(type(sys.float_info).max), 'max')
