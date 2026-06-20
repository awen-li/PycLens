# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: FileHandlerTest_test_emit_after_closing_in_write_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.unlink(self.fn)
    fh = logging.FileHandler(self.fn, encoding='utf-8', mode='w')
    fh.setFormatter(logging.Formatter('%(message)s'))
    fh.emit(self.next_rec())
    fh.close()
    fh.emit(self.next_rec())
    with open(self.fn) as fp:
        self.assertEqual(fp.read().strip(), '1')
