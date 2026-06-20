# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: HexFloatTestCase_test_invalid_inputs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    invalid_inputs = ['infi', '-Infinit', '++inf', '-+Inf', '--nan', '+-NaN', 'snan', 'NaNs', 'nna', 'an', 'nf', 'nfinity', 'inity', 'iinity', '0xnan', '', ' ', 'x1.0p0', '0xX1.0p0', '+ 0x1.0p0', '- 0x1.0p0', '0 x1.0p0', '0x 1.0p0', '0x1 2.0p0', '+0x1 .0p0', '0x1. 0p0', '-0x1.0 1p0', '-0x1.0 p0', '+0x1.0p +0', '0x1.0p -0', '0x1.0p 0', '+0x1.0p+ 0', '-0x1.0p- 0', '++0x1.0p-0', '--0x1.0p0', '+-0x1.0p+0', '-+0x1.0p0', '0x1.0p++0', '+0x1.0p+-0', '-0x1.0p-+0', '0x1.0p--0', '0x1.0.p0', '0x.p0', '0x1,p0', '0x1pa', '0x1p０', '０x1p0', '0x１p0', '0x1.０p0', '0x1p0 \n 0x2p0', '0x1p0\x00 0x1p0']
    for x in invalid_inputs:
        try:
            result = fromHex(x)
        except ValueError:
            pass
        else:
            self.fail('Expected float.fromhex(%r) to raise ValueError; got %r instead' % (x, result))
