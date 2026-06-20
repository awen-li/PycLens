# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ParseTest_test_parse_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    out = self.Outputter()
    parser = expat.ParserCreate(namespace_separator='!')
    self._hookup_callbacks(parser, out)
    parser.Parse(data, True)
    operations = out.out
    self._verify_parse_output(operations)
    self.assertRaises(AttributeError, getattr, parser, '\ud800')
