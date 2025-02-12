```sh
docker build -t streamlit .
docker run \
  --publish 8501:8501 \
  --volume ~/.aws:/root/.aws \ 
  --env AWS_PROFILE=SSO-MV-FullAccess-PermissionSet-872515275464 \
  --env BOT_NAME="scXpress agent (senshark)" \
  streamlit .
```
