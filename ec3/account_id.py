import urllib2, json
import boto3
import botocore.exceptions
from ec3.exceptions import CredentialError


# see https://gist.github.com/gene1wood/6d4974b7503336d642c9

def get_account_id_on_ec2_instance():
    response = json.loads(urllib2.urlopen(
        'http://169.254.169.254/latest/meta-data/iam/info/',
        None,
        1
    ).read())
    return response['InstanceProfileArn'].split(':')[4]

def get_account_id_from_iam(**boto_kwargs):
    # We're not on an ec2 instance but have api keys, get the account
    # id from the user ARN
    try:
        return boto3.client('iam', **boto_kwargs).get_user()['User']['Arn'].split(':')[4]
    except botocore.exceptions.NoCredentialsError as err:
        raise CredentialError(err)
    except botocore.exceptions.ClientError as err:
        raise CredentialError(err)

def get_account_id(**boto_kwargs):
    try:
        return get_account_id_on_ec2_instance()
    except urllib2.URLError:
        return get_account_id_from_iam(**boto_kwargs)
