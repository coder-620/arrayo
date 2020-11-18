"""
ARRAYO EXAMPLE
"""
from os import remove as rem;
import arrayo

my_arr=[2,True,100,False,"things and stuff",212.2356];
arrayo.save("example",my_arr,True);
arrayo.write(my_arr);
del my_arr;

my_arr=arrayo.get("example");
arrayo.write(my_arr);

rem("example.arr");
