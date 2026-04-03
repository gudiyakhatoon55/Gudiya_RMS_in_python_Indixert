# import json
# import os 

# class FileHandler:

#     def __init__(self):
#         self.base_path = "app/database/"

    
#     def read_file(self, filename):
#         path = os.path.join(self.base_path, filename)

#         # File exist nahi kare to empty list return
#         if not os.path.exists(path):
#             return []

#         try:
#             with open(path, "r", encoding="utf-8") as f:
#                 return json.load(f)
#         except json.JSONDecodeError:
#             # file empty ya corrupt ho
#             return []
#         except Exception as e:
#             print(f"Error reading file: {e}")
#             return []

    
#     def write_file(self, filename, data):
#         path = os.path.join(self.base_path, filename)

#         try:
#             with open(path, "w", encoding="utf-8") as f:
#                 json.dump(data, f, indent=4)
#         except Exception as e:
#             print(f"Error writing file: {e}")

    
#     def append_file(self, filename, new_data):
#         data = self.read_file(filename)
#         data.append(new_data)
#         self.write_file(filename, data)


import json
import os


class FileHandler:

    def __init__(self):
        self.base_path = "app/database/"

    def read_file(self, filename):
        path = os.path.join(self.base_path, filename)

        if not os.path.exists(path):
            return []

        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return []

    def write_file(self, filename, data):
        path = os.path.join(self.base_path, filename)

        with open(path, "w") as f:
            json.dump(data, f, indent=4)