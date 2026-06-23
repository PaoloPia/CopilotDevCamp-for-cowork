# Icon Setup Guide

This document provides guidance on setting up icons for the Copilot Dev Camp plugin.

## Icon Requirements

This plugin requires two PNG icons:

### 1. Color Icon (`color.png`)
- **Size**: 192×192 pixels
- **Purpose**: Full-color app icon for store and app list
- **Format**: PNG with transparency support
- **Recommendation**: Use Microsoft Fluent Design System colors

### 2. Outline Icon (`outline.png`)
- **Size**: 32×32 pixels  
- **Purpose**: Single-color outline icon for compact views
- **Format**: PNG with transparency support
- **Recommendation**: Monochrome design, high contrast

## Icon Design Suggestions

The Copilot Dev Camp plugin focuses on:
- 🎓 Education and learning
- 🧠 Microsoft Foundry (AI/ML)
- 📊 Presentations and content creation
- 📝 Documentation

### Color Icon Design Ideas
- Incorporate Microsoft branding colors (Navy Blue #0078D4, Light Blue)
- Include elements suggesting: learning, technology, creativity
- Use smooth, rounded corners for modern feel
- Ensure clear visibility at 192×192 resolution

### Outline Icon Design Ideas
- Simple, bold lines
- Highly recognizable at 32×32 resolution
- Single color (typically black or white on transparent)
- High contrast for clarity

## How to Create Icons

### Option 1: Use Existing Icons
- Find icons from Microsoft Fluent UI (https://fluent-icons.com)
- Export at required sizes
- Ensure consistency with your brand

### Option 2: Design from Scratch
1. Start in a design tool (Figma, Adobe XD, Illustrator)
2. Create at 10x the required size for better quality
3. Design in the appropriate style
4. Export as PNG with transparency
5. Scale down to exact dimensions

### Option 3: Generate with AI
- Use an AI image generator with prompts like:
  - "Fluent Design icon for Microsoft Foundry learning platform, navy blue, 192x192"
  - "Outline icon for Cowork plugin, simple, monochrome, 32x32"

### Option 4: Online Tools
- Figma (free tier available)
- Pixlr
- Canva Pro
- Photopea (Photoshop alternative)

## Placeholder Icons

If you need temporary placeholder icons:

### PowerShell Script to Create Placeholders
```powershell
# This would create basic placeholder PNG files
# (In practice, use actual design tools)

# For now, copy from reference plugin:
# https://github.com/Laskewitz/learn-for-cowork/releases
```

## Validation

After creating icons:
- [ ] `color.png` is exactly 192×192 pixels
- [ ] `outline.png` is exactly 32×32 pixels
- [ ] Both are PNG format with transparency
- [ ] Icons display correctly when zoomed
- [ ] File sizes are reasonable (< 50 KB each)

## Using Icons from Reference Plugin

The [learn-for-cowork](https://github.com/Laskewitz/learn-for-cowork) plugin provides good reference icons:

1. Download their latest release
2. Extract the ZIP file
3. Copy `color.png` and `outline.png`
4. Adapt colors/branding as needed for your plugin

## Next Steps

1. Design or source your icons
2. Ensure correct dimensions and format
3. Place in the plugin root directory alongside `manifest.json`
4. Test by packaging the plugin
5. Verify icons display correctly in Cowork

## Resources

- [Microsoft Fluent UI Icons](https://fluent-icons.com) - Official Fluent icons
- [Fluent Design System](https://fluent2.microsoft.design/) - Design guidelines
- [learn-for-cowork Icons](https://github.com/Laskewitz/learn-for-cowork/releases/latest) - Reference icons
- [PNG Optimization](https://tinypng.com/) - Optimize PNG files after creation
