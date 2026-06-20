# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: CTokenizerBufferTests_test_newline_at_the_end_of_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_script = f"        #coding: latin-1\n        #{'a' * 10000}\n        #{'a' * 10002}"
    with os_helper.temp_dir() as temp_dir:
        file_name = make_script(temp_dir, 'foo', test_script)
        run_test_script(file_name)
