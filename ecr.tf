resource "docker_image" "redis_python_image" {
  name = "redis_python"
  build {
    path = "."
    dockerfile = "Dockerfile"
    }
  }


# Start a container
resource "docker_container" "redis_python_container" {
  name  = "redis_python_container"
  image = docker_image.redis_python_image.latest
}


# Create a ECR repository
resource "aws_ecr_repository" "redis_python" {
  name                 = "redis_python"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}