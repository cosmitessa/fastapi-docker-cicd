variable "resource_group_name" {
    description = "The name of the resource group where the container registry will be created."
    type = string
}

variable "tags" {
  description = "A map of tags to assign to the container registry."
  type = map
}

variable "location" {
  description = "The location to deploy resources in."
  type = string
}

variable "container_registry_name" {
    description = "The name of the container registry to create."
  type = string
}