# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_open_nonwritable_fileobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for exctype in (OSError, EOFError, RuntimeError):

        class BadFile(io.BytesIO):
            first = True

            def write(self, data):
                if self.first:
                    self.first = False
                    raise exctype
        f = BadFile()
        with self.assertRaises(exctype):
            tar = tarfile.open(tmpname, self.mode, fileobj=f, format=tarfile.PAX_FORMAT, pax_headers={'non': 'empty'})
        self.assertFalse(f.closed)
