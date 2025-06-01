import os
import random
import subprocess
from datetime import datetime, timedelta

REPO_SSH = "git@github.com:AVINASH34/eti_game.git"
USER_NAME = "Avinash34"
USER_EMAIL = "avinash.g.devops@gmail.com"
TOTAL_COMMITS = 100
START_DATE = datetime(2021, 6, 20)
END_DATE = datetime(2021, 9, 30)
REPO_DIR = "eti_game"

COMMIT_MESSAGES = [
    "init dockerfile setup 🐳",
    "fix pip install flag",
    "add jenkinsfile 🧪",
    "typo in k8s file",
    "update README formatting",
    "refactor game logic",
    "fix entrypoint",
    "optimize requirements install",
    "restructure directory",
    "remove debug print",
    "ci/cd fixes",
    "re-add missing file",
    "yaml indentation fix",
    "bugfix: crash on maze read",
    "docker CMD fix",
    "test case added",
    "added azure pipeline",
    "reword commit message 😅"
]

FILES = {
    "Dockerfile": [
        'FROM python:3.9-slim\n',
        'WORKDIR /app\n',
        'COPY . /app\n',
        'RUN pip install requirements.txt\n',  # <-- mistake
        'CMD ["python", "game.py"]\n'  # <-- possible mistake
    ],
    "Jenkinsfile": [
        "pipeline {\n",
        "    agent any\n",
        "    stages {\n",
        "        stage('Build') {\n",
        "            steps { sh 'docker build -t eti_game .' }\n",
        "        }\n",
        "    }\n",
        "}\n"
    ],
    "azure-pipelines.yml": [
        "trigger:\n",
        "  - main\n",
        "pool:\n",
        "  vmImage: 'ubuntu-latest'\n",
        "steps:\n",
        "  - script: echo 'Build step here'\n"
    ],
    "k8s/deployment.yaml": [
        "apiVersion: apps/v1\n",
        "kind: Deployment\n",
        "metadata:\n",
        "  name: eti-game\n",
        "spec:\n",
        "  replicas: 2\n",
        "  selector:\n",
        "    matchLabels:\n",
        "      app: eti-game\n",
        "  template:\n",
        "    metadata:\n",
        "      labels:\n",
        "        app: eti-game\n",
        "    spec:\n",
        "      containers:\n",
        "      - name: eti-game\n",
        "        image: eti_game:latest\n",
        "        ports:\n",
        "        - containerPort: 80\n"
    ]
}


def run(cmd):
    subprocess.run(cmd, check=True)


def setup_repo():
    if os.path.exists(REPO_DIR):
        run(["rm", "-rf", REPO_DIR])
    run(["git", "clone", REPO_SSH])
    os.chdir(REPO_DIR)
    run(["git", "config", "user.name", USER_NAME])
    run(["git", "config", "user.email", USER_EMAIL])


def get_random_dates():
    total_days = (END_DATE - START_DATE).days
    selected_days = sorted(random.sample(range(total_days), TOTAL_COMMITS))
    return [START_DATE + timedelta(days=d) for d in selected_days]


def write_random_file():
    file_choice = random.choice(list(FILES.keys()))
    os.makedirs(os.path.dirname(file_choice), exist_ok=True)
    with open(file_choice, 'a') as f:
        line = random.choice(FILES[file_choice])
        f.write(line)
    return file_choice


def make_commit(commit_date):
    file = write_random_file()
    run(["git", "add", file])
    msg = random.choice(COMMIT_MESSAGES)
    env = {
        **os.environ,
        "GIT_COMMITTER_DATE": commit_date.isoformat(),
        "GIT_AUTHOR_DATE": commit_date.isoformat()
    }
    run(["git", "commit", "-m", msg], env=env)


def main():
    setup_repo()
    for date in get_random_dates():
        make_commit(date)
    run(["git", "push", "origin", "main"])


if __name__ == "__main__":
    main()
