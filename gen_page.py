"""
    Python to product an index.html page of Megaw legacy materials.
"""
import os

PAGE_FILENAME = "index.html"
TOP_DIR       = "Programs"

BEGIN = """<!DOCTYPE html>
<html>
    <head>
        <title>Megaw</title>
    </head>
    <body>
        <h2>Programs (in Alphabetic order not chronological):</h2>
        <ol>
"""
END = """
        </ol>
    </body>
</html>
"""

def convert_to_filename(dir_name):
    """
    Takes dir as argument ABC_DEF_GHI directory name
    and convert to filename of form Abc_Def_Ghi.
    @return filename
    """
    filename = ""
    # Get list of words from directory name
    tword = dir_name.split("_")
    # Convert to filename with proper case
    # Make string to return
    for w in tword:
        filename += w.lower()[0].upper() + w.lower()[1:] + "_"
    filename = filename.strip("_")
    return filename

def filename_list(dir_names):
    """
    For input list of directory names
    return list of file names.
    """
    filename_list = list()
    
    # find all the filenames
    for p in dir_names:
        filename=""
        filename=convert_to_filename(p)
        filename_list.append(filename)
    #  
    return filename_list


def main():
    """
    Main function to open a file for html page
    and write all the stuff into it.
    """
    global PAGE_FILENAME
    global TOP_DIR
    # get list of sub-directories
    dir_name_list = os.listdir(TOP_DIR)
    # get list of file names
    file_list = filename_list(dir_name_list)
    #
    # open page file for writing
    #
    with open(PAGE_FILENAME, 'w') as f:
        
        f.write(BEGIN)
        
        i = 0
        for d in dir_name_list:
            filename = file_list[i]
            title    = " ".join(filename.split("_"))
            rec = "            <a href=\"Programs" + os.sep + d + os.sep + filename + ".pdf\">" + title + "</a><br>\n"
            f.write("            <li>\n")
            f.write(rec)
            f.write("            </li>\n")
            i+=1
        
        f.write(END)

if __name__ == "__main__":
    main()