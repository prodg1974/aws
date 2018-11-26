import click
import boto3
#import botocore

@click.command()
#@click.argument('file_name')
@click.argument('bucket_name', default='bucket-psr-jupyter')
def main(bucket_name):
    s3 = boto3.client('s3')
    website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
    }
    s3.put_bucket_website(
        Bucket='bucket_name',
        WebsiteConfiguration=website_configuration
    )
if __name__ == "__main__":
    main()

