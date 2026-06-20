# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_disassemble_instance_method_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    method_bytecode = _C(1).__init__.__code__.co_code
    self.do_disassembly_test(method_bytecode, dis_c_instance_method_bytes)
