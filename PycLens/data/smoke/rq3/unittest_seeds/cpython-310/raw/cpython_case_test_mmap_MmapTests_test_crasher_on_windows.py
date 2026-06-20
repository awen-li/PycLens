# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_crasher_on_windows

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = mmap.mmap(-1, 1000, tagname='foo')
    try:
        mmap.mmap(-1, 5000, tagname='foo')[:]
    except:
        pass
    m.close()
    with open(TESTFN, 'wb') as fp:
        fp.write(b'x' * 10)
    f = open(TESTFN, 'r+b')
    m = mmap.mmap(f.fileno(), 0)
    f.close()
    try:
        m.resize(0)
    except:
        pass
    try:
        m[:]
    except:
        pass
    m.close()
