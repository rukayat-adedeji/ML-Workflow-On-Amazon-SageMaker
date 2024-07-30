# Scones Unlimited Image Classification Project

## Overview

This project demonstrates the use of AWS SageMaker, Lambda, and Step Functions to create an end-to-end machine learning workflow for image classification. The goal is to classify images of various objects and monitor the model's performance.

## Table of Contents
- [Project Overview](#overview)
- [Architecture](#architecture)
- [Implementation](#implementation)
- [Testing and Evaluation](#testing-and-evaluation)
- [Visualization](#visualization)
- [Conclusion](#conclusion)

## Architecture

The project leverages the following AWS services:
- **AWS S3**: Storage for the dataset and model artifacts.
- **AWS SageMaker**: Training and deployment of the image classification model.
- **AWS Lambda**: Serverless functions for preprocessing, invoking the model, and filtering inferences.
- **AWS Step Functions**: Orchestrates the workflow of Lambda functions.

## Implementation

### 1. Data Preparation

- Images were stored in S3 buckets: `train/` and `test/`.
- Image data was serialized using a Lambda function and stored in base64 format.

### 2. Model Training

- A convolutional neural network (CNN) model was trained using SageMaker.
- Training parameters included:
  - `image_shape`: `3,32,32`
  - `num_classes`: `2` (selected bicycles and motocycles from CIFAR-10 dataset)
  - `num_training_samples`: `1000`

### 3. Deployment

- The trained model was deployed as an endpoint using SageMaker.
- DataCaptureConfig was used to enable monitoring of the endpoint.

### 4. Lambda Functions

- **serializeImageData**: Reads an image from S3, encodes it in base64, and returns the encoded data.
- **classifyImage**: Decodes the image, invokes the SageMaker endpoint, and returns the inferences.
- **filterLowConfidence**: Filters out inferences that do not meet a predefined confidence threshold.

### 5. Step Functions Workflow

- The Step Functions workflow orchestrates the Lambda functions:
  1. **serializeImageData**: Fetches and encodes the image data.
  2. **classifyImage**: Sends the encoded image to the SageMaker endpoint for inference.
  3. **filterLowConfidence**: Ensures only high-confidence inferences are passed downstream.

<div style="display: flex; justify-content: space-between;">
    <img src="./screenshots/stepfunctions_graph.png" alt="Step Functions Workflow" style="width: 45%;">
    <img src="./screenshots/stepfunction-success-run.png" alt="Step Function in action" style="width: 45%;">
</div>


## Testing and Evaluation

- Several executions were performed using test images.
- The outputs were analyzed to ensure the workflow behaved as expected, passing high-confidence inferences and failing low-confidence ones.

## Visualization

- Model performance was monitored using various visualizations:
  - **Confidence Scatter Plot**: Shows the confidence levels of recent inferences with a threshold line.

  - **Bar Plot of Inferences Above and Below Threshold**: Count inferences above and below the threshold.
  
  - **Histogram of Inference Confidences**: Shows the distribution of confidence values from the inferences.
  
## Conclusion

This project successfully demonstrates an end-to-end machine learning pipeline using AWS services. The solution:
- Automates the workflow from data preparation to inference.
- Ensures model predictions are filtered for confidence.
- Provides visual monitoring of model performance.

This pipeline can be extended to accommodate more complex models and larger datasets, making it a robust solution for scalable machine learning deployments.
