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
            "command": "docker ps"
        },
        {
            "description": "List all containers (including stopped containers)",
            "command": "docker ps -a"
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
    ]
}
