# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_mkdir_with_unknown_drive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for d in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
        p = self.cls(d + ':\\')
        if not p.is_dir():
            break
    else:
        self.skipTest("cannot find a drive that doesn't exist")
    with self.assertRaises(OSError):
        (p / 'child' / 'path').mkdir(parents=True)
