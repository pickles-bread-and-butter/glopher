FROM golang:1.23 as base

WORKDIR /hello_world

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN go build

FROM base as running

CMD ["./hello_world"]
