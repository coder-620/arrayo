"""
.arr = ARRAY FILE
THIS PROGRAM OPENS .arr FILES
IT ALSO COMES WITH SOME USEFUL ARRAY TOOLS
"""
def string(arr=[]):
    st="";
    for s in arr:
        st+=str(s);
    return st;
##########################
def write(arr=[],dim=1):
    if dim == 1:
        print("1D ARRAY");
        i=0;
        for data in arr:
            try:
                print(f"{i} | {data}");
            except:
                pass;
            i+=1;
    elif dim == 2:
        print("2D ARRAY")
        i=0;
        for arr2 in arr:
            i2=0;
            s=f"At {i}:\n\t";
            for data in arr2:
                s+=f"{i2} : {data}, ";
                i2+=1;
            s=s[:-2];
            string(s);
            print(s)
            i+=1;
##########################
def assist():
    print(open("arrayohelp.txt","r").read());
    print();
##########################
def get(name="example"):
    try:
        fn=name+".arr";
        txt=open(fn,"r").readlines()[0][1:-1];
        txt=txt.split(",");
        newArr=[];
        for t in txt:
            err=False;
            if t == "True":
                typ="BOOLTRUE";
            elif t=="False":
                typ="BOOLFALSE";
            elif "\"" in t or "\'" in t:
                typ="STRING";
            elif "." in t:
                typ="FLOAT";
            else:
                typ="NUM";
            if typ=="BOOLTRUE":
                t=True;
            elif typ=="BOOLFALSE":
                t=False;
            elif typ=="STRING":
                t=string(t[2:-1]);
            elif typ=="FLOAT":
                try:
                    t=float(t);
                except:
                    err=True;
            elif typ=="INT":
                try:
                    t=int(t);
                except:
                    err=True;
            if err:
                t=None;
            newArr.append(t);
        return newArr;
    except FileNotFoundError:
        print("FILE NOT FOUND!")
    print();
##########################
def save(name="example",arr=[],overwrite=True):
    fn=name+".arr";
    fileExists=False;
    try:
        open(fn,"x");
    except FileExistsError:
        fileExists=True;
        print("THE FILE ALREADY EXISTS");
    if not fileExists or overwrite:
        file=open(fn,"w");
        file.write(str(arr));
        if fileExists:
            print("FILE OVERWRITTEN");
        else:
            print("FILE CREATED");
    else:
        print("FILE WAS NOT SAVED");
    print();
##########################
print("Thank you for using Arrayo.");
print("Use 'arrayo.assist()' for help on Arrayo.");
print();
