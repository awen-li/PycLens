# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asdl_parser.py
# case: TestAsdlParser_test_constructor_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ehandler = self.types['excepthandler']
    self.assertEqual(len(ehandler.types), 1)
    self.assertEqual(len(ehandler.attributes), 4)
    cons = ehandler.types[0]
    self.assertIsInstance(cons, self.asdl.Constructor)
    self.assertEqual(len(cons.fields), 3)
    f0 = cons.fields[0]
    self.assertEqual(f0.type, 'expr')
    self.assertEqual(f0.name, 'type')
    self.assertTrue(f0.opt)
    f1 = cons.fields[1]
    self.assertEqual(f1.type, 'identifier')
    self.assertEqual(f1.name, 'name')
    self.assertTrue(f1.opt)
    f2 = cons.fields[2]
    self.assertEqual(f2.type, 'stmt')
    self.assertEqual(f2.name, 'body')
    self.assertFalse(f2.opt)
    self.assertTrue(f2.seq)
