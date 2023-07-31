# DockerVolumePython

## 1. docker volume create static-files

> @blacksmithop ➜ /workspaces/DockerVolumePython (main) $ docker volume inspect static-files

```json
[
    {
        "CreatedAt": "2023-07-31T09:29:54Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/static-files/_data",
        "Name": "static-files",
        "Options": {},
        "Scope": "local"
    }
]
```