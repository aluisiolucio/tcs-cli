docker_data: dict = {
    "images": [
        {
            "description": "Build an Image from a Dockerfile",
            "command": "docker build -t <image_name>"
        },
        {
            "description": "List all images",
            "command": "docker images"
        },
        {
            "description": "Remove an image",
            "command": "docker rmi <image_name>"
        }
    ],
    "containers": [
        {
            "description": "Run a container",
            "command": "docker run <image_name>"
        },
        {
            "description": "List all containers",
            "command": "docker container ls"
        },
        {
            "description": "List all containers (including stopped containers)",
            "command": "docker container ls -a"
        },
        {
            "description": "Stop a container",
            "command": "docker stop <container_id>"
        },
        {
            "description": "Remove a container",
            "command": "docker rm <container_id>"
        },
        {
            "description": "Remove all containers",
            "command": "docker rm $(docker ps -a -q)"
        }
    ],
    "networks": [
        {
            "description": "List all networks",
            "command": "docker network ls"
        },
        {
            "description": "Create a network",
            "command": "docker network create <network_name>"
        },
        {
            "description": "Remove a network",
            "command": "docker network rm <network_name>"
        }
    ],
    "volumes": [
        {
            "description": "List all volumes",
            "command": "docker volume ls"
        },
        {
            "description": "Create a volume",
            "command": "docker volume create <volume_name>"
        },
        {
            "description": "Remove a volume",
            "command": "docker volume rm <volume_name>"
        }
    ],
    "logs": [
        {
            "description": "View the logs of a container",
            "command": "docker logs <container_id>"
        }
    ],
    "exec": [
        {
            "description": "Execute a command in a running container",
            "command": "docker exec -it <container_id> <command>"
        }
    ],
    "stats": [
        {
            "description": "Display a live stream of container(s) resource usage statistics",
            "command": "docker stats <container_id>"
        }
    ],
    "inspect": [
        {
            "description": "Return low-level information on Docker objects",
            "command": "docker inspect <object_id>"
        }
    ],
    "prune": [
        {
            "description": "Remove all unused containers, networks, images (both dangling and unreferenced), and volumes",
            "command": "docker system prune"
        }
    ]
}
