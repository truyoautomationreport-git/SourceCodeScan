# AI Keyword Scanner - Industry Test Repository

This repository is a QA test fixture for validating repository/source-code AI keyword
detection.

## Purpose

The source files intentionally contain representative AI/ML package names, imports,
service references, namespaces and code patterns that a repository scanner can detect.

This is **test data**, not production AI application code. Some vendor/package
references are included only because they are detection patterns configured in the
scanner.

## Structure

```text
src/
  python/
    ai_integrations.py
  java/
    AiServiceIntegrations.java
  javascript/
    ai-integrations.js
  typescript/
    ai-integrations.ts
scanner-fixtures/
  keyword-catalog.txt
tests/
  README.md
```

## Expected QA Result

A repository scan should identify AI-related patterns including:

- Azure Machine Learning
- Oracle AI
- Domino Data Lab
- H2O.ai / Driverless AI
- Databricks MLflow
- Snowflake Snowpark
- CognitiveScale Cortex
- MindsDB
- Iguazio / MLRun
- Spell
- Neurala
- Graphcore Poplar
- Comet.ml
- Grid.ai
- Weights & Biases
- Amazon SageMaker
- Amazon Bedrock
- Salesforce Einstein
- IBM Watson
- TensorFlow
- Google AI Platform
- PyTorch
- OpenAI GPT
- Microsoft Azure AI
- Zendesk AI
- Google Dialogflow
- DataRobot
- Clarifai
- Wit.ai
- Seldon
- Fritz AI
- BigML
- MonkeyLearn
- RapidMiner

## Important

All values in this repository are non-secret test strings. Do not add real API keys,
credentials, customer data, production URLs, or tokens.
