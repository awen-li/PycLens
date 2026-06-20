# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestTypeFunctionCalledOnDefault_test_no_double_type_conversion_of_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def extend(str_to_convert):
        return str_to_convert + '*'
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', type=extend, default='*')
    args = parser.parse_args([])
    self.assertEqual(NS(test='**'), args)
