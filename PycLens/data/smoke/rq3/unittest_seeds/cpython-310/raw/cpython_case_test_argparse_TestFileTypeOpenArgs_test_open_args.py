# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestFileTypeOpenArgs_test_open_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    FT = argparse.FileType
    cases = [(FT('rb'), ('rb', -1, None, None)), (FT('w', 1), ('w', 1, None, None)), (FT('w', errors='replace'), ('w', -1, None, 'replace')), (FT('wb', encoding='big5'), ('wb', -1, 'big5', None)), (FT('w', 0, 'l1', 'strict'), ('w', 0, 'l1', 'strict'))]
    with mock.patch('builtins.open') as m:
        for (type, args) in cases:
            type('foo')
            m.assert_called_with('foo', *args)
