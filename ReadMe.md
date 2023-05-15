What is this repo for?

        This data process is to extract data from landing s3 bucket to a target bucket and add tags to the data

How to set up the project?

    Install and deply all requirements.txt package that not provide by AWS lambda:pytz,dotenv

    Create s3 bucket as staging bucket:target_bucker to store
    the data from landing bucket
    
    Create AWS lambda functioin to do the above data process

    Set . s3 readonly accesee   and  . lambdaBasicExecutionRole   two permission to lambda 

    Add s3 landing s3 bucket as Trigger for lambda

    Add lambda code to  aws lambda code area, test it successfully , then Save and Deploy

    