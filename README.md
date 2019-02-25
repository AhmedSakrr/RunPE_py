# RunPE py

因為想玩玩用python呼叫C的function以及想玩玩執行在memory中的程式，就結合一起玩喽~

## ctypes

### build
`mingw32-gcc -shared -fPIC RunPE.cpp -o RunPE.dll`  

### Note
Build的bit要對應相同bit的python  

## basic

目前會發生Segmentation fault  

### build
`python setup.py build_ext --inplace`  


## Reference

[如Py似C：Python 與 C 的共生法則](https://medium.com/pyladies-taiwan/如py似c-python-與-c-的共生法則-568add0ba5b8)  
[RunPE: How to hide code behind a legit process](https://www.adlice.com/runpe-hide-code-behind-legit-process/)  
[codecrack3/Run-PE---Run-Portable-Executable-From-Memory](https://github.com/codecrack3/Run-PE---Run-Portable-Executable-From-Memory)  
[RE for Beginngers](https://www.begin.re/the-workshop?fbclid=IwAR2pdyq8amDbqn2MNq8knMo73da6FZ_UHySEIBPQcTlPlaB4RTmZwOlEAtU)  
[Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html)  
