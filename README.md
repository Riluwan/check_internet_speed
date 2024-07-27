# Flask Speedtest App

This is a simple Flask application that displays the current internet download and upload speed. The application uses the `speedtest-cli` package to measure the internet speed.

## Features

- Measure download speed
- Measure upload speed
- Measure ping

## Endpoints

- `/speedtest` - Returns the current download speed, upload speed, and ping in JSON format.

## Requirements

- Python 3.x
- Flask
- speedtest-cli
- gunicorn

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-speedtest.git
   cd flask-speedtest
