# Pickling 

# ✅ What is Pickling?
# Pickling is the process of serializing a Python object into a byte stream so it can be:
# Stored in a file or database,
# Transmitted over a network,
# Or reused later (e.g., saved ML models, cached API responses).
# The reverse process is called Unpickling (deserialization).
# Python provides the built-in pickle module to handle serialization and deserialization.

# | Use Case                             | Description                                       |
# | -----------------------------------  | ------------------------------------------------- |
# | ✅ Model Saving (ML/AI)              | Save trained models (e.g., `sklearn`) to disk     |
# | ✅ Caching                           | Cache heavy API responses or intermediate results |
# | ✅ IPC (Inter-process communication) | Send data between processes                       |
# | ✅ Session Storage                   | Web frameworks storing session objects            |
# | ✅ Configuration Snapshots           | Save program state/configurations                 |


# 🛠️ Basic Pickle Operations
# 1. 📝 Pickling (Serialize to file)

# import pickle

# data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'ML']}

# with open('data.pkl', 'wb') as file:
#     new = pickle.dump(data, file)   # python obj ---> byte stream
#     print(new)
# # 2. 📖 Unpickling (Deserialize from file)

# with open('data.pkl','rb') as file:
#     new1 = pickle.load(file)
#     print(new1)
    
# | Method                   | Use                                          |
# | ------------------------ | -------------------------------------------- |
# | `pickle.dump(obj, file)` | Serialize `obj` to `file`                    |
# | `pickle.load(file)`      | Deserialize object from `file`               |
# | `pickle.dumps(obj)`      | Serialize `obj` to a byte stream (in-memory) |
# | `pickle.loads(bytes)`    | Deserialize from byte stream to obj          |



# 📌 Important Concepts
# 1. Pickle File Mode
# Always use:
# 'wb' for writing (binary write)
# 'rb' for reading (binary read)

# 2. What Can Be Pickled
# ✅ Can pickle:
# Basic types: int, float, str, list, dict, tuple
# Custom classes & objects (if defined at top level)
# Functions (with limitations)
# Modules (with limitations)

# ❌ Cannot pickle:
# Open file objects
# Sockets
# Database connections
# Lambdas or local functions
# ⚠️ Always define classes and functions at the top level of a module to be pickleable.

# 📈 Real-World Example: Save a Trained Model
# from sklearn.linear_model import LogisticRegression
# import pickle

# model = LogisticRegression()
# model.fit(X_train, y_train)

# # Save the model
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# # Load the model
# with open('model.pkl', 'rb') as f:
#     loaded_model = pickle.load(f)



# | Best Practice                       | Explanation                                         |
# | ----------------------------------- | --------------------------------------------------  |
# | ✅ Use `wb`/`rb` modes               | Always read/write in binary                        |
# | ✅ Version control pickled files     | Treat them like artifacts; don’t blindly overwrite |
# | ✅ Use `with` blocks                 | Ensures files are properly closed                  |
# | ✅ Prefer JSON for simple data       | Pickle is Python-specific and unsafe               |
# | ❌ Don't unpickle untrusted data     | **Security risk** (see below)                      |
# | ✅ Document pickled object structure | Helpful for future team members                    |

# 🛡️ Security Warning
# Pickle is not secure against malicious data.
# ❗NEVER unpickle data from an untrusted source.
# Pickle can execute arbitrary code during deserialization.
# ❌ Dangerous Code Example
## import pickle

## malicious_data = b"cos\nsystem\n(S'del C:\\\\important\\\\file.txt'\ntR."
## pickle.loads(malicious_data)  # This will execute a system command!


# 📚 Alternatives to Pickle (Industry-Level Choices)

# | Tool                                | Use Case                                                       |
# | ----------------------------------- | -------------------------------------------------------------- |
# | `json`                              | Human-readable, safer, cross-platform                          |
# | `joblib`                            | Better for large numpy arrays (used in ML)                     |
# | `marshal`                           | Lower-level, used internally by Python                         |
# | `protobuf` / `Avro` / `MessagePack` | Used in high-performance, cross-language environments          |
# | `dill`                              | Can serialize more complex Python objects (but still insecure) |



# | Feature        | `pickle`                 | `json`                       |
# | -------------- | ------------------------ | -------------------------    |
# | Format         | Binary                   | Text                         |
# | Python-only?   | ✅ Yes                    | ❌ No (cross-language)     |
# | Security       | ❌ Unsafe                 | ✅ Safe                    |
# | Human-readable | ❌ No                     | ✅ Yes                     |
# | Custom objects | ✅ Yes (with limitations) | ❌ Needs manual conversion |





    
    

    





import pickle

# s = "hello world"
# y= pickle.dumps(s)  # it will converts python object into byte-stream (pickling or serialization)
# print(s)
# print(y)           #b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bhello world\x94.'
# z=pickle.dumps(y) # again we can convert the byte-stream into byte-stream
# print(z)          #b'\x80\x04\x95\x1e\x00\x00\x00\x00\x00\x00\x00C\x1a\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bhello world\x94.\x94.

# x=pickle.loads(y)  # it will convert byte-stream into python object (unpickling or deserialization )
# print(x)           # hello world
# w=pickle.loads(z)   
# print(w)           # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bhello world\x94.'
# a=pickle.loads(w)
# print(a)           #hello world



# k =['abc','def','ghi','jkl']
# with open ('one.pkl','wb') as file:
#     data=pickle.dump(k,file)    # python obj into bytestream (pickling)
# # os.popen('one.pkl')


# with open('one.pkl','rb') as file:
#     data=pickle.load(file)      #bytestream into python objj (unpickling)
#     print(data)
# os.popen('one.pkl')   
    
    
"""
without using file handling syntax :

import pickle 

1.dumps()  # python object to byte stream object
new_var = pickle.dumps(iterable)

2.loads()   # byte stream object to python object
new_var = pickle.loads(previous_var_name)

with using file handling syntax :

1. with open ('file name.pkl','wb')as file:
      new_var = pickle.dump(iterable , file)
2. with open('file name.pkl' ,'rb') as file:
      var_name = pickle.load(file)
      
"""