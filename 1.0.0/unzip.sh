#!/bin/bash

#unzip.sh $zipFile $zipSummary $__new_file_path__ $zipSummary.id

zipFile=$1
zipSummary=$2
newFilePath=$3
fileID=$4

ls > $zipSummary
unzip $zipFile 2>&1 >> $zipSummary
for file in $( grep -i Inflating $zipSummary | awk '{print $2}' )
do
   echo cp $file $newFilePath/primary_${fileID}_${file}_visible_txt
   cp $file $newFilePath/primary_${fileID}_${file}_visible_txt
done 

