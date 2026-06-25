# decompyle3 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.20 (default, Sep  7 2024, 18:35:08) 
# [GCC 11.4.0]
# Embedded file name: data/rq3/cpython-3.8/unittest_seeds/raw/cpython_case_test_threading_InterruptMainTests_test_interrupt_main_mainthread.py

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
while1stmt ::= \e__come_froms . c_stmts COME_FROM JUMP_LOOP COME_FROM_LOOP
while1stmt ::= \e__come_froms . c_stmts COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . c_stmts JUMP_LOOP \e__come_froms POP_BLOCK
whileTruestmt ::= \e__come_froms . c_stmts JUMP_LOOP _come_froms POP_BLOCK
whileTruestmt38 ::= \e__come_froms . c_stmts JUMP_LOOP COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . c_stmts JUMP_LOOP \e__come_froms
whileTruestmt38 ::= \e__come_froms . c_stmts JUMP_LOOP _come_froms
whileTruestmt38 ::= \e__come_froms . pass JUMP_LOOP
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_LOOP
whilestmt38 ::= \e__come_froms . bool_op c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . bool_op c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms . testexpr \e_c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms . testexprc \e_c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . testexprc \e_c_stmts_opt come_froms JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms . testexprc c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . testexprc c_stmts_opt come_froms JUMP_LOOP _come_froms
Instruction context:
-> 
 L.   5         0  JUMP_FORWARD         19  'to 19'
                   2  BINARY_RSHIFT    
                   4  CALL_FUNCTION_0       0  '0 positional arguments'
                   6  STORE_NAME               __pybcsec_seed__
