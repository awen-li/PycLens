# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_read_return_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for test_size in (1, 4095, 4096, 4097, 16384):
        file_size = test_size + 1
        junk = randbytes(file_size)
        with zipfile.ZipFile(io.BytesIO(), 'w', self.compression) as zipf:
            zipf.writestr('foo', junk)
            with zipf.open('foo', 'r') as fp:
                buf = fp.read(test_size)
                self.assertEqual(len(buf), test_size)
