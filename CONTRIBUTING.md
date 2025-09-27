# Contributing to EpicPrompts

Thank you for considering contributing to EpicPrompts! This document provides guidelines for contributing high-quality prompts to our collection.

## 🎯 What Makes a Great Prompt

### Quality Standards
- **Tested and Verified**: Your prompt should be thoroughly tested with the target AI models
- **Detailed and Specific**: Provide comprehensive instructions that produce consistent results
- **Well-Documented**: Include clear descriptions of when and how to use the prompt

### Prompt Categories
We welcome prompts for various purposes:
- 🖼️ **Image Generation** - Photography styles, artistic techniques, visual concepts
- 📝 **Text Generation** - Writing styles, documentation, analysis tasks
- 🎵 **Audio Processing** - Transcription, analysis, metadata extraction
- 🛠️ **Technical Tasks** - Code generation, system administration, automation
- 🎭 **Creative Tasks** - Storytelling, character development, creative writing

## 📁 File Structure and Naming

### Directory Organization
```
PromptCategoryName/
├── CategoryAcronym_V1.json    # Main JSON version
└── README.md                  # Optional: Category-specific documentation
```

### Naming Conventions
- **Directory Name**: Descriptive, PascalCase (e.g., `EtherealVintageBloom`)
- **File Name**: `[CategoryAcronym]_V[Version].json` (e.g., `EVB_V1.json`)
- **Version**: Start with V1, increment for significant changes

## 📋 Prompt Structure

### Required JSON Fields
```json
{
  "task": "Brief description of what the prompt does",
  "description": "Detailed explanation of the prompt's purpose and capabilities",
  "parameters": {
    // Specific configuration options
  },
  "usage_instructions": "How to use this prompt effectively",
  "compatibility": ["Model1", "Model2"], // Optional: specific model compatibility
  "examples": {
    // Optional: example inputs and expected outputs
  }
}
```

### Best Practices
- Use clear, descriptive field names
- Include detailed parameter descriptions
- Provide example usage scenarios
- Test with multiple AI models when possible

## 🔄 Submission Process

### 1. Fork and Clone
```bash
git clone https://github.com/YOUR_USERNAME/EpicPrompts.git
cd EpicPrompts
```

### 2. Create Your Prompt Directory
```bash
mkdir YourPromptName
cd YourPromptName
```

### 3. Create Your Prompt Files
- Create the main JSON prompt file
- Add a README.md if your prompt needs special explanation
- Test thoroughly with target AI models

### 4. Validation
Before submitting, ensure your JSON is valid:
```bash
# Check JSON validity
python3 -m json.tool YourPromptName/YPA_V1.json > /dev/null && echo "Valid JSON" || echo "Invalid JSON"
```

### 5. Submit Pull Request
- Create a feature branch: `git checkout -b add-your-prompt-name`
- Commit your changes: `git commit -m "Add YourPromptName prompt"`
- Push to your fork: `git push origin add-your-prompt-name`
- Create a Pull Request with:
  - Clear title describing the prompt
  - Description of what the prompt does
  - Example usage or output
  - Which AI models you've tested with

## ✅ Pull Request Template

When submitting your prompt, please include:

```markdown
## Prompt Description
Brief description of what your prompt does.

## Category
- [ ] Image Generation
- [ ] Text Processing
- [ ] Audio Processing
- [ ] Technical/Code
- [ ] Creative Writing
- [ ] Other: ___________

## Testing
- [ ] JSON syntax validated
- [ ] Tested with: [List AI models]
- [ ] Consistent results achieved
- [ ] Documentation complete

## Examples
Provide examples of input/output or screenshots if applicable.

## Additional Notes
Any special considerations, limitations, or advanced usage tips.
```

## 🎨 Style Guidelines

### JSON Formatting
- Use 2-space indentation
- Keep strings under 120 characters when possible
- Use descriptive variable names
- Include comments in description fields where helpful

### Documentation
- Write clear, concise descriptions
- Use proper grammar and spelling
- Include practical examples
- Explain any non-obvious parameters

## 🤝 Community Guidelines

- Be respectful and constructive in discussions
- Help others improve their prompts through feedback
- Share knowledge and testing results
- Report issues clearly and provide reproduction steps

## 📞 Getting Help

- **Questions**: Open a GitHub issue with the "question" label
- **Bug Reports**: Use the bug report template
- **Feature Requests**: Use the feature request template
- **Discord**: [Join our community](https://discord.gg/yourlink) (if available)

## 🏆 Recognition

Contributors will be:
- Credited in the repository
- Added to our contributors list
- Featured for exceptional contributions

Thank you for helping make EpicPrompts better! 🚀