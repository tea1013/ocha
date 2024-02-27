#/bin/bash
RYE_VERSION=0.27.0
curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash
source "$HOME/.rye/shims"
rye config --set-bool behavior.use-uv=true
