# Quick Reference Card

## 📦 Plugin at a Glance

**Copilot Dev Camp for Cowork** - Research, create presentations, author documents using Microsoft Foundry documentation.

| Property | Value |
|----------|-------|
| **Type** | Microsoft 365 Cowork Plugin |
| **Version** | 1.0.0 |
| **Skills** | 3 (Research, Deck, Document) |
| **MCP Server** | Microsoft Learn (https://learn.microsoft.com/api/mcp) |
| **Auth** | None required |
| **License** | MIT |

## 🎯 Three Skills

| # | Skill | Trigger | Output |
|---|-------|---------|--------|
| 1 | 🧠 **Foundry Research** | "Research Foundry..." | Markdown research document |
| 2 | 📊 **Dev Camp Deck** | "Create a PowerPoint..." | PowerPoint presentation (.pptx) |
| 3 | 📝 **Dev Camp Document** | "Write a document..." | Word document (.docx) |

## 📦 Package Contents

```
copilot-dev-camp.zip
├── manifest.json
├── color.png (192×192)
├── outline.png (32×32)
└── skills/
    ├── foundry-research/SKILL.md
    ├── dev-camp-deck/SKILL.md
    └── dev-camp-document/SKILL.md
```

## ⚡ Quick Commands

### Package (Choose one)

**PowerShell Windows**:
```powershell
Compress-Archive -Path manifest.json, color.png, outline.png, skills `
  -DestinationPath copilot-dev-camp.zip -Force
```

**npm**:
```bash
npm run package        # Windows
npm run package:unix   # macOS/Linux
```

**Bash macOS/Linux**:
```bash
zip -r copilot-dev-camp.zip manifest.json color.png outline.png skills/
```

### Install & Test

```bash
# Install toolkit
npm install -g @microsoft/m365agentstoolkit-cli

# Login
atk auth login

# Install plugin
atk install --file-path "./copilot-dev-camp.zip" --scope Personal

# List installed
atk list --scope Personal

# Update
atk update --title-id <ID> --file-path "./copilot-dev-camp.zip"

# Uninstall
atk uninstall --title-id <ID>
```

### Validate

```bash
# Validate manifest.json
node -e "console.log(JSON.parse(require('fs').readFileSync('manifest.json')))"

# Check ZIP structure
unzip -l copilot-dev-camp.zip | head -20

# Check skills
ls -la skills/*/SKILL.md
```

## 📋 Deployment Paths

### Path 1: Personal (5 min)
```
atk install --file-path "./copilot-dev-camp.zip" --scope Personal
↓
Appears in Cowork > Sources & Skills (personal only)
```

### Path 2: Tenant Admin (15 min)
```
M365 Admin Center > Agents > All agents > Add agent
↓
Select ZIP file
↓
Select target users/groups
↓
Apply organizational policies
↓
Review permissions
↓
Publish to organization
↓
Appears for all users (15-30 min sync)
```

### Path 3: Intune (30 min)
```
Intune Admin Center → Apps → Manage apps
↓
Upload plugin package
↓
Assign to groups
↓
Deploy to devices
```

## ✅ Pre-Deployment Checklist

- [ ] Icons: `color.png` (192×192), `outline.png` (32×32)
- [ ] Manifest: Valid JSON (no syntax errors)
- [ ] Skills: All 3 SKILL.md files present
- [ ] ZIP: Files at root (not nested), < 5 MB
- [ ] Testing: Local install successful with `atk install`

## 📁 Key Files

| File | Purpose |
|------|---------|
| `README.md` | Main docs (start here) |
| `DEPLOYMENT.md` | Step-by-step deployment guide |
| `MCP_SERVER_INTEGRATION.md` | MCP server technical details |
| `CONTRIBUTING.md` | How to add skills |
| `ICON_SETUP.md` | Icon creation guide |
| `manifest.json` | Plugin manifest (M365 v1.28) |
| `package.json` | npm scripts |

## 🎯 Troubleshooting

| Problem | Solution |
|---------|----------|
| Skills don't appear | Check manifest.json validity, skill folder names match `name` field, ZIP structure correct |
| MCP connection fails | Verify internet, test curl to learn.microsoft.com/api/mcp, check firewall |
| ZIP upload fails | Validate structure (no nested folders), check file size, ensure manifest.json exists |
| Icons not showing | Verify sizes (192×192 and 32×32), ensure PNG format, check file names match manifest |

## 🔗 Important URLs

| Resource | URL |
|----------|-----|
| MCP Server | https://learn.microsoft.com/api/mcp |
| Admin Center | https://admin.microsoft.com |
| Intune Admin | https://intune.microsoft.com |
| Plugin Docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development |
| Repository | https://github.com/Microsoft/CopilotDevCamp |

## 📊 Skill Details

### Foundry Research
- **Folder**: `skills/foundry-research/`
- **Searches**: Multiple topics (platform, models, deployment, best practices)
- **Output**: Structured markdown research document with citations
- **MCP Calls**: 4-6 searches + 5-8 article fetches

### Dev Camp PowerPoint
- **Folder**: `skills/dev-camp-deck/`
- **Input**: Topic, audience, duration, depth
- **Output**: Professional .pptx with speaker notes (10-25 slides)
- **MCP Calls**: 5-7 searches + 8-12 article fetches

### Dev Camp Document
- **Folder**: `skills/dev-camp-document/`
- **Input**: Topic, audience, document type, length
- **Output**: Professional .docx with formatting (1-15 pages)
- **MCP Calls**: 5-7 searches + 8-12 article fetches

## 🛠️ Manifest Structure

```json
{
  "id": "GUID",                              // Unique identifier
  "manifestVersion": "1.28",                 // Required version
  "version": "1.0.0",                        // Plugin version
  "agentSkills": [                           // Array of skills
    { "folder": "./skills/skill-name" }     // One per skill
  ],
  "agentConnectors": [                       // Array of MCP servers
    {
      "id": "connector-id",
      "displayName": "Display Name",
      "toolSource": {
        "remoteMcpServer": {
          "mcpServerUrl": "https://..."      // MCP server URL
        }
      }
    }
  ]
}
```

## 📝 Skill Frontmatter Template

```yaml
---
name: skill-name-kebab-case    # Must match folder name
description: |                 # Include trigger phrases
  What this skill does.
  Use when user asks to "trigger 1", "trigger 2".
license: MIT
metadata:
  author: Copilot Dev Camp
  version: "1.0"
---
```

## ⚙️ MCP Server Details

**Microsoft Learn MCP Server**

```
URL: https://learn.microsoft.com/api/mcp
Auth: None
Transport: JSON-RPC 2.0 over HTTP
TLS: Required (1.2+)
Tools: search-learn, get-learn-article, get-learn-samples
Rate Limit: 100 req/min per user, 1000 req/min per tenant
Timeout: 30 seconds (Cowork), 60 seconds (server)
```

## 🎓 Documentation Map

```
README.md (⭐ Start here)
├─ Quick Start
├─ Features Overview
├─ Troubleshooting
└─ FAQ

↓ For deployment:
DEPLOYMENT.md
├─ Prerequisites
├─ Local Testing
├─ Packaging Steps
├─ Deployment Options
└─ Verification

↓ For technical details:
MCP_SERVER_INTEGRATION.md
├─ Server Capabilities
├─ Tool Specifications
├─ Performance Characteristics
└─ Troubleshooting

↓ For development:
CONTRIBUTING.md
├─ Code of Conduct
├─ Creating New Skills
├─ Pull Request Process
└─ Style Guidelines

↓ For icons:
ICON_SETUP.md
├─ Requirements
├─ Design Guidelines
└─ Creation Tools
```

## 🚀 Deployment Checklist

### Before Packaging
- [ ] Icons added (color.png, outline.png)
- [ ] manifest.json validated
- [ ] All SKILL.md files present
- [ ] Folder structure verified

### Packaging
- [ ] ZIP created correctly (files at root)
- [ ] ZIP extracted and verified
- [ ] ZIP size < 10 MB

### Before Upload
- [ ] Local test with `atk install` passes
- [ ] Skills appear in Cowork
- [ ] All three skills trigger correctly

### After Upload
- [ ] Skills appear in Cowork > Sources & Skills
- [ ] MCP connection working
- [ ] Each skill produces expected output

## 📞 Support

- 📖 **Docs**: Read relevant .md files
- 💬 **Discussion**: GitHub Discussions
- 🐛 **Issues**: GitHub Issues
- 📧 **Email**: copilot-dev-camp@microsoft.com

## 🔗 Quick Links

| Link | Purpose |
|------|---------|
| [Microsoft Learn MCP](https://learn.microsoft.com/en-us/training/support/mcp) | MCP Server documentation |
| [Cowork Plugin Docs](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development) | Official plugin development |
| [M365 Manifest Schema](https://developer.microsoft.com/json-schemas/teams/v1.28/MicrosoftTeams.schema.json) | Manifest JSON schema |
| [Agent Skills Spec](https://docs.anthropic.com/en/docs/skills) | Agent Skills format |
| [Fluent Icons](https://fluent-icons.com) | Find icons for your plugin |

## 💾 File Sizes

Typical file sizes for reference:

| File | Size |
|------|------|
| manifest.json | < 2 KB |
| color.png (192×192) | 20-50 KB |
| outline.png (32×32) | 2-5 KB |
| SKILL.md (average) | 10-20 KB |
| skills/ folder | 60-80 KB |
| **Total ZIP** | **< 5 MB** |

---

**Version**: 1.0.0 | **Updated**: June 2026 | **Status**: Production Ready ✅
