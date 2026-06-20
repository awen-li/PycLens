# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestProcessTokens_test_with_correct_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TemporaryPyFile(SOURCE_CODES['error_free']) as file_path:
        with open(file_path) as f:
            tabnanny.process_tokens(tokenize.generate_tokens(f.readline))
        self.assertFalse(MockNannyNag.called)
