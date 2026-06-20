# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: HelperFunctionTest_test_subst

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    plist = ['id=1', 'number=2', 'total=3']
    test_cases = [(['', 'audio/*', 'foo.txt'], ''), (['echo foo', 'audio/*', 'foo.txt'], 'echo foo'), (['echo %s', 'audio/*', 'foo.txt'], 'echo foo.txt'), (['echo %t', 'audio/*', 'foo.txt'], None), (['echo %t', 'audio/wav', 'foo.txt'], 'echo audio/wav'), (['echo \\%t', 'audio/*', 'foo.txt'], 'echo %t'), (['echo foo', 'audio/*', 'foo.txt', plist], 'echo foo'), (['echo %{total}', 'audio/*', 'foo.txt', plist], 'echo 3')]
    for tc in test_cases:
        self.assertEqual(mailcap.subst(*tc[0]), tc[1])
