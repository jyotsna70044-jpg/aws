FROM public.ecr.aws/lambda/python:3.11
LABEL authors="jyotsna"
 # Copy and install dependencies
WORKDIR ${LAMBDA_TASK_ROOT}
#COPY requirements.txt .
#RUN pip install -r requirements.txt --target .
COPY lambda_function.py .
CMD ["lambda_function.handler"]