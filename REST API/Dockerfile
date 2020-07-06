FROM continuumio/miniconda3

ADD enviroment.yml /tmp/enviroment.yml
RUN conda env create -f /tmp/enviroment.yml

RUN echo "source activate $(head -1 /tmp/enviroment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/enviroment.yml | cut -d' ' -f2)/bin:$PATH

COPY * /app/
WORKDIR /app/
