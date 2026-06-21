# Lambda IAM for lambda_start_fargate.py

A Lambda has an **execution role** with two parts: a *trust policy* (who can assume
it = the Lambda service) and *permission policies* (what it can do).

## 1) Trust policy (lets Lambda assume the role)
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "lambda.amazonaws.com" },
    "Action": "sts:AssumeRole"
  }]
}
```
```bash
aws iam create-role --role-name forecast-lambda-role \
  --assume-role-policy-document file://trust.json
aws iam attach-role-policy --role-name forecast-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

## 2) Permission policy (run a Fargate task + pass the task roles)
`iam:PassRole` is the subtle one: to launch a task that uses
`ecsTaskExecutionRole`/`forecast-task-role`, Lambda must be allowed to *pass*
those roles to ECS.
```json
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow", "Action": ["ecs:RunTask"], "Resource": "*" },
    { "Effect": "Allow", "Action": ["iam:PassRole"],
      "Resource": [
        "arn:aws:iam::ACCOUNT_ID:role/ecsTaskExecutionRole",
        "arn:aws:iam::ACCOUNT_ID:role/forecast-task-role"
      ] }
  ]
}
```
```bash
aws iam put-role-policy --role-name forecast-lambda-role \
  --policy-name run-fargate --policy-document file://perm.json
```
