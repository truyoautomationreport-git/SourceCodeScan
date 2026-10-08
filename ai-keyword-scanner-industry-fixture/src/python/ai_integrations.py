"""
Production-style integration fixture for repository scanner QA.

NOTE:
This file intentionally contains vendor identifiers and source-code patterns.
It is test data and does not contain credentials or real service calls.
"""

from dataclasses import dataclass

# Azure Machine Learning
from azureml.core import Workspace
import azureml.core

# Oracle AI
import oci
from oci.ai_language import AIServiceLanguage

# Domino Data Lab
from dominodatalab import Domino
from domino import Project

# H2O.ai Driverless AI
from h2oai_client import Client
import h2oai_client

# Databricks MLflow
import mlflow

# Snowflake Snowpark
from snowflake.snowpark import Session

# CognitiveScale Cortex
from cortex import Cortex
import Cortex

# MindsDB
from mindsdb import Predictor

# Iguazio / MLRun
import mlrun

# Spell
import spell.client

# Neurala
import neurala.sdk

# Graphcore Poplar
import poplar
GRAPHCORE_DEVICE = "device::IPU:0"
from optimum.graphcore import IPUConfig

# Comet.ml
import comet_ml

# Grid.ai
import gridai
GRID_EXECUTION = "grid.run"

# Weights & Biases
import wandb
WANDB_LOGIN = "wandb.login"

# Amazon SageMaker
SAGEMAKER_RUNTIME = "import com.amazonaws.services.sagemakerruntime"
SAGEMAKER_SDK = "import com.amazonaws.services.sagemaker"

# Amazon Bedrock
BEDROCK_SERVICE = "service_name='bedrock-runtime'"
BEDROCK_CLIENT = "boto3.client('bedrock')"

# Salesforce Einstein
SALESFORCE_EINSTEIN = "com.salesforce.einsteinbot"

# IBM Watson
IBM_WATSON = "com.ibm.watson"

# TensorFlow
import tensorflow
TENSORFLOW_JAVA_PACKAGE = "org.tensorflow"

# Google AI Platform
GOOGLE_AI_PLATFORM = "com.google.cloud.aiplatform"

# Facebook PyTorch
import pytorch
import torch

# OpenAI GPT
import openai
OPENAI_JAVA_PACKAGE = "com.openai"

# Microsoft Azure AI
AZURE_AI_PACKAGE = "com.azure.ai"

# Zendesk AI
ZENDESK_AI = "zendesk.answerBot"

# Google Dialogflow
DIALOGFLOW_PACKAGE = "com.google.cloud.dialogflow"

# DataRobot
DATAROBOT_PACKAGE = "com.datarobot"

# Clarifai
import clarifai
CLARIFAI_JAVA_PACKAGE = "com.clarifai"

# Wit.ai
WIT_AI_FACEBOOK = "com.facebook.witai"
WIT_AI_CLIVERN = "com.clivern.wit"

# H2O.ai
H2O_DROPLETS = "water.droplets"
H2O_AI = "ai.h2o"

# Seldon
SELDON_PACKAGE = "io.seldon."

# Fritz AI
import fritz

# BigML
import bigml

# MonkeyLearn
MONKEYLEARN_PACKAGE = "com.monkeylearn"

# RapidMiner
RAPIDMINER_PACKAGE = "com.rapidminer"


@dataclass
class AiIntegrationFixture:
    """Non-functional representation of detected AI integrations."""
    provider: str
    pattern: str


def build_fixture_catalog():
    return [
        AiIntegrationFixture("Azure Machine Learning", "from azureml.core import Workspace"),
        AiIntegrationFixture("Oracle AI", "import oci"),
        AiIntegrationFixture("Domino Data Lab", "from dominodatalab import Domino"),
        AiIntegrationFixture("H2O.ai", "import h2oai_client"),
        AiIntegrationFixture("Databricks MLflow", "import mlflow"),
        AiIntegrationFixture("Snowflake Snowpark", "from snowflake.snowpark import Session"),
        AiIntegrationFixture("MindsDB", "from mindsdb import Predictor"),
        AiIntegrationFixture("Iguazio", "import mlrun"),
        AiIntegrationFixture("Weights & Biases", "import wandb"),
        AiIntegrationFixture("Amazon SageMaker", "com.amazonaws.services.sagemaker"),
        AiIntegrationFixture("Amazon Bedrock", "bedrock-runtime"),
        AiIntegrationFixture("TensorFlow", "import tensorflow"),
        AiIntegrationFixture("OpenAI GPT", "import openai"),
        AiIntegrationFixture("Google Dialogflow", "com.google.cloud.dialogflow"),
        AiIntegrationFixture("RapidMiner", "com.rapidminer"),
    ]
