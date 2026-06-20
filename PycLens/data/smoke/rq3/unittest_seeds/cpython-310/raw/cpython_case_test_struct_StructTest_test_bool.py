# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ExplodingBool(object):

        def __bool__(self):
            raise OSError
    for prefix in tuple('<>!=') + ('',):
        false = ((), [], [], '', 0)
        true = ([1], 'test', 5, -1, 4294967295 + 1, 4294967295 / 2)
        falseFormat = prefix + '?' * len(false)
        packedFalse = struct.pack(falseFormat, *false)
        unpackedFalse = struct.unpack(falseFormat, packedFalse)
        trueFormat = prefix + '?' * len(true)
        packedTrue = struct.pack(trueFormat, *true)
        unpackedTrue = struct.unpack(trueFormat, packedTrue)
        self.assertEqual(len(true), len(unpackedTrue))
        self.assertEqual(len(false), len(unpackedFalse))
        for t in unpackedFalse:
            self.assertFalse(t)
        for t in unpackedTrue:
            self.assertTrue(t)
        packed = struct.pack(prefix + '?', 1)
        self.assertEqual(len(packed), struct.calcsize(prefix + '?'))
        if len(packed) != 1:
            self.assertFalse(prefix, msg='encoded bool is not one byte: %r' % packed)
        try:
            struct.pack(prefix + '?', ExplodingBool())
        except OSError:
            pass
        else:
            self.fail('Expected OSError: struct.pack(%r, ExplodingBool())' % (prefix + '?'))
    for c in [b'\x01', b'\x7f', b'\xff', b'\x0f', b'\xf0']:
        self.assertTrue(struct.unpack('>?', c)[0])
