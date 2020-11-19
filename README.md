# Tosci Texts

The script expects to find a dictionary in a file called `people_data.py` with this structure:
```
people = {
        'Haylee':     {'phone_number':'+18883334444', 
                        'faves':['Butter Mint Chip', 'Roxbury Pudding Stone']},
        ...
}
```

This is now running on AWS Lambda. In order to make this run there, you need to make a layer with the dependencies in `requirements.txt` and `people_data.py` included. This is how you should make your layer for AWS: `https://dev.to/razcodes/how-to-create-a-lambda-layer-in-aws-106m`.

To update the `people_data.py`:
1. Update `people_data.py` at `tosci_texts/aws-lambda-layer/lambda-layer/python/lib/python3.8/site-packages/people_data.py` with the new people.
2. Rezip folder: `zip aws-lambda-layer/lambda-layer.zip aws-lambda-layer/lambda-layer -r`
3. Upload zip to AWS Lambda Layer by creating a new version of your existing layer.
4. Update layer in the Lambda function to new version.

