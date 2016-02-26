import odbchelper

def call_buildConnectionString():
    params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
    return odbchelper.buildConnectionString(params)

if __name__ == "__main__":
    print ("lab02 executing...")
    print (call_buildConnectionString())
