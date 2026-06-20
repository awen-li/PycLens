# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue1267

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (mod, encoding, _) in self.test_strings:
        (fp, filename, info) = imp.find_module('module_' + mod, self.test_path)
        with fp:
            self.assertNotEqual(fp, None)
            self.assertEqual(fp.encoding, encoding)
            self.assertEqual(fp.tell(), 0)
            self.assertEqual(fp.readline(), '# test %s encoding\n' % encoding)
    (fp, filename, info) = imp.find_module('tokenize')
    with fp:
        self.assertNotEqual(fp, None)
        self.assertEqual(fp.encoding, 'utf-8')
        self.assertEqual(fp.tell(), 0)
        self.assertEqual(fp.readline(), '"""Tokenization help for Python programs.\n')
