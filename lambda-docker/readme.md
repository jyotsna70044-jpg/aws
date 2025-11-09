# create virtual env
python3 -m venv aws_env
source aws_env/bin/activate
pip install pandas pyarrow awswrangler
pip3 freeze>requirements.txt
# build and test image
docker build -t s3tos3 .
docker images
# push in ecr
aws ecr create-repository --repository-name lambda/s3tos3

# Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS CLI:
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 412040338345.dkr.ecr.ap-south-1.amazonaws.com
# Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built:
docker build -t lambda/s3tos3 . --provenance=false 
docker build --platform linux/amd64 -t lambda/s3tos3 .
# After the build completes, tag your image so you can push the image to this repository:
docker tag lambda/s3tos3:latest 412040338345.dkr.ecr.ap-south-1.amazonaws.com/lambda/s3tos3:latest
# Run the following command to push this image to your newly created AWS repository:
docker push 412040338345.dkr.ecr.ap-south-1.amazonaws.com/lambda/s3tos3:latest