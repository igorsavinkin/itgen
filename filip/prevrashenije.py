import pickle
data =["RUSSIA","CANADA","CHINA",
       "UNITED STATES OF AMERICA"
       ,"BRAZIL", "AUSTRALIJA",
       "INDIJA","ARGENTINA",
       "KAZAKHSTAN"]
bytestream = pickle.dumps(data)
print(bytestream)
