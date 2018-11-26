import click
import boto3

@click.command()
@click.argument('file_name')
@click.argument('bucket_name', default='bucket-psr-jupyter')
def main(file_name,bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)
if __name__ == "__main__":
    main()

