# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_widths

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (opcode, opname) in enumerate(dis.opname):
        if opname in ('BUILD_MAP_UNPACK_WITH_CALL', 'BUILD_TUPLE_UNPACK_WITH_CALL', 'JUMP_IF_NOT_EXC_MATCH'):
            continue
        with self.subTest(opname=opname):
            width = dis._OPNAME_WIDTH
            if opcode < dis.HAVE_ARGUMENT:
                width += 1 + dis._OPARG_WIDTH
            self.assertLessEqual(len(opname), width)
