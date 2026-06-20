# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_callbacks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def handler1(exc):
        r = range(exc.start, exc.end)
        if isinstance(exc, UnicodeEncodeError):
            l = ['<%d>' % ord(exc.object[pos]) for pos in r]
        elif isinstance(exc, UnicodeDecodeError):
            l = ['<%d>' % exc.object[pos] for pos in r]
        else:
            raise TypeError("don't know how to handle %r" % exc)
        return ('[%s]' % ''.join(l), exc.end)
    codecs.register_error('test.handler1', handler1)

    def handler2(exc):
        if not isinstance(exc, UnicodeDecodeError):
            raise TypeError("don't know how to handle %r" % exc)
        l = ['<%d>' % exc.object[pos] for pos in range(exc.start, exc.end)]
        return ('[%s]' % ''.join(l), exc.end + 1)
    codecs.register_error('test.handler2', handler2)
    s = b'\x00\x81\x7f\x80\xff'
    self.assertEqual(s.decode('ascii', 'test.handler1'), '\x00[<129>]\x7f[<128>][<255>]')
    self.assertEqual(s.decode('ascii', 'test.handler2'), '\x00[<129>][<128>]')
    self.assertEqual(b'\\u3042\\u3xxx'.decode('unicode-escape', 'test.handler1'), 'あ[<92><117><51>]xxx')
    self.assertEqual(b'\\u3042\\u3xx'.decode('unicode-escape', 'test.handler1'), 'あ[<92><117><51>]xx')
    self.assertEqual(codecs.charmap_decode(b'abc', 'test.handler1', {ord('a'): 'z'})[0], 'z[<98>][<99>]')
    self.assertEqual('güßrk'.encode('ascii', 'test.handler1'), b'g[<252><223>]rk')
    self.assertEqual('güß'.encode('ascii', 'test.handler1'), b'g[<252><223>]')
