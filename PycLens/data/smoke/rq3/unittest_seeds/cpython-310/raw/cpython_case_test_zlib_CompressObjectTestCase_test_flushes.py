# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_flushes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sync_opt = ['Z_NO_FLUSH', 'Z_SYNC_FLUSH', 'Z_FULL_FLUSH', 'Z_PARTIAL_FLUSH']
    ver = tuple((int(v) for v in zlib.ZLIB_RUNTIME_VERSION.split('.')))
    if ver >= (1, 2, 5, 3):
        sync_opt.append('Z_BLOCK')
    sync_opt = [getattr(zlib, opt) for opt in sync_opt if hasattr(zlib, opt)]
    data = HAMLET_SCENE * 8
    for sync in sync_opt:
        for level in range(10):
            try:
                obj = zlib.compressobj(level)
                a = obj.compress(data[:3000])
                b = obj.flush(sync)
                c = obj.compress(data[3000:])
                d = obj.flush()
            except:
                print('Error for flush mode={}, level={}'.format(sync, level))
                raise
            self.assertEqual(zlib.decompress(b''.join([a, b, c, d])), data, 'Decompress failed: flush mode=%i, level=%i' % (sync, level))
            del obj
