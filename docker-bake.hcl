# Builds one channel's image. The workflow checks out the server fork into ./server (with its
# wheel in server/dist) and puts the frontend wheel into ./ha/image before running bake.

variable "IMAGE" {}
variable "CHANNEL" {}
variable "APP_VERSION" {}
variable "MASS_VERSION" {}
variable "MASS_REVISION" {}
variable "BASE_IMAGE_VERSION" {}
variable "SERVER_REF" {}
variable "FRONTEND_REF" {}
variable "SOURCE_URL" {}

target "server" {
  context    = "server"
  dockerfile = "Dockerfile"
  platforms  = ["linux/amd64", "linux/arm64"]
  args = {
    MASS_VERSION       = MASS_VERSION
    MASS_REVISION      = MASS_REVISION
    MASS_WHEEL_SHA256  = ""
    BASE_IMAGE_VERSION = BASE_IMAGE_VERSION
  }
}

target "app" {
  context    = "ha/image"
  dockerfile = "Dockerfile"
  contexts = {
    server = "target:server"
  }
  platforms = ["linux/amd64", "linux/arm64"]
  args = {
    APP_VERSION  = APP_VERSION
    MASS_VERSION = MASS_VERSION
    CHANNEL      = CHANNEL
    SERVER_REF   = SERVER_REF
    FRONTEND_REF = FRONTEND_REF
    SOURCE_URL   = SOURCE_URL
  }
  tags = ["${IMAGE}:${APP_VERSION}", "${IMAGE}:${CHANNEL}"]
  output = ["type=registry"]
}
