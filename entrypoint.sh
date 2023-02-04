#!/usr/bin/env sh

chmod +x /src/scripts/process.sh
chmod +x /src/scripts/deploy.sh

cd /src/ && ./scripts/process.sh
cd /src/ && hugo

cd /src/ && ./scripts/deploy.sh
