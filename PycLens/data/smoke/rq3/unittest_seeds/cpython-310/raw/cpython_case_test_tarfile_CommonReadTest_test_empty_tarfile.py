# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommonReadTest_test_empty_tarfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tmpname, self.mode.replace('r', 'w')):
        pass
    try:
        tar = tarfile.open(tmpname, self.mode)
        tar.getnames()
    except tarfile.ReadError:
        self.fail('tarfile.open() failed on empty archive')
    else:
        self.assertListEqual(tar.getmembers(), [])
    finally:
        tar.close()
