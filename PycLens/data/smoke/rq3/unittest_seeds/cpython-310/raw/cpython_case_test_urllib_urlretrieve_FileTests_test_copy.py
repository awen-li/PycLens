# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlretrieve_FileTests_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    second_temp = '%s.2' % os_helper.TESTFN
    self.registerFileForCleanUp(second_temp)
    result = urllib.request.urlretrieve(self.constructLocalFileUrl(os_helper.TESTFN), second_temp)
    self.assertEqual(second_temp, result[0])
    self.assertTrue(os.path.exists(second_temp), 'copy of the file was not made')
    FILE = open(second_temp, 'rb')
    try:
        text = FILE.read()
        FILE.close()
    finally:
        try:
            FILE.close()
        except:
            pass
    self.assertEqual(self.text, text)
