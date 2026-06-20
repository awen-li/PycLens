# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestFormatWitnesses_test_format_witnesses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [('Test', 'at tab sizes T, e, s, t'), ('', 'at tab size '), ('t', 'at tab size t'), ('  t  ', 'at tab sizes  ,  , t,  ,  ')]
    for (words, expected) in tests:
        with self.subTest(words=words, expected=expected):
            self.assertEqual(tabnanny.format_witnesses(words), expected)
