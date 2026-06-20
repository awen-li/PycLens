# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_code_page_decode_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    for cp in (50220, 50221, 50222, 50225, 50227, 50229, *range(57002, 57011 + 1), 65000):
        if is_code_page_present(cp):
            self.assertEqual(codecs.code_page_decode(cp, b'abc'), ('abc', 3), f'cp{cp}')
        elif support.verbose:
            print(f'  skipping cp={cp}')
    self.assertEqual(codecs.code_page_decode(42, b'abc'), ('\uf061\uf062\uf063', 3))
