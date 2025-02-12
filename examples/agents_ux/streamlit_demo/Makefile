# Default AWS credentials profile
PROFILE?=SSO-MV-FullAccess-PermissionSet-872515275464

.PHONY: help
help: ## Show this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: check-aws-profile
check-aws-profile: ## Check if AWS profile exists
	@aws configure list-profiles | grep -q "^${PROFILE}$$" || (echo "AWS profile '${PROFILE}' does not exist. Please run 'make aws-profile' to configure AWS SSO" && exit 1)

.PHONY: aws-login
aws-login: check-aws-profile ## Call AWS SSO login to fetch temporary CLI credentials
	aws sso login --profile ${PROFILE} --no-browser

.PHONY: check-aws-login
check-aws-login: ## Check if AWS credentials are valid
	@aws sts get-caller-identity --profile ${PROFILE} > /dev/null 2>&1 || (echo "Please run 'make aws-login' to login via AWS SSO" && exit 1)


