# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_find_module_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (mod, encoding, _) in self.test_strings:
        with imp.find_module('module_' + mod, self.test_path)[0] as fd:
            self.assertEqual(fd.encoding, encoding)
    path = [os.path.dirname(__file__)]
    with self.assertRaises(SyntaxError):
        imp.find_module('badsyntax_pep3120', path)
