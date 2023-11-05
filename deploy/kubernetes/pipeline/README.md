This repository contains file implementing Tekton pipeline for VEM shop frontend.
In order to run the pipeline you need two secrets containing the OCP internal image registry and bitbucket repo credentials.

The secret structure is represented below:
```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: dockerconfig-secret
stringData:
  config.json: |
    {
      "auths" : {
        "icr.io" : {
          "auth" : "sa",
          "identitytoken" : "[pipeline-sa-token]"
        }
      }
    }
---
apiVersion: v1
kind: Secret
metadata:
  name: git-credentials
data:
  id_rsa: [repo_private_key]
```

To obtain `identitytoken` follow this [guide](https://itnext.io/explore-different-methods-to-build-and-push-image-to-private-registry-with-tekton-pipelines-5cad9dec1ddc).

Once created the two secrets you can create tekton pipeline objects using:

```
kubectl apply -f pipeline.yaml
kubectl create -f pipelinerun.yaml
```


