# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_transitiveness

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = b'a'
    b = 1
    h = 255
    i = 65535
    l = 65536
    f = 3.1415
    d = 3.1415
    t = True
    for prefix in ('', '@', '<', '>', '=', '!'):
        for format in ('xcbhilfd?', 'xcBHILfd?'):
            format = prefix + format
            s = struct.pack(format, c, b, h, i, l, f, d, t)
            (cp, bp, hp, ip, lp, fp, dp, tp) = struct.unpack(format, s)
            self.assertEqual(cp, c)
            self.assertEqual(bp, b)
            self.assertEqual(hp, h)
            self.assertEqual(ip, i)
            self.assertEqual(lp, l)
            self.assertEqual(int(100 * fp), int(100 * f))
            self.assertEqual(int(100 * dp), int(100 * d))
            self.assertEqual(tp, t)
