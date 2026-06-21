# config.example.sh — copy to config.sh and fill in YOUR values, then: source config.sh
# config.sh is gitignored (never commit real names/IDs). The Python labs read these env vars.
#
#   cp config.example.sh config.sh && nano config.sh && source config.sh

# --- Core ---
export AWS_PROFILE="learn"                            # SAFETY: always use the personal-account profile,
                                                     # never the company 'default'. See projects/SETUP-personal-aws.md
export AWS_REGION="ap-south-1"                       # Mumbai; pick the region closest to you
export FORECAST_BUCKET="milan-forecast-lab"          # must be GLOBALLY unique — add your name/date

# --- EC2 (filled in as you create them in Module 3) ---
export KEY_NAME="forecast-key"                        # the EC2 key pair name (for SSH)
export SECURITY_GROUP_ID="sg-xxxxxxxx"               # SG allowing SSH (22) from YOUR ip only
export SUBNET_ID=""                                   # optional; blank = default subnet
export INSTANCE_TYPE="t3.micro"                       # free-tier eligible
export IAM_INSTANCE_PROFILE="forecast-worker-profile" # role the instance assumes (S3 access, no keys)

# --- Tagging (so you can find & delete everything) ---
export PROJECT_TAG="forecast"

# AMI is looked up automatically (latest Ubuntu 24.04) by the scripts via SSM —
# no need to hardcode an ami-id.
