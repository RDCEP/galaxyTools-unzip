#!/usr/bin/env python

import os
import shutil
import sys
import zipfile

#unzip.sh $zipFile $zipSummary $__new_file_path__ $zipSummary.id
zipFile = sys.argv[1]
zipSummary = sys.argv[2]
newFilePath = sys.argv[3]
fileID = sys.argv[4]

zs = open(zipSummary, 'w')
zs.write("Unzipping %s\n" % zipFile)

zf = zipfile.ZipFile(zipFile, 'r')
for member in zf.namelist():
    zs.write("Extracting %s\n" % member)
    zf.extract(member)
    (base, ext) = member.rsplit('.', 1)
    new_file_path="%s/primary_%s_%s_visible_%s" % (newFilePath, fileID, member, ext)
    shutil.copyfile(member, new_file_path)
    
zf.close()
zs.close()
