# Vision Assistant 🇲🇾
<p align=center>
  <img src='VisionAssistant.png' width=50%>
</p>

As of June 2023, the Social Welfare Department of Malaysia reported that 52,027 people in the country are registered as visually impaired. This is an estimated 1.2% of the population.

Many visually impaired individuals face challenges in navigating and understanding their surroundings.

Our Vision Assistant leverages OpenAI's advanced AI models to provide real-time assistance to visually impaired users by describing their environment and identifying objects.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Vision Assistant is designed to help visually impaired individuals by using advanced AI to interpret and describe their surroundings. By leveraging OpenAI's powerful models, the assistant provides real-time descriptions of objects and scenes, helping users navigate and understand their environment more effectively.

## Features
- **Image Recognition**: Identifies objects within an image and provides labels.
- **Scene Understanding**: Describes the overall scene and context of images.
- **Text Recognition (OCR)**: Converts written text in images to readable text.
- **Voice Assistance**: Provides audio feedback to users, describing the scene or objects detected.

## Technologies
- **OpenAI Models**: GPT-4 for natural language processing, DALL-E for image generation.
- **API Integration**: Using OpenAI API for model interaction and image recognition capabilities.
- **Streamlit**: Provides a web-based application that can be operated on various devices.
- **Hardware**: Designed to run on devices like smartphones, tablets, and personal computers.

## Installation
To install and run the Vision Assistant locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/vision-assistant.git
    ```
2. Navigate to the project directory:
    ```bash
    cd vision-assistant
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up your OpenAI API key:
    - Create a `.env` file in the project directory.
    - Add your OpenAI API key to the `.env` file:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage
To start the Vision Assistant, run the following command:

```bash
streamlit run test.py
