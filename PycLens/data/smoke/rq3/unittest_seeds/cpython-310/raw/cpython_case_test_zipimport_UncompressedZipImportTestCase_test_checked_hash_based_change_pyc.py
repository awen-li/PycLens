# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipimport.py
# case: UncompressedZipImportTestCase_test_checked_hash_based_change_pyc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = b"state = 'old'"
    source_hash = importlib.util.source_hash(source)
    bytecode = importlib._bootstrap_external._code_to_hash_pyc(compile(source, '???', 'exec'), source_hash, False)
    files = {TESTMOD + '.py': (NOW, "state = 'new'"), TESTMOD + '.pyc': (NOW - 20, bytecode)}

    def check(mod):
        self.assertEqual(mod.state, 'new')
    self.doTest(None, files, TESTMOD, call=check)
