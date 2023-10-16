"""
    Python to product an index.html page of Megaw legacy materials.
"""
import os
import datetime

PAGE_FILENAME = "index.html"
TOP_DIR       = "Programs"

BEGIN = """<!DOCTYPE html>
<html>
    <head>
        <title>Megaw</title>
    </head>
    <body>
        <header>
            <div style="text-align:center;">
                <h1>Programs of The Original Megaw Theatre (1974-1987)</h1>
            </div>
        </header>
        <p>
         This page contains a partial collection of the original programs created to support The Megaw Theatre
         shows.  The Megaw Theatre was a 99 seat equity weaver theatre that was open from 1974 to 1987
         and located in Northridge, CA.  After the Megaw closed it's doors in California the founders 
         (Sydney May Morrison and Elaine EE Moe) reinvented the theatre as 
         <a href="https://megawtheatreinc.com/">The Megaw Theatre and Acting Studio, Inc.</a> - relocating to
         Scottsdale, AZ. For the unfamilliar, a theatre that has only 99 seats can be exempt from paying
         union actors. Thus The Megaw Theatre was an all volunteer effort of professionals
         performing (without pay) in the productions. This page is a temporary location of a partial
         collection of programs.  The programs where graciously supplied by JoAnn Iaccino (formally JoAnna
         Mashall). JoAnn designed the original Megaw logo and many of the programs. The programs where
         scanned and placed on this web page by Leonard (Lenny) Reder.  Lenny spent a couple years at
         Megaw as a young man assisting with and learning all about technical theatre (e.g. set construction,
         stage lighting, etc.).<br><br>

         Megaw Theatre opened it's doors in April of 1974 with the production
         of "Little Mary Sunshine". This was almost 50 years ago.  It is my hope to grow
         this web page with production photographs and other information into a 50th.
         anniversary Megaw Theatre legacy page. The goal of the page is to preserve the
         memory for the many people that worked at The Megaw Theatre.<br><br>

         Finally I would be remiss if I did not mension two people I personnally and foundly
         remember who have passed away and are no longer with us - Sydney Morrison and Dave Lukas.
         Sydney May Morrison (Syd) the executive producer and founder of Megaw.  Syd one summer
         day in 1974 interviewed me (a junior in high school) to particapate at the Megaw as a
         technical theatre apprentice which was the beginning of a couple years of learning.  Syd 
         was my advocate at Megaw and taught me about work.  Dave Lukas, an extrodonary
         theatrical set designer and scenic carpetar, would be my first true mentor. I have
         life long memories of Dave and myself in 1976 working almost daily hammering out set
         after set at that little theatre in Northridge. For the uninitiated you will notice
         these two individuals names along with Elaine (EE) Moe in every single program listed.
         EE is the ultimate expert on everything theatrical and is still actively teaching acting.
         Everyone misses Syd and Dave who knew and worked with them at Megaw.<br><br>
         
         Leonard J. Reder<br>
         Email: <a href = "mailto: reder@ieee.org">reder@ieee.org</a><br>
         Last Updated: $DATE$<br>
         </p>
        <h2>Programs (in alphabetic order not chronological):</h2>
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
    # get today's date
    today = datetime.date.today()
    today = today.strftime("%B %d, %Y")
    print(today)
    # get list of sub-directories
    dir_name_list = os.listdir(TOP_DIR)
    # get list of file names
    file_list = filename_list(dir_name_list)
    #
    # open page file for writing
    #
    with open(PAGE_FILENAME, 'w') as f:
        b = BEGIN.replace("$DATE$",today)
        f.write(b)

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