# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_dis_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        del sys.last_traceback
    except AttributeError:
        pass
    try:
        1 / 0
    except Exception as e:
        tb = e.__traceback__
        sys.last_traceback = tb
    tb_dis = self.get_disassemble_as_string(tb.tb_frame.f_code, tb.tb_lasti)
    self.do_disassembly_test(None, tb_dis)
