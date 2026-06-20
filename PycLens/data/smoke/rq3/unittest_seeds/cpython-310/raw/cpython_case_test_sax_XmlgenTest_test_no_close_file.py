# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_no_close_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()

    def func(out):
        gen = XMLGenerator(out)
        gen.startDocument()
        gen.startElement('doc', {})
    func(result)
    self.assertFalse(result.closed)
