# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: PyZipFileTests_test_write_non_pyfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
        with open(TESTFN, 'w', encoding='utf-8') as f:
            f.write('most definitely not a python file')
        self.assertRaises(RuntimeError, zipfp.writepy, TESTFN)
        unlink(TESTFN)
