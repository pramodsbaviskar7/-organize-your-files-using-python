#!/usr/bin/env python
# coding: utf-8

# In[8]:



import os

location = r"C:\Users\pramo\deepblue\Untitled Folder 1"

all_files = os.listdir(location)
all_fext = []

#split all file extensions from the dir

for f in all_files:
  _, fext = os.path.splitext(f)
  if fext not in all_fext:
      all_fext.append(fext)
print(all_fext)

#create all dirs to organise files

for ext in all_fext:  
  
  if ext:
      os.mkdir(os.path.join(location, ext))

#move all files to their respective dirs

for f in all_files:
  _, ext = os.path.splitext(f)
  old_path = os.path.join(location, f)
  new_path = os.path.join(location, ext, f)
  os.rename(old_path, new_path)


# In[ ]:




