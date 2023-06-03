<div align="center">

# [ Bucket Anti-Cheat ]
### [ About project ]
B.A.C (Bucket Anti-Cheat) - is a python solution, that protect your application from DLL injection.  
### [ How it works? ]
During DLL injection process, additional annotations are added to the used application DLL's libraries. 
My solution does not let this happen and after detection new annotations kills your application and closes. Please, install libraries from `requirements.txt`
### [ Arguments ]
Usage: `[-h] [--protect] apppath logspath` 
  ```
- `-h` Shows help page 
- `--protect` Enable protection mode, by default logs generation mode  
- `apppath` Path to your application (.exe file), required
- `logspath` Path of logs file, required
 ```
</div>
