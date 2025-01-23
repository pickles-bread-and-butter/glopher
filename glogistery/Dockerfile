FROM golang:1.23 as base

WORKDIR /glogistery

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .
COPY ./glogistery_config.yaml /root/
COPY ./glogistery_manifest.yaml /root/

RUN go build .

FROM base as running

CMD ["./glogistery"]
