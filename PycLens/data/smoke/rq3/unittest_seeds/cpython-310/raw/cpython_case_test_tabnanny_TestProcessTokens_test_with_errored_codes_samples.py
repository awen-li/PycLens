# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestProcessTokens_test_with_errored_codes_samples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for key in ['tab_space_errored_1', 'tab_space_errored_2']:
        with self.subTest(key=key):
            with TemporaryPyFile(SOURCE_CODES[key]) as file_path:
                with open(file_path) as f:
                    tokens = tokenize.generate_tokens(f.readline)
                    with self.assertRaises(tabnanny.NannyNag):
                        tabnanny.process_tokens(tokens)
