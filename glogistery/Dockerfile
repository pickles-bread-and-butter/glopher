FROM golang:1.21 as base

WORKDIR /glogistery

COPY go.mod go.sum ./

RUN go mod install

COPY . .

RUN go build . -o main

FROM base as running

EXPOSE 8000

CMD ["./main"]
