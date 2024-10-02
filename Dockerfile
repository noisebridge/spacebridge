FROM ubuntu:22.04

ARG BAZEL_VERSION=latest

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
    curl \
    python3 \
    gnupg \
    apt-transport-https

# Install bazel (https://docs.bazel.build/versions/master/install-ubuntu.html)

RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg
RUN mv bazel-archive-keyring.gpg /usr/share/keyrings
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
RUN apt update
RUN apt-get install bazel -y
