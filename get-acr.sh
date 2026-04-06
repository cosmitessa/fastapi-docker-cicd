# Get your ACR resource ID
ACR_ID=$(az acr show --name acrprojectssadev --query id -o tsv)

# Create service principal with AcrPush permission
az ad sp create-for-rbac \
  --name "github-actions-acr-push" \
  --role "AcrPush" \
  --scopes $ACR_ID \
  --sdk-auth

# Save the JSON output - you'll need it for GitHub Secrets