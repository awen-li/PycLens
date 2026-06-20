# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ReadFileTestCase_test_readline_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = configparser.ConfigParser()
    with self.assertRaises(TypeError):
        parser.read_file(FakeFile())
    parser.read_file(readline_generator(FakeFile()))
    self.assertIn('Foo Bar', parser)
    self.assertIn('foo', parser['Foo Bar'])
    self.assertEqual(parser['Foo Bar']['foo'], 'newbar')
