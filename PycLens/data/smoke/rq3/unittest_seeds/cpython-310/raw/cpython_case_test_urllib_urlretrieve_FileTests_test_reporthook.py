# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlretrieve_FileTests_test_reporthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def hooktester(block_count, block_read_size, file_size, count_holder=[0]):
        self.assertIsInstance(block_count, int)
        self.assertIsInstance(block_read_size, int)
        self.assertIsInstance(file_size, int)
        self.assertEqual(block_count, count_holder[0])
        count_holder[0] = count_holder[0] + 1
    second_temp = '%s.2' % os_helper.TESTFN
    self.registerFileForCleanUp(second_temp)
    urllib.request.urlretrieve(self.constructLocalFileUrl(os_helper.TESTFN), second_temp, hooktester)
