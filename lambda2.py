import json
import sagemaker
import base64

ENDPOINT = 'image-classification-2024-07-28-10-57-25-791'

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    # Instantiate a Predictor
    sagemaker_session = sagemaker.Session()
    predictor = sagemaker.predictor.Predictor(
        endpoint_name=ENDPOINT,
        sagemaker_session=sagemaker_session
    )
    predictor.serializer = sagemaker.serializers.IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image)
    
    # We return the data back to the Step Function    
    event["body"]["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': event['body']
    }