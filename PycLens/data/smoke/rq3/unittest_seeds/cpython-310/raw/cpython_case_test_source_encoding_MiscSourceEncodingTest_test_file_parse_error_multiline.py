# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_file_parse_error_multiline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as fd:
        fd.write(b'print("""\n\xb1""")\n')
    try:
        (retcode, stdout, stderr) = script_helper.assert_python_failure(TESTFN)
        self.assertGreater(retcode, 0)
        self.assertIn(b"Non-UTF-8 code starting with '\\xb1'", stderr)
    finally:
        os.unlink(TESTFN)
