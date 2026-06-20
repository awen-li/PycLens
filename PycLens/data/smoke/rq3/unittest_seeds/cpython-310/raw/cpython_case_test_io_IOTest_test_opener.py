# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_opener

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'w', encoding='utf-8') as f:
        f.write('egg\n')
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)

    def opener(path, flags):
        return fd
    with self.open('non-existent', 'r', encoding='utf-8', opener=opener) as f:
        self.assertEqual(f.read(), 'egg\n')
