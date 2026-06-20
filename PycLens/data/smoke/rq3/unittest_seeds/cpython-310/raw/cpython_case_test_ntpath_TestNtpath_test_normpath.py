# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_normpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester("ntpath.normpath('A//////././//.//B')", 'A\\B')
    tester("ntpath.normpath('A/./B')", 'A\\B')
    tester("ntpath.normpath('A/foo/../B')", 'A\\B')
    tester("ntpath.normpath('C:A//B')", 'C:A\\B')
    tester("ntpath.normpath('D:A/./B')", 'D:A\\B')
    tester("ntpath.normpath('e:A/foo/../B')", 'e:A\\B')
    tester("ntpath.normpath('C:///A//B')", 'C:\\A\\B')
    tester("ntpath.normpath('D:///A/./B')", 'D:\\A\\B')
    tester("ntpath.normpath('e:///A/foo/../B')", 'e:\\A\\B')
    tester("ntpath.normpath('..')", '..')
    tester("ntpath.normpath('.')", '.')
    tester("ntpath.normpath('')", '.')
    tester("ntpath.normpath('/')", '\\')
    tester("ntpath.normpath('c:/')", 'c:\\')
    tester("ntpath.normpath('/../.././..')", '\\')
    tester("ntpath.normpath('c:/../../..')", 'c:\\')
    tester("ntpath.normpath('../.././..')", '..\\..\\..')
    tester("ntpath.normpath('K:../.././..')", 'K:..\\..\\..')
    tester("ntpath.normpath('C:////a/b')", 'C:\\a\\b')
    tester("ntpath.normpath('//machine/share//a/b')", '\\\\machine\\share\\a\\b')
    tester("ntpath.normpath('\\\\.\\NUL')", '\\\\.\\NUL')
    tester("ntpath.normpath('\\\\?\\D:/XY\\Z')", '\\\\?\\D:/XY\\Z')
