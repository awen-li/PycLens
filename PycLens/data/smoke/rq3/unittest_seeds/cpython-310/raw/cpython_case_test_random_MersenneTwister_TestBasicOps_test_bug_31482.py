# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_bug_31482

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.gen.seed(b'nofar', version=1)
    self.assertEqual([self.gen.random().hex() for i in range(4)], ['0x1.8645314505ad7p-1', '0x1.afb1f82e40a40p-5', '0x1.2a59d2285e971p-1', '0x1.56977142a7880p-6'])
    self.gen.seed(b'rachel', version=1)
    self.assertEqual([self.gen.random().hex() for i in range(4)], ['0x1.0b294cc856fcdp-1', '0x1.2ad22d79e77b8p-3', '0x1.3052b9c072678p-2', '0x1.578f332106574p-3'])
    self.gen.seed(b'', version=1)
    self.assertEqual([self.gen.random().hex() for i in range(4)], ['0x1.b0580f98a7dbep-1', '0x1.84129978f9c1ap-1', '0x1.aeaa51052e978p-2', '0x1.092178fb945a6p-2'])
    b = b'\x00 @`\x80\xa0\xc0\xe0\xf0'
    self.gen.seed(b, version=1)
    self.assertEqual([self.gen.random().hex() for i in range(4)], ['0x1.52c2fde444d23p-1', '0x1.875174f0daea4p-2', '0x1.9e9b2c50e5cd2p-1', '0x1.fa57768bd321cp-2'])
