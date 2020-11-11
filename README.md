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

