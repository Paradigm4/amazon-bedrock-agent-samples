```sh
docker build -t streamlit .
docker run -p 8501:8501 --volume ~/.aws:/root/.aws -e AWS_PROFILE=SSO-MV-FullAccess-PermissionSet-872515275464 -e BOT_NAME="scXpress agent (senshark)" streamlit .
```
