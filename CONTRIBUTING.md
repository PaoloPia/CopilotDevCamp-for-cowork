# Contributing to Copilot Dev Camp Plugin

Thank you for your interest in contributing to the Copilot Dev Camp for Cowork plugin! This document provides guidelines for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Types of Contributions](#types-of-contributions)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Creating New Skills](#creating-new-skills)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [License](#license)

## Code of Conduct

This project adheres to the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

By participating, you are expected to uphold this code. Please report unacceptable behavior to copilot-dev-camp@microsoft.com.

## Types of Contributions

We welcome contributions in several areas:

### 🎯 Report Bugs

If you find a bug:
1. Check [existing issues](https://github.com/Microsoft/CopilotDevCamp/issues)
2. Include version number and steps to reproduce
3. Provide sample input/output if applicable
4. Mention your environment (OS, PowerShell version, etc.)

### 📋 Request Features

Have an idea for improvement?
1. Check [discussions](https://github.com/Microsoft/CopilotDevCamp/discussions)
2. Describe the use case and expected behavior
3. Explain why it would be beneficial
4. Include examples if possible

### 📚 Create New Skills

Want to add a skill? Here's the process:
1. Discuss idea in [discussions](https://github.com/Microsoft/CopilotDevCamp/discussions)
2. Get feedback before implementing
3. Follow the [Creating New Skills](#creating-new-skills) guide below
4. Submit pull request with complete documentation

### 📖 Improve Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add troubleshooting information
- Include more examples
- Improve formatting and structure

### ♻️ Refactor Code

Help make the codebase better:
- Improve SKILL.md clarity
- Add missing metadata
- Enhance workflow descriptions
- Optimize skill triggers

## Getting Started

### Prerequisites

- Git installed and configured
- GitHub account
- Text editor (VS Code recommended)
- Basic understanding of Agent Skills format

### Fork & Clone

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/CopilotDevCamp.git

# 3. Add upstream remote
git remote add upstream https://github.com/Microsoft/CopilotDevCamp.git

# 4. Create feature branch
git checkout -b feature/your-feature-name
```

### Build Environment

No complex build setup needed! You can edit SKILL.md files directly.

For packaging:
```bash
# Windows PowerShell
Compress-Archive -Path manifest.json, color.png, outline.png, skills `
  -DestinationPath copilot-dev-camp.zip -Force

# macOS/Linux
zip -r copilot-dev-camp.zip manifest.json color.png outline.png skills/
```

## Development Workflow

### 1. Create Feature Branch

```bash
git checkout -b feature/descriptive-name

# Good examples:
# feature/foundry-advanced-research
# feature/new-skill-azure-deployment
# fix/skill-trigger-phrases
# docs/update-deployment-guide
```

### 2. Make Changes

Edit files as needed. Common changes:

**Adding a new skill**:
1. Create `skills/skill-name/` directory
2. Create `skills/skill-name/SKILL.md`
3. Update `manifest.json` to add `agentSkills` entry
4. Update `README.md` with feature description

**Updating existing skill**:
1. Edit `skills/skill-name/SKILL.md`
2. Follow Agent Skills format strictly
3. Update version in `metadata` section

**Updating documentation**:
1. Edit relevant `.md` file
2. Ensure clarity and accuracy
3. Update table of contents if adding sections

### 3. Test Locally

Before submitting:

**Validate YAML frontmatter**:
```bash
# Each SKILL.md should have valid frontmatter
# Use a YAML validator or JSON validator if unsure
```

**Validate manifest.json**:
```bash
# Ensure manifest.json is valid JSON
node -e "console.log(JSON.parse(require('fs').readFileSync('manifest.json')))"
```

**Verify folder structure**:
```bash
# Run validation checks
ls -la skills/
# Each skill should have SKILL.md with matching folder name
```

### 4. Commit Changes

```bash
# Stage files
git add .

# Commit with clear message
git commit -m "feat: add new X skill for Y functionality"

# Good commit messages:
# "feat: add Foundry advanced research skill"
# "fix: correct trigger phrases in dev-camp-deck"
# "docs: update deployment guide with troubleshooting"
# "refactor: improve skill workflow clarity"
```

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 6. Create Pull Request

1. Go to GitHub
2. Create Pull Request against `main` branch
3. Fill in PR template with:
   - Description of changes
   - Why this change is needed
   - Link to related issues/discussions
   - Testing performed

## Creating New Skills

### Skill Requirements

Every skill must have:

1. **Valid folder structure**:
   ```
   skills/skill-name/
   └── SKILL.md
   ```

2. **YAML frontmatter** in SKILL.md:
   ```yaml
   ---
   name: skill-name          # kebab-case, matches folder
   description: |            # Clear description with trigger phrases
     What this skill does.
     Use when user asks to "..."
   license: MIT
   metadata:
     author: Copilot Dev Camp
     version: "1.0"
   ---
   ```

3. **Clear structure**:
   - H1 title (skill name)
   - "What This Skill Does" section
   - "When to Use This Skill" section
   - "Workflow" section with numbered steps
   - "Output Format" section
   - Any other relevant sections

4. **Trigger phrases** in description:
   - Include 3-5 example trigger phrases
   - Make them specific and actionable
   - Include variations (e.g., "research", "analyze", "deep-dive")

### Skill Development Process

1. **Plan**:
   - What problem does this solve?
   - Who is the target user?
   - What should the output be?
   - Does it need MCP server integration?

2. **Design**:
   - Draft workflow steps
   - Identify research needs
   - Plan output structure
   - Create example trigger phrases

3. **Document**:
   - Write SKILL.md with complete workflow
   - Include examples of good/bad usage
   - Document all output formats
   - Add resource links

4. **Test**:
   - Validate frontmatter and structure
   - Test with sample prompts
   - Verify output format
   - Check MCP tool integration

5. **Submit**:
   - Create PR with your skill
   - Include description of skill purpose
   - Link to any related discussions

### Example Skill Template

```markdown
---
name: example-skill
description: |
  Short description of what skill does.
  Use when user asks to "trigger phrase 1", "trigger phrase 2",
  "trigger phrase 3", or "trigger phrase 4".
license: MIT
metadata:
  author: Copilot Dev Camp
  version: "1.0"
---

# Example Skill

## What This Skill Does

Clear explanation of the skill's purpose and capabilities.

## When to Use This Skill

Specific scenarios where this skill is most useful.

## Workflow

1. **Step One**: Description and purpose
2. **Step Two**: Description and purpose
3. **Step Three**: Description and purpose

## Output Format

| Component | Description |
|-----------|-------------|
| Item 1 | What it is |
| Item 2 | What it is |

## Example

```
User: "trigger phrase that activates this skill"
Expected: description of what happens
```
```

### Naming Conventions

**Skill folder and name** (kebab-case):
- ✅ `azure-deployment-guide`
- ✅ `foundry-research`
- ✅ `team-communication-summary`
- ❌ `AzureDeploymentGuide` (PascalCase)
- ❌ `azure_deployment_guide` (snake_case)
- ❌ `azure--deployment` (consecutive hyphens)

## Pull Request Process

1. **Update documentation**:
   - [ ] Update README.md if adding new skill
   - [ ] Update manifest.json if needed
   - [ ] Update DEPLOYMENT.md if process changes

2. **Follow style guidelines**:
   - [ ] All SKILL.md files use consistent format
   - [ ] No hardcoded secrets or credentials
   - [ ] Proper attribution and citations
   - [ ] Clear, concise language

3. **Pass validation**:
   - [ ] Manifest.json is valid JSON
   - [ ] All skill folders contain SKILL.md
   - [ ] Folder names match skill names
   - [ ] Skill names use kebab-case

4. **PR review**:
   - Code owners will review your PR
   - Address feedback and requested changes
   - Keep commits clean and logical

5. **Merge**:
   - Squash commits if needed
   - Ensure all checks pass
   - PR gets merged to main

## Style Guidelines

### Markdown Style

- Use clear, concise language
- Headings: H1 (#) for title, H2 (##) for sections
- Lists: Use bullet points or numbered lists as appropriate
- Code blocks: Use triple backticks with language identifier
- Links: Use inline links [text](url) format

### SKILL.md Format

```yaml
---
name: skill-name-kebab-case  # Required, matches folder
description: |               # Required, 1-1024 chars
  Clear description.
  Include trigger phrases.
license: MIT                 # Recommended
metadata:
  author: Copilot Dev Camp
  version: "1.0"
---

# Skill Name

## What This Skill Does

Clear bullet-point explanation.

## When to Use This Skill

Specific use cases.

## Workflow

1. **Step**: Description
2. **Step**: Description

## Output Format

Structured description of output.
```

### Documentation Standards

- Write for a broad audience (not just developers)
- Include examples for most features
- Link to relevant resources
- Use consistent terminology
- Keep code samples simple and clear

### Commit Messages

Follow conventional commits:

```
feat: add new skill
fix: correct skill trigger
docs: update README
refactor: improve SKILL.md clarity
```

Format: `<type>: <subject>`

Types:
- `feat`: New skill or feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code restructuring (no feature change)
- `test`: Adding tests
- `chore`: Build, dependencies, etc.

## License

By contributing, you agree that your contributions will be licensed under the MIT License. All contributions to this project are assumed to be under the MIT license.

## Questions?

- 💬 Ask in [GitHub Discussions](https://github.com/Microsoft/CopilotDevCamp/discussions)
- 📧 Email: copilot-dev-camp@microsoft.com
- 📚 Read [Cowork Plugin Development](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development)

---

Thank you for contributing to Copilot Dev Camp! 🎉
