package com.qa.scanner.fixtures;

/**
 * Industry-style Java fixture for repository AI keyword scanner QA.
 *
 * The values below intentionally represent scanner patterns.
 * No external service is called and no credentials are used.
 */
public final class AiServiceIntegrations {

    // Amazon SageMaker
    private static final String SAGEMAKER =
            "import com.amazonaws.services.sagemaker";
    private static final String SAGEMAKER_RUNTIME =
            "import com.amazonaws.services.sagemakerruntime";

    // Amazon Bedrock
    private static final String BEDROCK =
            "service_name='bedrock-runtime'";

    // IBM Watson
    private static final String IBM_WATSON =
            "com.ibm.watson";

    // Salesforce Einstein
    private static final String SALESFORCE_EINSTEIN =
            "com.salesforce.einsteinbot";

    // Google AI Platform
    private static final String GOOGLE_AI_PLATFORM =
            "com.google.cloud.aiplatform";

    // Google Dialogflow
    private static final String DIALOGFLOW =
            "com.google.cloud.dialogflow";

    // Microsoft Azure AI
    private static final String AZURE_AI =
            "com.azure.ai";

    // OpenAI GPT
    private static final String OPENAI =
            "com.openai";

    // TensorFlow
    private static final String TENSORFLOW =
            "org.tensorflow";

    // Clarifai
    private static final String CLARIFAI =
            "com.clarifai";

    // Wit.ai
    private static final String WIT_AI =
            "com.facebook.witai";

    // Seldon
    private static final String SELDON =
            "io.seldon.";

    // MonkeyLearn
    private static final String MONKEYLEARN =
            "com.monkeylearn";

    // RapidMiner
    private static final String RAPIDMINER =
            "com.rapidminer";

    public static String[] allPatterns() {
        return new String[] {
            SAGEMAKER,
            SAGEMAKER_RUNTIME,
            BEDROCK,
            IBM_WATSON,
            SALESFORCE_EINSTEIN,
            GOOGLE_AI_PLATFORM,
            DIALOGFLOW,
            AZURE_AI,
            OPENAI,
            TENSORFLOW,
            CLARIFAI,
            WIT_AI,
            SELDON,
            MONKEYLEARN,
            RAPIDMINER
        };
    }

    private AiServiceIntegrations() {
        // Utility class.
    }
}
