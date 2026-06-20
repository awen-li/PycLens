# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_disassemble_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(expected, **kwargs):
        dis = self.get_disassembly(_h, **kwargs)
        dis = self.strip_addresses(dis)
        self.assertEqual(dis, expected)
    check(dis_nested_0, depth=0)
    check(dis_nested_1, depth=1)
    check(dis_nested_2, depth=2)
    check(dis_nested_2, depth=3)
    check(dis_nested_2, depth=None)
    check(dis_nested_2)
