# app/Dockerfile

FROM python:3.9-slim

# working directory. Named same as repo
WORKDIR /resume_gen_ai

# update a apt-get (package manager in linux) and install git, curl and others build essentials. 
# remove/delete the unwanted libraries at the end to keep the container lightweight.
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# clone in case of public repo and do ssh in case of private repo.
RUN git clone https://github.com/anurag-code/gen-ai-resume.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Use ENTRYPOINT to run the specified script
ENTRYPOINT ["streamlit", "run", "python_scripts/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
