FROM python:3.11-slim

ARG USER_ID
ARG USER_NAME
ENV HOME=/home/${USER_NAME} \
    VIRTUAL_ENV=/home/${USER_NAME}/venv
ENV \
  PYTHONUNBUFFERED=1 \
  DEBIAN_FRONTEND=noninteractive \
  TZ=Europe/London \
  PATH="${HOME}/.local/bin:${VIRTUAL_ENV}/bin:${PATH}" \
  PYTHONPATH="/app:${PYTHONPATH}" \
  BUILD_POETRY_LOCK="${HOME}/poetry.lock.build"
ENV IS_USING_IMAGE_RUNTIME=True


RUN apt-get -qq update \
    && apt-get -qq -y install vim gcc curl git build-essential libb64-dev software-properties-common \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq -y clean

RUN addgroup --system --gid ${USER_ID} ${USER_NAME} \
    && useradd --system -m --no-log-init --home-dir ${HOME} --uid ${USER_ID} --gid ${USER_NAME} --groups ${USER_NAME} ${USER_NAME}

RUN chown -R ${USER_NAME}:${USER_NAME} ${HOME}
RUN mkdir -p /app && chown -R ${USER_NAME}:${USER_NAME} /app /tmp

USER ${USER_NAME}
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4
ENV PATH="${HOME}/.local/bin:$PATH"

COPY pyproject.toml *.lock /app/
WORKDIR /app

RUN poetry config virtualenvs.create false 
RUN python3.11 -m venv ${VIRTUAL_ENV}
RUN pip install --upgrade pip setuptools 
RUN poetry install 
RUN cp poetry.lock ${BUILD_POETRY_LOCK}
RUN rm -rf ${HOME}/.cache/*

RUN pip install pysqlite3-binary

USER root
COPY ./docker/scripts/* /
RUN chown -R ${USER_NAME} /*.sh && chmod +x /*.sh
USER ${USER_NAME}

COPY . /app/
CMD ["/startup-script.sh"]



