output "resource_group_name" {
    description = "The name of the resource group where the container registry is created."
    value = azurerm_container_registry.acr.resource_group_name
}



output "container_registry_name" {
    description = "The name of the container registry created."
    value = azurerm_container_registry.acr.name
}