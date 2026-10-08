/**
 * JavaScript source fixture for repository AI keyword scanner QA.
 *
 * Intentionally contains non-functional provider/package patterns.
 * No credentials, API keys or production endpoints are included.
 */

const aiIntegrations = {
  openai: "import openai",
  tensorflow: "import tensorflow",
  pytorch: "import pytorch",
  mlflow: "import mlflow",
  wandb: "import wandb",
  clarifai: "import clarifai",
  bigml: "import bigml",
  fritz: "import fritz",
  mlrun: "import mlrun",

  azureMachineLearning: "from azureml.core import Workspace",
  mindsdb: "from mindsdb import Predictor",
  h2oDriverlessAI: "from h2oai_client import Client",

  bedrock: "service_name='bedrock-runtime'",
  bedrockClient: "boto3.client('bedrock')",

  graphcore: "device::IPU:0",
  grid: "grid.run",
  weightsAndBiases: "wandb.login",

  dialogflow: "com.google.cloud.dialogflow",
  dataRobot: "com.datarobot",
  witAi: "com.facebook.witai",
  seldon: "io.seldon.",
  rapidMiner: "com.rapidminer"
};

export function getAiScannerFixtures() {
  return Object.entries(aiIntegrations);
}
