# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: TestMain_test_encode_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'wb') as fp:
        fp.write(b'a\xffb\n')
    output = self.get_output('-e', os_helper.TESTFN)
    self.assertEqual(output.rstrip(), b'Yf9iCg==')
