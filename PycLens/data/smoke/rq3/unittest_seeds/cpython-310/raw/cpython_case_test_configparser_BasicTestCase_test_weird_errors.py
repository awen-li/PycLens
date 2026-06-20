# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_weird_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig()
    cf.add_section('Foo')
    with self.assertRaises(configparser.DuplicateSectionError) as cm:
        cf.add_section('Foo')
    e = cm.exception
    self.assertEqual(str(e), "Section 'Foo' already exists")
    self.assertEqual(e.args, ('Foo', None, None))
    if self.strict:
        with self.assertRaises(configparser.DuplicateSectionError) as cm:
            cf.read_string(textwrap.dedent("                    [Foo]\n                    will this be added{equals}True\n                    [Bar]\n                    what about this{equals}True\n                    [Foo]\n                    oops{equals}this won't\n                ".format(equals=self.delimiters[0])), source='<foo-bar>')
        e = cm.exception
        self.assertEqual(str(e), "While reading from '<foo-bar>' [line  5]: section 'Foo' already exists")
        self.assertEqual(e.args, ('Foo', '<foo-bar>', 5))
        with self.assertRaises(configparser.DuplicateOptionError) as cm:
            cf.read_dict({'Bar': {'opt': 'val', 'OPT': 'is really `opt`'}})
        e = cm.exception
        self.assertEqual(str(e), "While reading from '<dict>': option 'opt' in section 'Bar' already exists")
        self.assertEqual(e.args, ('Bar', 'opt', '<dict>', None))
