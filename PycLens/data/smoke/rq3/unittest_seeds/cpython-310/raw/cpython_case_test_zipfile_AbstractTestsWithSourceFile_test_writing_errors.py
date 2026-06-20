# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_writing_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BrokenFile(io.BytesIO):

        def write(self, data):
            nonlocal count
            if count is not None:
                if count == stop:
                    raise OSError
                count += 1
            super().write(data)
    stop = 0
    while True:
        testfile = BrokenFile()
        count = None
        with zipfile.ZipFile(testfile, 'w', self.compression) as zipfp:
            with zipfp.open('file1', 'w') as f:
                f.write(b'data1')
            count = 0
            try:
                with zipfp.open('file2', 'w') as f:
                    f.write(b'data2')
            except OSError:
                stop += 1
            else:
                break
            finally:
                count = None
        with zipfile.ZipFile(io.BytesIO(testfile.getvalue())) as zipfp:
            self.assertEqual(zipfp.namelist(), ['file1'])
            self.assertEqual(zipfp.read('file1'), b'data1')
    with zipfile.ZipFile(io.BytesIO(testfile.getvalue())) as zipfp:
        self.assertEqual(zipfp.namelist(), ['file1', 'file2'])
        self.assertEqual(zipfp.read('file1'), b'data1')
        self.assertEqual(zipfp.read('file2'), b'data2')
