/**
 * TypeScript source fixture for repository AI keyword scanner QA.
 */

export interface AiKeywordFixture {
  provider: string;
  pattern: string;
}

export const AI_KEYWORD_FIXTURES: AiKeywordFixture[] = [
  { provider: "Azure Machine Learning", pattern: "import azureml.core" },
  { provider: "Oracle AI", pattern: "import oci" },
  { provider: "Domino Data Lab", pattern: "from domino import Project" },
  { provider: "Databricks MLflow", pattern: "import mlflow" },
  { provider: "Snowflake Snowpark", pattern: "from snowflake.snowpark import Session" },
  { provider: "MindsDB", pattern: "from mindsdb import Predictor" },
  { provider: "Iguazio", pattern: "import mlrun" },
  { provider: "Spell", pattern: "import spell.client" },
  { provider: "Neurala", pattern: "import neurala.sdk" },
  { provider: "Comet.ml", pattern: "import comet_ml" },
  { provider: "Grid.ai", pattern: "import gridai" },
  { provider: "Amazon Bedrock", pattern: "boto3.client('bedrock')" },
  { provider: "TensorFlow", pattern: "org.tensorflow" },
  { provider: "Google AI Platform", pattern: "com.google.cloud.aiplatform" },
  { provider: "OpenAI GPT", pattern: "com.openai" },
  { provider: "Zendesk AI", pattern: "zendesk.answerBot" },
  { provider: "Wit.ai", pattern: "com.clivern.wit" },
  { provider: "H2O.ai", pattern: "water.droplets" },
  { provider: "BigML", pattern: "import bigml" },
  { provider: "MonkeyLearn", pattern: "com.monkeylearn" }
];

export function getFixtureCount(): number {
  return AI_KEYWORD_FIXTURES.length;
}
