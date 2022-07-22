import pickle
data = ["Russia", "Canada", "China",  
        "United States", "Brazil", "Australia",  
        "India", "Argentina", "Kazakhstan"]  

bytestream = pickle.dumps(data)
print(bytestream)
normal_data = pickle.loads(bytestream)
print(normal_data)
