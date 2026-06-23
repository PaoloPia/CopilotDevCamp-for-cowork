# 🎓 Copilot Dev Camp for Cowork

A **Copilot Cowork plugin** powered by the [Copilot Developer Camp](https://aka.ms/CopilotDevCamp) that brings Copilot Extensibility and Microsoft Foundry documentation, research capabilities, and content creation tools to your Cowork environment. Perfect for Copilot Dev Camp participants and anyone learning about Microsoft Foundry and Copilot extensibility.

**Author**: Paolo Pialorsi (M365 Developer Advocate)

## 📚 Features

### 🧠 Microsoft Foundry Research
**Deep-dive research on Microsoft Foundry** with comprehensive documentation coverage:
- Platform architecture and components
- Available models and capabilities  
- Deployment options and patterns
- Best practices and optimization
- Integration with Azure services

Perfect for: Understanding Foundry fundamentals, architectural planning, and implementation guidance.

### 📊 Dev Camp PowerPoint Deck
**Create professional presentations** on any Copilot Dev Camp topic:
- Research-backed content from Microsoft Learn and Copilot Developer Camp
- Professional slide structure with speaker notes
- Customizable for any audience level (Overview → Advanced)
- Source citations and references included
- Ready to present or customize further

Perfect for: Team presentations, training materials, conference talks, and knowledge sharing.

### 📝 Dev Camp Word Document  
**Author technical documents** about Dev Camp labs and topics:
- Research-backed content from Microsoft Learn and Copilot Developer Camp
- One-pagers, technical guides, how-tos, and more
- Structured with table of contents and formatting
- Professional layout with citations
- Export-ready for PDF or printing
- Customizable for any audience

Perfect for: Documentation, guides, decision records, architecture overviews, and training materials.

## 📚 About Data Sources

This plugin draws from two primary, authoritative sources:

### 1. Microsoft Learn MCP Server
Connects to the **Microsoft Learn MCP Server** at `https://learn.microsoft.com/api/mcp`, providing:
- 🔍 Search through Microsoft's official documentation
- 📄 Fetch complete articles and resources
- 💻 Access code samples and quickstarts
- ✅ No authentication required
- 🆓 Free to use

### 2. Copilot Developer Camp
Leverage official resources from **[Copilot Developer Camp](https://microsoft.github.io/copilot-camp/)**, featuring:
- 🎓 Official labs and hands-on tutorials
- 💡 Real-world scenarios and use cases
- 📂 Code samples and working examples
- 🎯 Best practices from training curriculum
- 🏫 Comprehensive learning materials

Both sources power research and content generation for all three skills in this plugin.

## 📦 What's Included

```
copilot-dev-camp.zip
├── manifest.json                      # M365 Unified App Manifest
├── color.png (192×192)               # Full-color app icon
├── outline.png (32×32)               # Outline icon
└── skills/
    ├── foundry-research/
    │   └── SKILL.md                  # Research skill
    ├── dev-camp-deck/
    │   └── SKILL.md                  # PowerPoint creation skill
    └── dev-camp-document/
        └── SKILL.md                  # Word document creation skill
```

## 🛠️ Tech Stack

| Component | Details |
|-----------|---------|
| **Format** | Microsoft 365 App Package (ZIP) |
| **Manifest** | M365 Unified App Manifest v1.28 |
| **Skills** | Agent Skills open standard |
| **Primary Data Sources** | Microsoft Learn MCP Server + Copilot Developer Camp |
| **MCP Server** | Microsoft Learn (https://learn.microsoft.com/api/mcp) |
| **Learning Platform** | Copilot Developer Camp (https://microsoft.github.io/copilot-camp/) |
| **Authentication** | None required |
| **Transport** | Streamable HTTP |
| **Author** | Paolo Pialorsi (M365 Developer Advocates) |

## 🚀 Quick Start

### 1️⃣ Download the Plugin

Get the latest `copilot-dev-camp.zip` from the [Releases](https://github.com/Microsoft/CopilotDevCamp/releases) page.

### 2️⃣ Install to Your Tenant

#### Option A: Admin Portal (Recommended for teams)
1. Open **Microsoft 365 Admin Center**
2. Go to **Manage Apps** > **Upload custom app**
3. Upload the `.zip` package
4. Skills appear in **Cowork** > **Sources & Skills**

#### Option B: Sideload Personal Use

Using the **Microsoft 365 Agents Toolkit CLI**:

```bash
# Install the toolkit
npm install -g @microsoft/m365agentstoolkit-cli

# Authenticate
atk auth login

# Install the plugin
atk install --file-path "path/to/copilot-dev-camp.zip" --scope Personal
```

You'll receive `TitleId` and `AppId` for future updates or uninstalls.

### 3️⃣ Use in Cowork

Once installed:

1. Open **Microsoft 365 Copilot** > **Cowork**
2. Go to **Sources & Skills**
3. You'll see:
   - 📊 **Copilot Dev Camp** plugin
   - 🧠 **Microsoft Foundry Research** skill
   - 📊 **Dev Camp PowerPoint Deck** skill
   - 📝 **Dev Camp Word Document** skill

## 💡 Usage Examples

### Research Microsoft Foundry
```
"Research Microsoft Foundry architecture and deployment options"
```
Returns comprehensive documentation with best practices and code examples.

### Create a Presentation
```
"Create a PowerPoint deck about Microsoft Foundry for enterprise architects"
```
Generates a professional presentation with research-backed content and speaker notes.

### Author a Guide
```
"Write a technical guide on deploying models with Microsoft Foundry"
```
Produces a formatted Word document with steps, best practices, and resources.

## 📋 Plugin Details

| Setting | Value |
|---------|-------|
| **MCP Server URL** | https://learn.microsoft.com/api/mcp |
| **Authentication** | None |
| **Transport** | Streamable HTTP (HTTPS required, TLS 1.2+) |
| **Availability** | Production-grade, 99.9% uptime |
| **Response Time** | < 30 seconds per tool call |

## 🏗️ Development & Packaging

### Prerequisites
- PowerShell 5.0+ (Windows) or Bash (macOS/Linux)
- Node.js 14+ (for npm scripts, optional)
- ZIP utility (included on most systems)

### Packaging the Plugin

#### Using PowerShell (Windows)
```powershell
Compress-Archive -Path manifest.json, color.png, outline.png, skills `
  -DestinationPath copilot-dev-camp.zip -Force
```

#### Using npm
```bash
npm run package        # Windows
npm run package:unix   # macOS/Linux
```

#### Manual ZIP (macOS/Linux)
```bash
zip -r copilot-dev-camp.zip manifest.json color.png outline.png skills/
```

### File Structure Requirements

✅ **Correct** (all files at root level inside ZIP):
```
copilot-dev-camp.zip
├── manifest.json
├── color.png
├── outline.png
└── skills/
```

❌ **Incorrect** (nested in subdirectory):
```
copilot-dev-camp.zip
└── copilot-dev-camp/  ← Don't nest!
    ├── manifest.json
    ├── color.png
    ...
```

### Validation Rules

Before packaging, ensure:

| Rule | Status |
|------|--------|
| `manifest.json` exists in root | ✓ |
| `color.png` (192×192 px) exists | ✓ |
| `outline.png` (32×32 px) exists | ✓ |
| Each skill folder contains `SKILL.md` | ✓ |
| Skill folder names match `name` in frontmatter | ✓ |
| Skill names use kebab-case | ✓ |
| All manifest JSON is valid | ✓ |

## 📤 Deployment Process

### Step 1: Prepare
- [ ] Test plugin locally with `atk install`
- [ ] Verify all three skills appear in Cowork
- [ ] Test each skill's functionality
- [ ] Check icon rendering (color and outline)

### Step 2: Package
- [ ] Run packaging command (PowerShell, npm, or zip)
- [ ] Verify ZIP structure and size
- [ ] Test ZIP can be extracted cleanly

### Step 3: Deploy to Tenant

**For IT Admins:**
1. M365 Admin Center > Agents > All agents > Add agent
2. Select the `.zip` file
3. Configure target users/groups, configure any organizational policies, and review any permissions
4. Publish to user groups

**For Individual Users:**
1. Use `atk install --file-path <zip-file> --scope Personal`
2. Confirm installation succeeds
3. Verify skills appear in Cowork

### Step 4: Verify
- [ ] Skills appear in **Sources & Skills** panel
- [ ] MCP Server connection established
- [ ] Foundry Research skill can search docs
- [ ] Deck creation generates PowerPoint
- [ ] Document creation generates Word file

### Step 5: Distribute
- [ ] Share `.zip` file via secure channel
- [ ] Document installation instructions for users
- [ ] Provide user guide for each skill
- [ ] Gather feedback for future updates

## 🧪 Testing Locally

### Test Before Deployment

1. **Validate manifest**:
   ```bash
   # Ensure manifest.json is syntactically valid
   # Check schema compliance with M365 v1.28
   ```

2. **Test skills**:
   ```bash
   # In Cowork, test each skill trigger phrase:
   # - "Research Microsoft Foundry..."
   # - "Create a PowerPoint deck about..."
   # - "Write a document about..."
   ```

3. **Verify MCP connection**:
   - All skills should connect to Microsoft Learn MCP Server
   - Search and fetch operations should work
   - Response times should be < 30 seconds

4. **Check outputs**:
   - PowerPoint files should be valid and openable
   - Word documents should be properly formatted
   - Research summaries should be comprehensive

### Using atk CLI for Testing

```bash
# Install locally
atk install --file-path ./copilot-dev-camp.zip --scope Personal

# Get installation details
atk list --scope Personal

# Later: Update installed version
atk update --title-id <TitleId> --file-path ./copilot-dev-camp.zip

# Uninstall when done
atk uninstall --title-id <TitleId>
```

## 📖 Skill Documentation

Each skill includes detailed workflows:

### 🧠 Foundry Research (`foundry-research/SKILL.md`)
- Multi-topic research capability
- Structured organization of findings
- Comprehensive output with citations
- Best for: Understanding Foundry platform

### 📊 Dev Camp Deck (`dev-camp-deck/SKILL.md`)
- Topic and audience selection
- 6-step research and structure workflow
- Professional PowerPoint generation
- Best for: Presentations and training

### 📝 Dev Camp Document (`dev-camp-document/SKILL.md`)
- Flexible document types (one-pager, guide, how-to)
- Research-backed content
- Professional Word formatting
- Best for: Documentation and guides

## 🎯 Compatibility

This plugin is built on **Agent Skills open standard** — the same format supported by:

- ✅ Claude Code
- ✅ VS Code Copilot
- ✅ Gemini CLI
- ✅ JetBrains Junie
- ✅ Cursor
- ✅ 30+ other AI tools

You can repurpose these skills across multiple platforms!

## 🔐 Security & Privacy

- ✅ No secrets or API keys embedded in skills
- ✅ MCP Server connection uses no authentication (public Learn docs)
- ✅ All data is read-only (research mode)
- ✅ Microsoft Learn content is official and trusted
- ✅ Generated documents stay on user's device
- ✅ No telemetry or tracking beyond standard M365

## 🤝 Contributing

Want to improve this plugin? 

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-skill`)
3. **Add** your skill to `skills/` following Agent Skills standard
4. **Test** the skill locally with Cowork
5. **Submit** a pull request with description

### Adding New Skills

1. Create folder: `skills/skill-name/`
2. Add `SKILL.md` with proper frontmatter:
   ```yaml
   ---
   name: skill-name
   description: |
     What this skill does and when to use it.
     Include trigger phrases.
   license: MIT
   metadata:
     author: Copilot Dev Camp
     version: "1.0"
   ---
   ```
3. Write skill workflow and output format
4. Update `manifest.json` to reference new skill
5. Test and validate

## 📋 Skill Development Best Practices

When creating new skills:

- ✅ **Be specific** in the description — include trigger phrases
- ✅ **Structure as workflow** — number the steps clearly
- ✅ **Define output format** — show expected result structure
- ✅ **Reference tools by name** — if using MCP tools
- ✅ **Keep SKILL.md lean** — < 3,000 words in main body
- ✅ **Move details to references/** — for complex content
- ❌ **Don't embed secrets** — use agent connectors instead
- ❌ **Don't hardcode paths** — keep skills portable
- ❌ **Don't duplicate built-ins** — check existing skills first

## 📊 Manifest Reference

The `manifest.json` follows **M365 Unified App Manifest v1.28**:

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/teams/v1.28/MicrosoftTeams.schema.json",
  "manifestVersion": "1.28",
  "id": "GUID",
  "agentSkills": [
    { "folder": "./skills/skill-name" }
  ],
  "agentConnectors": [
    {
      "id": "connector-id",
      "toolSource": {
        "remoteMcpServer": {
          "mcpServerUrl": "https://..."
        }
      }
    }
  ]
}
```

[Full schema documentation](https://developer.microsoft.com/json-schemas/teams/v1.28/MicrosoftTeams.schema.json)

## 🆘 Troubleshooting

### Skills Don't Appear in Cowork
- Verify `manifest.json` is valid JSON
- Check skill folder names match `name` in frontmatter
- Ensure ZIP has correct structure (no nested folders)
- Try reinstalling: `atk uninstall` then `atk install`

### MCP Connection Errors
- Verify internet connectivity to `https://learn.microsoft.com/api/mcp`
- Check firewall allows HTTPS to learn.microsoft.com
- Confirm TLS 1.2+ is supported
- MCP Server typically has 99.9% uptime SLA

### PowerPoint Not Generated
- Ensure topic is specific enough for research
- Check audience and duration are defined
- Verify skill is using the correct MCP tool calls
- Review skill logs for research completion

### Word Documents Not Formatted
- Confirm document type selected (one-pager, guide, etc.)
- Check audience level is appropriate
- Verify content length matches expectations
- Ensure Word is available for opening output

### Plugin Upload Fails
- Validate ZIP structure matches requirements
- Check file size is reasonable (< 10 MB typical)
- Verify all referenced files exist in ZIP
- Try uploading to test tenant first

## 📞 Support & Feedback

- 🐛 **Report issues**: [GitHub Issues](https://github.com/Microsoft/CopilotDevCamp/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Microsoft/CopilotDevCamp/discussions)
- 📧 **Email**: copilot-dev-camp@microsoft.com
- 📚 **Documentation**: [Copilot Dev Camp](https://learn.microsoft.com/training/paths/...)

## 📝 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Paolo Pialorsi** (M365 Developer Advocates) - Plugin creator and maintainer
- **Copilot Developer Camp** - Official training curriculum and learning materials
- Microsoft Foundry team for platform and documentation
- Microsoft Learn team for the public MCP Server
- Copilot Dev Camp community
- Contributors and testers

## 🔗 Related Resources

- [Copilot Developer Camp](https://microsoft.github.io/copilot-camp/) - Official training and learning materials
- [Copilot Cowork Plugin Development](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development) - Official Cowork documentation
- [Microsoft Learn MCP Server](https://learn.microsoft.com/en-us/training/support/mcp) - MCP server documentation
- [Agent Skills Open Standard](https://docs.anthropic.com/en/docs/skills) - Agent Skills format specification
- [M365 Unified App Manifest](https://learn.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema) - Manifest schema reference
- [Microsoft 365 Agents Toolkit](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/microsoft-365-agents-toolkit-cli) - CLI toolkit documentation

---

**Created by**: Paolo Pialorsi (M365 Developer Advocates)  
**Based on**: [Copilot Developer Camp](https://microsoft.github.io/copilot-camp/)  
**Powered by**: Microsoft Learn MCP Server + Copilot Developer Camp  
**Built with ❤️ for the Copilot Dev Camp community**

*Last updated: June 2026*
