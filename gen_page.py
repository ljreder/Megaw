"""
    Python to product an index.html page of Megaw legacy materials.
"""
import os

top_dir = "Programs"

program_list = os.listdir(top_dir)

program_name_list = list()

# find all the names
for p in program_list:
    name=""
    # list of words
    t = p.split("_")
    # convert to proper case and make string name
    for i in t:
        name += i.lower()[0].upper() + i.lower()[1:] + "_"
    name = name.strip("_")
    program_name_list.append(name)
#  
print(program_name_list)

HEADER = """
<!DOCTYPE html>
<html>
   <head>
      <title>Megaw test page</title>
   </head>
   <body>
"""
END = """
   </body>
</html>
"""
i = 0
for prog in program_list:
    filename = program_name_list[i]
    title    = " ".join(filename.split("_"))
    rec = "<a href=\"Programs" + os.sep + prog + os.sep + filename + ".pdf>\"" + title + "</a><br>"
    print(rec)
    i+=1    

