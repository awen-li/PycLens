# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_read_returns_file_list_with_bytestring_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.delimiters[0] != '=':
        self.skipTest('incompatible format')
    file1_bytestring = support.findfile('cfgparser.1').encode()
    cf = self.newconfig()
    parsed_files = cf.read(file1_bytestring, encoding='utf-8')
    self.assertEqual(parsed_files, [file1_bytestring])
    cf = self.newconfig()
    parsed_files = cf.read(b'nonexistent-file', encoding='utf-8')
    self.assertEqual(parsed_files, [])
    cf = self.newconfig()
    parsed_files = cf.read([file1_bytestring, b'nonexistent-file'], encoding='utf-8')
    self.assertEqual(parsed_files, [file1_bytestring])
