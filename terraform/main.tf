terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "init_devops_image" {
  name = "init-terrafrom-docker:terraform"

  build {
    context = ".."
  }
}

resource "docker_container" "init_devops_container" {
  name  = "init-terrafrom-docker-container-01"
  image = docker_image.init_devops_image.image_id

  ports {
    internal = 5000
    external = 5000
  }

  restart = "unless-stopped"
}