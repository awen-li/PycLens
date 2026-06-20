# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlretrieve_FileTests_test_reporthook_5_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    report = []

    def hooktester(block_count, block_read_size, file_size, _report=report):
        _report.append((block_count, block_read_size, file_size))
    srcFileName = self.createNewTempFile(b'x' * 5)
    urllib.request.urlretrieve(self.constructLocalFileUrl(srcFileName), os_helper.TESTFN, hooktester)
    self.assertEqual(len(report), 2)
    self.assertEqual(report[0][2], 5)
    self.assertEqual(report[1][2], 5)
