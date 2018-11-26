import boto3
import click

@click.command()
@click.argument('bucket_name')
def main(bucket_name):
    s3 = boto3.client('s3')

    # Call to S3 to retrieve the policy for the given bucket
    result = s3.get_bucket_acl(Bucket=bucket_name)
    click.echo(result)
if __name__ == '__main__':
    pass
    #main()
