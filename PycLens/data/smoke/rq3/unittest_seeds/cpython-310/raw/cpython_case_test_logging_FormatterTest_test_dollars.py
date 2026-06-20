# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: FormatterTest_test_dollars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.get_record()
    f = logging.Formatter('${message}', style='$')
    self.assertEqual(f.format(r), 'Message with 2 placeholders')
    f = logging.Formatter('$message', style='$')
    self.assertEqual(f.format(r), 'Message with 2 placeholders')
    f = logging.Formatter('$$%${message}%$$', style='$')
    self.assertEqual(f.format(r), '$%Message with 2 placeholders%$')
    f = logging.Formatter('${random}', style='$')
    self.assertRaises(ValueError, f.format, r)
    self.assertFalse(f.usesTime())
    f = logging.Formatter('${asctime}', style='$')
    self.assertTrue(f.usesTime())
    f = logging.Formatter('$asctime', style='$')
    self.assertTrue(f.usesTime())
    f = logging.Formatter('${message}', style='$')
    self.assertFalse(f.usesTime())
    f = logging.Formatter('${asctime}--', style='$')
    self.assertTrue(f.usesTime())
