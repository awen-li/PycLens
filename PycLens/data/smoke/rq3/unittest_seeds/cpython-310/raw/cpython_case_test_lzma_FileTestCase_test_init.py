# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        pass
    with LZMAFile(BytesIO(), 'w') as f:
        pass
    with LZMAFile(BytesIO(), 'x') as f:
        pass
    with LZMAFile(BytesIO(), 'a') as f:
        pass
