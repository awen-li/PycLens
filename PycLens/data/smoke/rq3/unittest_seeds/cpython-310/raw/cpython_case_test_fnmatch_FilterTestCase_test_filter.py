# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FilterTestCase_test_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(filter(['Python', 'Ruby', 'Perl', 'Tcl'], 'P*'), ['Python', 'Perl'])
    self.assertEqual(filter([b'Python', b'Ruby', b'Perl', b'Tcl'], b'P*'), [b'Python', b'Perl'])
