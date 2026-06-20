# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractBadCrcTests_test_read_with_bad_crc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipdata = self.zip_with_bad_crc
    with zipfile.ZipFile(io.BytesIO(zipdata), mode='r') as zipf:
        self.assertRaises(zipfile.BadZipFile, zipf.read, 'afile')
    with zipfile.ZipFile(io.BytesIO(zipdata), mode='r') as zipf:
        with zipf.open('afile', 'r') as corrupt_file:
            self.assertRaises(zipfile.BadZipFile, corrupt_file.read)
    with zipfile.ZipFile(io.BytesIO(zipdata), mode='r') as zipf:
        with zipf.open('afile', 'r') as corrupt_file:
            corrupt_file.MIN_READ_SIZE = 2
            with self.assertRaises(zipfile.BadZipFile):
                while corrupt_file.read(2):
                    pass
