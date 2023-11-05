#!/bin/bash

SOURCE=../deploy/kubernetes/manifests/base
FILENAME=31-hpa-front-end.yaml

if [ -f $SOURCE/$FILENAME ]; then
   echo "Updating $FILENAME"
   python3 ./yaml-editor.py $SOURCE/$FILENAME minReplicas $1
   python3 ./yaml-editor.py $SOURCE/$FILENAME maxReplicas $2

   echo "Committing on repo"
   git add $SOURCE/$FILENAME
   git commit -m 'Edited $FILENAME'
   git push -f
else
   echo "File $FILENAME does not exist."
   exit 1
fi

