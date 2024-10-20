# IELTS Writing Task 2 Validator

This project provides an automated validation tool for IELTS Writing Task 2 responses using Amazon Bedrock and a custom-trained language model.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)

## Description

This Python-based tool evaluates IELTS Writing Task 2 essays by leveraging Amazon Bedrock's language models and a dataset of pre-evaluated responses. It provides an overall band score and examiner comments for given question-answer pairs.

## Features

- Automated evaluation of IELTS Writing Task 2 essays
- Utilizes Amazon Bedrock for natural language processing
- Provides band scores and detailed examiner feedback
- Incorporates a training dataset for improved accuracy

## Prerequisites

- Python 3.10
- AWS account with Bedrock access
- Pandas library
- Boto3 library

## Installation

1. Clone the repository:

   ```
   https://github.com/sajithsajith/IELTS_writing_task2_validator.git
   ```

2. Install required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up your AWS credentials and configure the `app_constants.py` file with your specific settings.

## Usage

Run the script from the command line:

```
python app.py
```

You will be prompted to enter the question and your essay answer. The script will then provide an evaluation and band score.

## Configuration

Modify the `app_constants.py` file to set:

- AWS region
- AWS access key and secret key
- Bedrock model ID
- System prompt
- Other model parameters (temperature, max tokens, etc.)

## How It Works

1. The script loads a pre-existing dataset of evaluated IELTS essays.
2. It formats the user's input (question and answer) along with the training data.
3. The formatted data is sent to Amazon Bedrock for processing.
4. The model returns an evaluation and band score based on the input and training data.
5. Results are displayed to the user.
