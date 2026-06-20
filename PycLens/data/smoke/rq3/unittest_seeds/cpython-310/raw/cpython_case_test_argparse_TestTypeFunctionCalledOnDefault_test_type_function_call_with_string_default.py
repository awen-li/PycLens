# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestTypeFunctionCalledOnDefault_test_type_function_call_with_string_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(int_to_convert):
        return 'foo_converted'
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', type=spam, default='0')
    args = parser.parse_args([])
    self.assertEqual(NS(foo='foo_converted'), args)
