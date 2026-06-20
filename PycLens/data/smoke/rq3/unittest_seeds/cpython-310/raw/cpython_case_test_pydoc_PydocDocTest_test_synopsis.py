# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_synopsis

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(unlink, TESTFN)
    for encoding in ('ISO-8859-1', 'UTF-8'):
        with open(TESTFN, 'w', encoding=encoding) as script:
            if encoding != 'UTF-8':
                print('#coding: {}'.format(encoding), file=script)
            print('"""line 1: hé', file=script)
            print('line 2: hi"""', file=script)
        synopsis = pydoc.synopsis(TESTFN, {})
        self.assertEqual(synopsis, 'line 1: hé')
