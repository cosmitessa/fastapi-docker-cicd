
data "azurerm_resource_group" "rg" {
  name = "rg-projects-dev-sa"
}

module "acr" {
  source = "./modules/acr"

  resource_group_name     = data.azurerm_resource_group.rg.name
  location                = data.azurerm_resource_group.rg.location
  container_registry_name = var.container_registry_name
  tags                    = local.common_tags
}