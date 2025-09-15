# EpicPrompts

Welcome to **EpicPrompts**, a curated and regularly updated collection of brilliant, high-quality prompts for various use cases. These prompts are designed as JSON files to be used with powerful, general-purpose consumer multimodal generative AI tools.

Created by [Navaneeth Sankar K P](https://www.linkedin.com/in/navaneeth-sankar-k-p).

## About The Project

This repository is a work-in-progress, containing a collection of meticulously crafted prompts that have been tested and found to work beautifully. The goal is to provide a resource for anyone looking to leverage the full potential of advanced Generative AI models for creative and technical tasks.

The prompts are structured in JSON format for clarity and ease of use. They are designed to be detailed and comprehensive, ensuring high-quality and specific outputs from the AI.

We welcome collaboration and contributions! If you have a powerful prompt you'd like to share, feel free to open a pull request.

<details>
<summary><b>EtherealVintageBloom -image</b></summary>

A prompt for generating and analyzing images with a specific photographic style.

**When to use:**
To generate an image with an ethereal, vintage, and cinematic feel.

**What to provide:**
* A brief description of the image + the JSON prompt.

[Access Folder](./EtherealVintageBloom/)

*OutputExample: Gemini 2.5 Flash Image Preview (Google Nano Banana)*

<img width="1024" height="1024" alt="Preview" src="https://res.cloudinary.com/dporqrc5z/image/upload/v1757923505/download_poxdzo.png" />

---
</details>

<details>
<summary><b>SequentialAudioTranscription -audio</b></summary>

A prompt for transcribing a collection of audio files sequentially and extracting metadata.

**When to use:**
* When you have multiple audio files to transcribe and want to extract information like speaker's name, gender, and age.

**What to upload:**
* A collection of audio files.

[Access Folder](./SequentialAudioTranscription/)
</details>

<details>
<summary><b>SetExecutionPolicy -text</b></summary>

A meta-instruction prompt to set the execution policy for a large-scale task.

**When to use:**
* Before a complex, multi-step task to ensure the AI prioritizes quality and accuracy over speed.

[Access Folder](./SetExecutionPolicy/)
</details>

### Compatibility

These prompts are designed for high-token count, multimodal models (default Temperature etc. settings) released after **June 2025**, such as:
* Google DeepMind's Gemini 2.5 Pro (and subsequent versions)
* OpenAI's ChatGPT (GPT-5 and subsequent high-token models)
* Other similar advanced consumer-scale multimodal Generative AI tools

UNLESS: The model name is specifically mentioned in the directory name ("modelName" + "_" + "directoryName")  

## File Structure

Here is an overview of the current project structure:

```
.
├── EtherealVintageBloom
│   ├── EVBwRL_V1.json
├── SequentialAudioTranscription
│   └── SAT_V1.json
└── SetExecutionPolicy
    └── SEP_V1.json
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
