
@description('Name of the Azure AI Foundry  instance')
param accountName string


resource account 'Microsoft.CognitiveServices/accounts@2025-06-01' existing = {
  name: accountName
}



resource gpt4oDeployment 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: account
  name: 'gpt-4o'
  sku: {
    capacity: 250
    name: 'GlobalStandard'
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-4o'
      version: '2024-11-20'
    }
    versionUpgradeOption: 'OnceCurrentVersionExpired'
    raiPolicyName: 'Microsoft.DefaultV2'
  }

}

resource gpt41Deployment 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: account
  name: 'gpt-4.1'
  sku: {
    name: 'GlobalStandard'
    capacity: 152
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-4.1'
      version: '2025-04-14'
    }
    versionUpgradeOption: 'OnceNewDefaultVersionAvailable'
    raiPolicyName: 'Microsoft.DefaultV2'
  }
  dependsOn: [
    gpt4oDeployment
  ]
}

resource gpt5Deployment 'Microsoft.CognitiveServices/accounts/deployments@2025-06-01' = {
  parent: account
  name: 'gpt-5-chat'
  sku: {
    name: 'GlobalStandard'
    capacity: 430
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-5-chat'
      version: '2025-10-03'
    }
    versionUpgradeOption: 'OnceNewDefaultVersionAvailable'
    raiPolicyName: 'Microsoft.DefaultV2'
  }
  dependsOn: [
    gpt41Deployment
  ]
}

