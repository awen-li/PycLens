# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: TestMain_test_encode_from_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with script_helper.spawn_python('-m', 'base64', '-e') as proc:
        (out, err) = proc.communicate(b'a\xffb\n')
    self.assertEqual(out.rstrip(), b'Yf9iCg==')
    self.assertIsNone(err)
