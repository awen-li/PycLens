# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ReadFileTestCase_test_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    file_paths = [support.findfile('cfgparser.1')]
    try:
        file_paths.append(file_paths[0].encode('utf8'))
    except UnicodeEncodeError:
        pass
    for file_path in file_paths:
        parser = configparser.ConfigParser()
        with open(file_path, encoding='utf-8') as f:
            parser.read_file(f)
        self.assertIn('Foo Bar', parser)
        self.assertIn('foo', parser['Foo Bar'])
        self.assertEqual(parser['Foo Bar']['foo'], 'newbar')
