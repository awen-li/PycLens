# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_read_returns_file_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.delimiters[0] != '=':
        self.skipTest('incompatible format')
    file1 = support.findfile('cfgparser.1')
    cf = self.newconfig()
    parsed_files = cf.read([file1, 'nonexistent-file'], encoding='utf-8')
    self.assertEqual(parsed_files, [file1])
    self.assertEqual(cf.get('Foo Bar', 'foo'), 'newbar')
    cf = self.newconfig()
    parsed_files = cf.read(file1, encoding='utf-8')
    self.assertEqual(parsed_files, [file1])
    self.assertEqual(cf.get('Foo Bar', 'foo'), 'newbar')
    cf = self.newconfig()
    parsed_files = cf.read(pathlib.Path(file1), encoding='utf-8')
    self.assertEqual(parsed_files, [file1])
    self.assertEqual(cf.get('Foo Bar', 'foo'), 'newbar')
    cf = self.newconfig()
    parsed_files = cf.read([pathlib.Path(file1), file1], encoding='utf-8')
    self.assertEqual(parsed_files, [file1, file1])
    self.assertEqual(cf.get('Foo Bar', 'foo'), 'newbar')
    cf = self.newconfig()
    parsed_files = cf.read(['nonexistent-file'], encoding='utf-8')
    self.assertEqual(parsed_files, [])
    cf = self.newconfig()
    parsed_files = cf.read([], encoding='utf-8')
    self.assertEqual(parsed_files, [])
