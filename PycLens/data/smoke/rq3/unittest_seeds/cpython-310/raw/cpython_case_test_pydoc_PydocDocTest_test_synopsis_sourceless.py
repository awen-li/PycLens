# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_synopsis_sourceless

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = os.__doc__.splitlines()[0]
    filename = os.__cached__
    synopsis = pydoc.synopsis(filename)
    self.assertEqual(synopsis, expected)
