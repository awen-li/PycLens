──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                  ,ggggggggggg,              ,gggg,                                                                                                   
                                 dP"""88""""""Y8,           d8" "8I                                                           ,dPYb,                                  
                                 Yb,  88      `8b           88  ,dP                                                           IP'`Yb                                  
                                  `"  88      ,8P        8888888P"     gg                                                     I8  8I                                  
                                      88aaaad8P"            88         ""                                                     I8  8'                                  
                                      88"""""gg     gg      88         gg    ,ggg,,ggg,     ,gggg,gg  gg      gg    ,gggg,gg  I8 dP                                   
                                      88     I8     8I ,aa,_88         88   ,8" "8P" "8,   dP"  "Y8I  I8      8I   dP"  "Y8I  I8dP                                    
                                      88     I8,   ,8IdP" "88P         88   I8   8I   8I  i8'    ,8I  I8,    ,8I  i8'    ,8I  I8P                                     
                                      88    ,d8b, ,d8IYb,_,d88b,,_   _,88,_,dP   8I   Yb,,d8,   ,d8I ,d8b,  ,d8b,,d8,   ,d8b,,d8b,_                                   
                                      88    P""Y88P"888"Y8P"  "Y888888P""Y88P'   8I   `Y8P"Y8888P"8888P'"Y88P"`Y8P"Y8888P"`Y88P'"Y88                                  
                                                  ,d8I'                                         ,d8I'                                                                 
                                                ,dP'8I                                        ,dP'8I                                                                  
                                               ,8"  8I                                       ,8"  8I                                                                  
                                               I8   8I                                       I8   8I                                                                  
                                               `8, ,8I                                       `8, ,8I                                                                  
                                                `Y8P"                                         `Y8P"                                                                   
                                                                                                                                                                      
                                                            The University of Texas at Dallas, Syssec Lab                                                             
                                                                    0.1.0 - https://pylingual.io                                                                      
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[20:38:32] INFO     Loading data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-e30d6d594ff2.pyc...                                                     decompiler.py:444
           ERROR    Failed to decompile data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-e30d6d594ff2.pyc                                                  main.py:134
                    ╭──────────────────────────────────────────────── Traceback (most recent call last) ─────────────────────────────────────────────────╮            
                    │ /root/PyBC-Sec/pybcSEC/data/rq2/envs/global-pylingual/lib/python3.12/site-packages/pylingual/main.py:122 in main                   │            
                    │                                                                                                                                    │            
                    │   119 │   │   │   │   raise FileNotFoundError(f"pyc file {pyc_path} does not exist")                                               │            
                    │   120 │   │   │                                                                                                                    │            
                    │   121 │   │   │   try:                                                                                                             │            
                    │ ❱ 122 │   │   │   │   result = decompile(                                                                                          │            
                    │   123 │   │   │   │   │   pyc=pyc_path,                                                                                            │            
                    │   124 │   │   │   │   │                                                                                                            │            
                    │       save_to=Path(f"{out_dir}/decompiled_{pyc_path.with_suffix('.py').name}" if out_dir else                                      │            
                    │       f"decompiled_{pyc_path.with_suffix('.py').name}"),                                                                           │            
                    │   125 │   │   │   │   │   config_file=Path(config_file) if config_file else None,                                                  │            
                    │                                                                                                                                    │            
                    │ /root/PyBC-Sec/pybcSEC/data/rq2/envs/global-pylingual/lib/python3.12/site-packages/pylingual/decompiler.py:446 in decompile        │            
                    │                                                                                                                                    │            
                    │   443 │   """                                                                                                                      │            
                    │   444 │   logger.info(f"Loading {pyc}...")                                                                                         │            
                    │   445 │   if isinstance(pyc, Path):                                                                                                │            
                    │ ❱ 446 │   │   pyc = PYCFile(pyc)                                                                                                   │            
                    │   447 │                                                                                                                            │            
                    │   448 │   # try to auto resolve version                                                                                            │            
                    │   449 │   if version is None:                                                                                                      │            
                    │                                                                                                                                    │            
                    │ /root/PyBC-Sec/pybcSEC/data/rq2/envs/global-pylingual/lib/python3.12/site-packages/pylingual/editable_bytecode/PYCFile.py:28 in    │            
                    │ __init__                                                                                                                           │            
                    │                                                                                                                                    │            
                    │   25 │   │   elif source is not None:                                                                                              │            
                    │   26 │   │   │   source_tuple = load_module(source)                                                                                │            
                    │   27 │   │                                                                                                                         │            
                    │ ❱ 28 │   │   (                                                                                                                     │            
                    │   29 │   │   │   version,                                                                                                          │            
                    │   30 │   │   │   self.timestamp,                                                                                                   │            
                    │   31 │   │   │   self.magic,                                                                                                       │            
                    ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯            
                    ValueError: too many values to unpack (expected 7)                                                                                                
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
