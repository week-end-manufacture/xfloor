# xfloor

An app that classifies file lists through crawling.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

`xfloor` is an application that classifies file lists and retrieves additional information through web crawling. It fetches the file list from a given directory, classifies the files based on their extensions, and retrieves additional information from specific websites.

## Features

- Fetch file list from a directory
- Classify files based on their extensions
- Retrieve additional information about files through web crawling
- Set environment variables through a JSON file
- Handle exceptions for reliable network requests

## Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/week-end-manufacture/xfloor.git
    cd xfloor
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set up the `config.json` file. Example:

    ```json
    {
        "FLIB_VERSION": "1.0.0",
        "URL_LIST": ["http://example.com", "http://example.org"]
    }
    ```

2. Run the application:

    ```sh
    python main.py -i <source_directory> -o <destination_directory>
    ```

    Example:

    ```sh
    python main.py -i ./src -o ./dst
    ```

## Configuration

You can set environment variables through the `config.json` file. Example:

```json
{
    "FLIB_VERSION": "1.0.0",
    "URL_LIST": ["http://example.com", "http://example.org"]
}