# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_FileTests_test_fileno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    file_num = self.returned_obj.fileno()
    self.assertIsInstance(file_num, int, 'fileno() did not return an int')
    self.assertEqual(os.read(file_num, len(self.text)), self.text, 'Reading on the file descriptor returned by fileno() did not return the expected text')
