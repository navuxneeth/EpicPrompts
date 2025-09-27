# EpicPrompts

[![Validation](https://img.shields.io/badge/validation-passing-brightgreen)](#validation)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A curated collection of meticulously crafted AI prompts designed to work beautifully with powerful, general-purpose consumer multimodal generative AI tools.

## 🚀 Quick Start

1. **Browse the collection** below to find prompts that suit your needs
2. **Choose your format**: JSON for precise structure, YAML for readability  
3. **Copy the prompt** from the appropriate directory
4. **Paste into your AI tool** and customize as needed
5. **Create amazing content** with consistent, high-quality results!

📖 **New to prompting?** Check out our [practical examples](EXAMPLES.md) with step-by-step usage guides!

## 🎯 What's Inside

This repository contains structured prompts in both **JSON** and **YAML** formats, each designed for specific creative and technical tasks. Every prompt has been tested and refined to ensure optimal performance.

### 🎨 Available Prompt Categories

| Category | Description | Use Cases |
|----------|-------------|-----------|
| 🖼️ **Image Generation** | Photography styles, artistic techniques | Creative visuals, professional photography |
| 📝 **Text Processing** | Writing, documentation, analysis | Content creation, documentation |
| 🎵 **Audio Processing** | Transcription, metadata extraction | Media processing, accessibility |
| 🛠️ **Technical Tasks** | Code generation, system administration | Development, automation |
| 🎭 **Creative Writing** | Storytelling, character development | Fiction, creative content |

### Compatibility

These prompts are designed for high-token count, multimodal models (default Temperature etc. settings) released after **June 2025**, such as:
* Google DeepMind's Gemini 2.5 Pro (and subsequent versions)
* OpenAI's ChatGPT (GPT-5 and subsequent high-token models)
* Other similar advanced consumer-scale multimodal Generative AI tools

## 📚 Featured Prompts

> 💡 **Tip**: See [EXAMPLES.md](EXAMPLES.md) for detailed usage instructions and practical workflows!

### Image Generation

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

<details>
<summary><b>RepositoryDocumentation -text</b></summary>

A collection of prompts to generate and maintain documentation for a code repository.

**When to use:**
* To automatically generate or update a `README.md` and `LICENSE` file for your repository based on its content.

**Versions:**
* **`makeReadme_V1.json`**: Use this to generate a brand new `README.md` and `LICENSE` from scratch by analyzing the repository's content.
* **`syncReadme_V1.json`**: Use this for a basic update. It checks for new or deleted files and updates the file structure in the `README.md`.
* **`syncReadme_V2` / `syncReadme_V2.json`**: Use this for a comprehensive update. It performs a deep analysis of code, dependencies, and build scripts to ensure every part of the `README.md` is perfectly synchronized with the repository's current state.

[Access Folder](./RepositoryDocumentation/)
</details>

UNLESS: The model name is specifically mentioned in the directory name ("modelName" + "_" + "directoryName")

## 🛠️ Tools & Validation

### Validation Tool
We've included a comprehensive validation tool to ensure prompt quality and consistency:

```bash
# Run the validation tool
python3 .github/tools/validate_prompts.py
```

This tool checks for:
- ✅ Valid JSON syntax
- 📋 Consistent file naming conventions
- 🏗️ Proper directory structure
- 📝 Required metadata fields
- 🔄 YAML/JSON synchronization

### File Formats
- **JSON**: Primary format for precise, programmatic use
- **YAML**: Human-readable alternative in `YAML-versions/` directory

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### 🎯 Ways to Contribute
- **Submit new prompts** following our [guidelines](CONTRIBUTING.md)
- **Improve existing prompts** with better results or documentation
- **Report bugs** or issues with prompts
- **Suggest enhancements** to the repository structure
- **Add translations** or variations for different AI models

### 📋 Before Contributing
1. Read our [Contributing Guidelines](CONTRIBUTING.md)
2. Check existing [issues](https://github.com/navuxneeth/EpicPrompts/issues) and [pull requests](https://github.com/navuxneeth/EpicPrompts/pulls)
3. Run the validation tool on your prompts
4. Test with multiple AI models when possible

### 🚀 Quick Contribution
1. Fork this repository
2. Create your prompt following the structure in `CONTRIBUTING.md`
3. Run validation: `python3 .github/tools/validate_prompts.py`
4. Submit a pull request with our template

## 📊 Repository Stats
- 📁 **Prompt Categories**: 4 main categories
- 📄 **Total Prompts**: 8+ unique prompts  
- 🔧 **Formats**: JSON + YAML versions
- ✅ **Validation**: Automated quality checks
- 🤝 **Contributors**: Growing community

## 🎉 Recognition

Special thanks to all contributors who help make EpicPrompts better! Contributors are recognized in:
- Repository contributor list
- Individual prompt credits
- Community showcase (coming soon)

## 📁 File Structure

Here is an overview of the current project structure:

```
├── .github/                    # GitHub templates and tools
│   ├── ISSUE_TEMPLATE/        # Issue templates for contributions
│   └── tools/                 # Validation and maintenance scripts
├── .gitattributes
├── CONTRIBUTING.md            # Contribution guidelines
├── LICENSE                    # MIT License
├── README.md                  # This file
├── EtherealVintageBloom/      # Image generation prompts
│   └── EVB_V1.json
├── RepositoryDocumentation/   # Documentation generation prompts
│   ├── makeReadme_V1.json
│   ├── optimizedTopics_V1.json
│   ├── syncReadme_V1.json
│   ├── syncReadme_V2.json
│   ├── syncReadme_V3.json
│   └── syncReadme_V4.json
├── SequentialAudioTranscription/  # Audio processing prompts
│   └── SAT_V1.json
├── SetExecutionPolicy/        # Meta-instruction prompts
│   └── SEP_V1.json
├── YAML-versions/             # YAML format alternatives
│   ├── EtherealVintageBloom/
│   │   └── EVB_V1.yaml
│   ├── RepositoryDocumentation/
│   │   ├── makeReadme_V1.yaml
│   │   ├── optimizedTopics_V1.yaml
│   │   ├── syncReadme_V1.yaml
│   │   ├── syncReadme_V2.yaml
│   │   ├── syncReadme_V3.yaml
│   │   └── syncReadme_V4.yaml
│   ├── SequentialAudioTranscription/
│   │   └── SAT_V1.yaml
│   └── SetExecutionPolicy/
│       └── SEP_V1.yaml
```

### 🏗️ Structure Conventions
- **Directory Names**: PascalCase, descriptive (e.g., `EtherealVintageBloom`)
- **File Names**: `ACRONYM_V#.json` (e.g., `EVB_V1.json`)
- **Versioning**: Start with V1, increment for major changes
- **Dual Format**: Both JSON and YAML versions maintained
## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
Created by [Navaneeth Sankar K P](https://www.linkedin.com/in/navaneeth-sankar-k-p).
