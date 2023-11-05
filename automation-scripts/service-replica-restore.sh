#!/bin/bash

SOURCE=../deploy/kubernetes/manifests/overlays
CLUSTER1='local-cluster'
CLUSTER2='os-aws-sno'
FILENAME='kustomization.yaml'

DEPLOYMENT_NAME = $1

if [ -f $SOURCE/$CLUSTER1/$FILENAME -a -f $SOURCE/$CLUSTER2/$FILENAME ]; then
    echo "Updating $CLUSTER1/$FILENAME"
    python3 ./yaml-kustomization-cleaner.py $SOURCE/$CLUSTER1/$FILENAME $DEPLOYMENT_NAME

    echo "Updating $CLUSTER1/$FILENAME"
    python3 ./yaml-kustomization-cleaner.py $SOURCE/$CLUSTER2/$FILENAME $DEPLOYMENT_NAME

    echo "Committing on repo"
    git add $SOURCE/$CLUSTER1/$FILENAME
    git add $SOURCE/$CLUSTER2/$FILENAME
    git commit -m 'Edited $SOURCE/$CLUSTER1/$FILENAME and $SOURCE/$CLUSTER2/$FILENAME'
    git push -f
else
    echo "File $FILENAME does not exist."
    exit 1
fi

