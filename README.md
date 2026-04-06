
# Containerised FastAPI & Azure CI/CD Pipeline

This project demonstrates the transition from local Python development to a production-ready, containerised deployment. It features a high-performance FastAPI application, optimized with Multi-Stage Docker builds, and integrated into an automated CI/CD pipeline targeting Azure Container Registry (ACR).

I used `terraform-docs` to ensure the infrastructure is self-documenting. Every variable has a clear description and type, making it easy for other engineers to consume these modules as a library.

## Architecture Overview

The workflow is designed to simulate a professional enterprise software delivery lifecycle:

1. Development: Python API built with FastAPI and Pydantic V2 for strict schema validation.
2. Containerisation: Optimized Multi-Stage Dockerfile using `alpine` to reduce image size and attack surface.
3. Infrastructure: Azure Container Registry (ACR) provisioned via Terraform.
4. Automation: GitHub Actions workflow that authenticates to Azure via Service Principal to build and push the image.

## Engineering Challenges

- Image Size Optimization: Initially, using a standard Python image resulted in a large footprint. By switching to a Multi-Stage Alpine build, the image size was reduced by over 60%, speeding up deployment times.
- Action Authentication: Configured GitHub Secrets to securely pass JSON-formatted Service Principal credentials, ensuring no sensitive data is exposed in logs.

## Technical Deep Dive

### 1. High-Performance API

- FastAPI: Asynchronous Python framework for speed and automatic OpenAPI documentation.
- Pydantic Models: Strict enforcement of data types for Health and Echo endpoints.
- Production Ready: Includes a dedicated `/health` endpoint for Docker and Orchestrator health checks.

### 2. Security-Hardened Dockerization

The `Dockerfile` implements several "Mid-Level" best practices:

- Multi-Stage Build: Separation of the "Builder" (to install dependencies) from the "Runtime" (to execute code), resulting in a significantly smaller image.
- Non-Root User: The container runs as `appuser` (UID 1000) instead of `root` to mitigate potential container breakout exploits.
- Native Healthchecks: Built-in `HEALTHCHECK` instruction using `wget` for proactive container monitoring.

### 3. Infrastructure & CI/CD

- Terraform-Managed ACR: Deployed using a modular approach to ensure the registry is version-controlled.
- GitHub Actions: * Authenticates via Azure Service Principal using `AcrPush` permissions.
    - Dynamically parses secrets to handle login server and credentials securely.
    - Uses a `workflow_dispatch` trigger for controlled, manual deployment.


# Terraform Docs

```bash

terraform-docs markdown table --output-file README.md --output-mode inject .

```

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >=1.9.0 |
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | ~> 4.8.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 4.8.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_acr"></a> [acr](#module\_acr) | ./modules/acr | n/a |

## Resources

| Name | Type |
|------|------|
| [azurerm_resource_group.rg](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/resource_group) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_container_registry_name"></a> [container\_registry\_name](#input\_container\_registry\_name) | n/a | `string` | `"acrprojectsdevsa"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_container_registry_name"></a> [container\_registry\_name](#output\_container\_registry\_name) | The name of the container registry created. |
| <a name="output_resource_group_name"></a> [resource\_group\_name](#output\_resource\_group\_name) | The name of the resource group where the container registry is created. |
<!-- END_TF_DOCS -->