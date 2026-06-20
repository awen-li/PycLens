# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ReadFileTestCase_test_source_as_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = textwrap.dedent('\n        [badbad]\n        [badbad]').strip().split('\n')
    parser = configparser.ConfigParser()
    with self.assertRaises(configparser.DuplicateSectionError) as dse:
        parser.read_file(lines, source=b'badbad')
    self.assertEqual(str(dse.exception), "While reading from b'badbad' [line  2]: section 'badbad' already exists")
    lines = textwrap.dedent('\n        [badbad]\n        bad = bad\n        bad = bad').strip().split('\n')
    parser = configparser.ConfigParser()
    with self.assertRaises(configparser.DuplicateOptionError) as dse:
        parser.read_file(lines, source=b'badbad')
    self.assertEqual(str(dse.exception), "While reading from b'badbad' [line  3]: option 'bad' in section 'badbad' already exists")
    lines = textwrap.dedent('\n        [badbad]\n        = bad').strip().split('\n')
    parser = configparser.ConfigParser()
    with self.assertRaises(configparser.ParsingError) as dse:
        parser.read_file(lines, source=b'badbad')
    self.assertEqual(str(dse.exception), "Source contains parsing errors: b'badbad'\n\t[line  2]: '= bad'")
    lines = textwrap.dedent('\n        [badbad\n        bad = bad').strip().split('\n')
    parser = configparser.ConfigParser()
    with self.assertRaises(configparser.MissingSectionHeaderError) as dse:
        parser.read_file(lines, source=b'badbad')
    self.assertEqual(str(dse.exception), "File contains no section headers.\nfile: b'badbad', line: 1\n'[badbad'")
