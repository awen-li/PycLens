# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureDefinitions_test_base_class_have_text_signature

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test.ann_module7 import BufferedReader

    class MyBufferedReader(BufferedReader):
        """buffer reader class."""
    text_signature = BufferedReader.__text_signature__
    self.assertEqual(text_signature, '(raw, buffer_size=DEFAULT_BUFFER_SIZE)')
    sig = inspect.signature(MyBufferedReader)
    self.assertEqual(str(sig), '(raw, buffer_size=8192)')
