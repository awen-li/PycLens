# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: StdPrinterTests_test_disallow_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = self.STDOUT_FD
    printer = self.create_printer(fd)
    support.check_disallow_instantiation(self, type(printer))
