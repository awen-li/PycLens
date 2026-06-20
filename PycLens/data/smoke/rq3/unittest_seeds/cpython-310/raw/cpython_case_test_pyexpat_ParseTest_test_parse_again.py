# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ParseTest_test_parse_again

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = expat.ParserCreate()
    file = BytesIO(data)
    parser.ParseFile(file)
    with self.assertRaises(expat.error) as cm:
        parser.ParseFile(file)
    self.assertEqual(expat.ErrorString(cm.exception.code), expat.errors.XML_ERROR_FINISHED)
