import os
import sys
import gzip
import tarfile
import re

#ordner = "%s" % sys.argv[1]
datei = "%s" % sys.argv[1]
dateiname = datei
#print dateiname
with open(dateiname, "r") as f:
        t  = tarfile.open(dateiname + ".tar", "w")

        for line in f:
               line = line.strip()
               #ignore lines starting with r"#EXT"
               if (re.search(r"#EXT", line)):
                       continue
               #line now contains a path
               pfad = line
               print pfad
               t.add(pfad)
        
        
f.closed
      
