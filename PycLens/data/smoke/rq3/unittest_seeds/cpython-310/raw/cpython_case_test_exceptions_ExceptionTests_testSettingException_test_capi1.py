# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_testSettingException_test_capi1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    try:
        _testcapi.raise_exception(BadException, 1)
    except TypeError as err:
        (exc, err, tb) = sys.exc_info()
        co = tb.tb_frame.f_code
        self.assertEqual(co.co_name, 'test_capi1')
        self.assertTrue(co.co_filename.endswith('test_exceptions.py'))
    else:
        self.fail('Expected exception')
