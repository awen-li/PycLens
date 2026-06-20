# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_yet_more_evil_still_undecodable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = b'#\x00\n#\xfd\n'
    with tempfile.TemporaryDirectory() as tmpd:
        fn = os.path.join(tmpd, 'bad.py')
        with open(fn, 'wb') as fp:
            fp.write(src)
        res = script_helper.run_python_until_end(fn)[0]
    self.assertIn(b'Non-UTF-8', res.err)
