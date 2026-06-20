# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: NamespaceSeparatorTest_test_illegal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        expat.ParserCreate(namespace_separator=42)
        self.fail()
    except TypeError as e:
        self.assertEqual(str(e), "ParserCreate() argument 'namespace_separator' must be str or None, not int")
    try:
        expat.ParserCreate(namespace_separator='too long')
        self.fail()
    except ValueError as e:
        self.assertEqual(str(e), 'namespace_separator must be at most one character, omitted, or None')
