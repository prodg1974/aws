import click
import boto3
import botocore

@click.command()
@click.argument('file_name')
@click.argument('bucket_name', default='bucket-psr-jupyter')
def main(file_name,bucket_name):
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket_name).download_file(file_name, file_name)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
if __name__ == "__main__":
    main()

