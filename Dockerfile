FROM python:3.10-slim

# Install C build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        make \
        libc6-dev && \
    rm -rf /var/lib/apt/lists/*

# Install fixed NumPy version
RUN pip install --no-cache-dir numpy==2.2.6\
                               matplotlib==3.10.3\
                               pycryptosat==5.11.21\
                               tqdm==4.67.1

WORKDIR /app
CMD ["bash"]