# Deployment Guide - Copilot Dev Camp for Cowork

This guide provides step-by-step instructions for packaging and deploying the Copilot Dev Camp plugin to your organization. The plugin is powered by the official **[Copilot Developer Camp](https://microsoft.github.io/copilot-camp/)** curriculum and integrates with the **Microsoft Learn MCP Server** for research capabilities.

**Created by**: Paolo Pialorsi (M365 Developer Advocates)

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Testing](#local-testing)
3. [Packaging](#packaging)
4. [Deployment Options](#deployment-options)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)
7. [Updates and Maintenance](#updates-and-maintenance)

## Prerequisites

Before you begin, ensure you have:

### Required Tools
- **PowerShell 5.0+** (Windows) OR **Bash** (macOS/Linux)
- **7-Zip**, **WinRAR**, or built-in ZIP tool
- **Node.js 14+** (optional, for npm packaging script)

### Required Access
- Microsoft 365 tenant access
- **Cowork** application available
- Admin access to **Microsoft 365 Admin Center** (for tenant-wide deployment)

### Plugin Source
- Downloaded plugin source from repository OR built from source
- Valid icon files (`color.png` 192×192, `outline.png` 32×32)
- All skill files in place

### Knowledge
- Basic understanding of ZIP file structure
- Familiarity with Microsoft 365 Admin Center
- (Optional) Understanding of JSON manifest format

## Local Testing

### Step 1: Verify Plugin Structure

Ensure your plugin directory looks like this:

```
copilot-dev-camp/
├── manifest.json              # Plugin manifest
├── color.png                  # 192×192 icon
├── outline.png                # 32×32 icon
├── skills/
│   ├── foundry-research/
│   │   └── SKILL.md
│   ├── dev-camp-deck/
│   │   └── SKILL.md
│   └── dev-camp-document/
│       └── SKILL.md
├── package.json
├── README.md
├── LICENSE
└── .gitignore
```

### Step 2: Validate manifest.json

Open `manifest.json` and verify:

```bash
# Option 1: Use an online JSON validator
# Visit https://jsonlint.com and paste manifest.json

# Option 2: Use PowerShell
$json = Get-Content manifest.json -Raw | ConvertFrom-Json
Write-Host "Manifest is valid JSON"

# Option 3: Use Node.js
node -e "console.log(JSON.parse(require('fs').readFileSync('manifest.json')))"
```

**Checklist**:
- [ ] `manifestVersion` is `1.28`
- [ ] `id` is a valid GUID
- [ ] `agentSkills` array contains 3 items
- [ ] Each skill has a `folder` property
- [ ] `agentConnectors` has Microsoft Learn MCP Server URL
- [ ] `icons.color` and `icons.outline` point to correct files

### Step 3: Validate Skill Files

Check each skill's `SKILL.md`:

```bash
# For each skill file, verify:
# 1. YAML frontmatter is between --- delimiters
# 2. name and description fields exist
# 3. name matches the folder name (kebab-case)
# 4. description includes trigger phrases
```

**Skill validation checklist**:
- [ ] `skills/foundry-research/SKILL.md` - name: `foundry-research`
- [ ] `skills/dev-camp-deck/SKILL.md` - name: `dev-camp-deck`
- [ ] `skills/dev-camp-document/SKILL.md` - name: `dev-camp-document`

### Step 4: Check Icon Files

Verify icon files exist and have correct dimensions:

**Windows PowerShell**:
```powershell
# Check file exists
Test-Path -Path "color.png"
Test-Path -Path "outline.png"

# Check dimensions using [System.Drawing]
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("color.png")
"Color icon: $($img.Width)x$($img.Height)"
$img.Dispose()
```

**macOS/Linux**:
```bash
# Using ImageMagick (if installed)
identify color.png outline.png

# Using file command (basic info)
file color.png outline.png
```

## Packaging

### Option 1: PowerShell (Windows)

```powershell
# Navigate to plugin directory
cd C:\path\to\copilot-dev-camp

# Create ZIP file with all required contents
Compress-Archive -Path manifest.json, color.png, outline.png, skills `
  -DestinationPath copilot-dev-camp.zip -Force

# Verify ZIP contents
Expand-Archive -Path copilot-dev-camp.zip -DestinationPath verify
Get-ChildItem -Path verify -Recurse
Remove-Item -Path verify -Recurse  # Cleanup verification

Write-Host "✓ Plugin packaged: copilot-dev-camp.zip"
```

### Option 2: npm Script

```bash
npm run package          # Windows PowerShell
npm run package:unix     # macOS/Linux
```

The script uses the commands defined in `package.json`.

### Option 3: Manual ZIP (macOS/Linux)

```bash
cd /path/to/copilot-dev-camp

# Create ZIP with proper structure (files at root)
zip -r copilot-dev-camp.zip manifest.json color.png outline.png skills/

# Verify structure
unzip -l copilot-dev-camp.zip | head -20

echo "✓ Plugin packaged: copilot-dev-camp.zip"
```

### Step 5: Verify ZIP Structure

**Critical**: Files must be at the ROOT level of the ZIP, not nested.

**✓ Correct structure inside ZIP**:
```
copilot-dev-camp.zip
├── manifest.json
├── color.png
├── outline.png
└── skills/
    └── [skill folders]
```

**✗ Incorrect structure (common mistake)**:
```
copilot-dev-camp.zip
└── copilot-dev-camp/        ← Don't nest in a folder!
    ├── manifest.json
    ├── color.png
    ...
```

**Verify with**:
```bash
# List ZIP contents - should start with manifest.json, not a folder
unzip -l copilot-dev-camp.zip
```

## Deployment Options

### Option A: Individual User Installation (Quickest)

Use the Microsoft 365 Agents Toolkit CLI to install for personal use.

**Step 1: Install the toolkit**
```bash
npm install -g @microsoft/m365agentstoolkit-cli
```

**Step 2: Verify installation**
```bash
atk --version
```

**Step 3: Authenticate**
```bash
atk auth login
```
Follow the browser prompts to sign in with your Microsoft 365 account.

**Step 4: Install the plugin**
```bash
atk install --file-path "C:/path/to/copilot-dev-camp.zip" --scope Personal
```

Expected output:
```
✓ Installation successful
TitleId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AppId: yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
```

**Save these IDs** for future updates or uninstalls.

**Step 5: Verify installation**
```bash
atk list --scope Personal
```

### Option B: Tenant-Wide Deployment (Admin)

Deploy to entire organization through Microsoft 365 Admin Center.

**Step 1: Access Admin Center**
1. Open [Microsoft 365 Admin Center](https://admin.microsoft.com)
2. Sign in with admin credentials
3. Navigate to **Manage Apps** section
   - Older path: **Teams & Skype** → **Manage Apps** (may vary by version)
   - Newer path: **Applications** → **Manage Apps** or **Agents** → **All agents**

**Step 2: Upload Custom App**
1. Click **Upload custom app** or **+ Add agent**
2. Click **Select file**
3. Choose your `copilot-dev-camp.zip`
4. Click **Upload** or **Next**

**Step 3: Configure (if applicable)**
- Review plugin details
- Set organizational policies
- Configure scope (Personal, Team, Organization)

**Step 4: Publish**
- Click **Publish** or **Deploy**
- Select target users/groups
- Confirm and deploy

**Step 5: Monitor Rollout**
- Track deployment status in Admin Center
- Allow 15-30 minutes for sync to all users
- Check dashboard for any errors

### Option C: Group Policy Deployment

For enterprise environments with Microsoft Intune:

**Step 1: Prepare**
1. Host `.zip` file on internal server or SharePoint
2. Create deployment policy
3. Define target groups

**Step 2: Deploy via Intune**
1. Open [Microsoft Intune Admin Center](https://intune.microsoft.com)
2. Navigate to **Apps** → **Manage apps** → **Microsoft 365 apps**
3. Upload plugin package
4. Configure assignment rules
5. Deploy to target groups

**Step 3: Monitor**
- View deployment reports
- Check installation status per device
- Handle any failures

## Verification

### Verify Installation Success

**For Personal Installation**:
```bash
# Using ATK CLI
atk list --scope Personal

# Should show:
# - Plugin name: Copilot Dev Camp
# - Status: Installed
# - TitleId and AppId
```

**For Tenant-Wide**:
1. Go to Microsoft 365 Admin Center
2. Check **Manage Apps** > **Upload custom apps**
3. Look for "Copilot Dev Camp"
4. Verify status shows "Published" or "Available"

### Verify in Cowork

1. Open **Microsoft 365 Copilot** (M365 home page or Teams)
2. Navigate to **Cowork** tab
3. Go to **Sources & Skills** panel
4. You should see:
   - 📦 **Copilot Dev Camp** (plugin name)
   - 🧠 **Microsoft Foundry Research** (skill)
   - 📊 **Dev Camp PowerPoint Deck** (skill)
   - 📝 **Dev Camp Word Document** (skill)

### Test Each Skill

**Test Foundry Research**:
```
Prompt: "Research Microsoft Foundry platform architecture"
Expected: Comprehensive research summary with documentation links
```

**Test Dev Camp Deck**:
```
Prompt: "Create a PowerPoint presentation about Microsoft Foundry for developers"
Expected: Generated .pptx file ready to download
```

**Test Dev Camp Document**:
```
Prompt: "Write a technical guide on deploying models with Foundry"
Expected: Generated .docx file ready to download
```

## Troubleshooting

### Skills Don't Appear in Cowork

**Symptom**: Plugin installed but skills missing from **Sources & Skills**

**Solutions**:
1. **Verify manifest.json**:
   ```bash
   # Ensure no syntax errors
   node -e "console.log(JSON.parse(require('fs').readFileSync('manifest.json')))"
   ```

2. **Check skill folder names**:
   - Folder: `skills/foundry-research/` → name in SKILL.md: `foundry-research` ✓
   - Folder: `skills/dev-camp-deck/` → name in SKILL.md: `dev-camp-deck` ✓
   - Folder: `skills/dev-camp-document/` → name in SKILL.md: `dev-camp-document` ✓

3. **Reinstall plugin**:
   ```bash
   atk uninstall --title-id <TitleId>
   atk install --file-path ./copilot-dev-camp.zip --scope Personal
   ```

4. **Clear cache**:
   - Sign out of Cowork
   - Close browser completely
   - Wait 5 minutes
   - Sign back in

### MCP Connection Fails

**Symptom**: "Cannot connect to Microsoft Learn" or timeout errors

**Solutions**:
1. **Check network connectivity**:
   ```bash
   # Test if learn.microsoft.com is reachable
   ping learn.microsoft.com
   nslookup learn.microsoft.com
   ```

2. **Check firewall rules**:
   - Ensure HTTPS (port 443) is open to learn.microsoft.com
   - Check corporate proxy doesn't block the domain
   - Verify TLS 1.2+ support

3. **Test MCP endpoint**:
   ```bash
   # Windows PowerShell
   $response = Invoke-WebRequest -Uri "https://learn.microsoft.com/api/mcp" -UseBasicParsing
   $response.StatusCode  # Should be 200 or 405 (not available for direct request)
   ```

4. **Wait and retry**:
   - MCP Server occasionally needs 30-60 seconds to respond
   - Retry after waiting

### ZIP Structure Issues

**Symptom**: "Invalid package structure" or "Cannot find SKILL.md" errors

**Solution - Verify ZIP structure**:
```bash
# List ZIP contents
unzip -l copilot-dev-camp.zip | head -20

# Should look like:
# Archive:  copilot-dev-camp.zip
#   Length      Date    Time    Name
# ---------  ---------- -----   ----
#       XXX  2026-06-23 10:00   manifest.json
#       XXX  2026-06-23 10:00   color.png
#       ...
```

**Fix**: Recreate ZIP ensuring files are at root level, not nested.

### Upload Fails in Admin Center

**Symptom**: "Upload failed" or "Invalid package" in admin portal

**Solutions**:
1. **Check file size**: ZIP should be < 10 MB (typically < 2 MB)
2. **Verify manifest format**: Ensure valid JSON (no trailing commas)
3. **Test with different browser**: Try Edge or Chrome
4. **Try admin center refresh**: Logout and back in
5. **Check tenant permissions**: Ensure you're a Global Admin

## Updates and Maintenance

### Update Plugin Version

**Step 1: Update source files**
```bash
# Modify skills, update version in manifest and package.json
# Update version: "version": "1.1.0"
```

**Step 2: Repackage**
```bash
npm run package
# Or use PowerShell/zip command
```

**Step 3: Reinstall**

**For personal use**:
```bash
atk update --title-id <TitleId> --file-path ./copilot-dev-camp.zip
```

**For tenant**:
1. Go to Admin Center > Manage Apps
2. Find "Copilot Dev Camp"
3. Select **Update** or **Upload new version**
4. Select new ZIP file
5. Confirm update

### Uninstall Plugin

**Personal uninstall**:
```bash
atk uninstall --title-id <TitleId>
```

**Tenant uninstall**:
1. Admin Center > Manage Apps
2. Find "Copilot Dev Camp"
3. Click **...** (More options)
4. Select **Delete** or **Remove**
5. Confirm

### Monitor Usage

**Track in Admin Center**:
1. Go to **Manage Apps** > **Installed apps**
2. Find "Copilot Dev Camp"
3. View:
   - Installation date
   - Usage metrics
   - User adoption
   - Any errors

## Rollback Procedure

If you need to revert to a previous version:

1. **Get previous version** from releases or backups
2. **Uninstall current version** (see above)
3. **Repackage previous version**
4. **Reinstall using previous ZIP file**
5. **Verify all three skills appear**

## Support & Assistance

- 📧 **Email**: copilot-dev-camp@microsoft.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/Microsoft/CopilotDevCamp/issues)
- 💬 **Discussion**: [GitHub Discussions](https://github.com/Microsoft/CopilotDevCamp/discussions)

---

**Last updated**: June 2026
**Manifest version**: 1.28
**Plugin version**: 1.0.0
