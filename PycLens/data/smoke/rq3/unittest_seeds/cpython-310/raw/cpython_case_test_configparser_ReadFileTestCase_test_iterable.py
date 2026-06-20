# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ReadFileTestCase_test_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = textwrap.dedent('\n        [Foo Bar]\n        foo=newbar').strip().split('\n')
    parser = configparser.ConfigParser()
    parser.read_file(lines)
    self.assertIn('Foo Bar', parser)
    self.assertIn('foo', parser['Foo Bar'])
    self.assertEqual(parser['Foo Bar']['foo'], 'newbar')
