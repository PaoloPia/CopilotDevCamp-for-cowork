# Microsoft Learn MCP Server Integration

This document explains how the Copilot Dev Camp plugin integrates with data sources and how it powers the three skills.

## Overview

The Copilot Dev Camp plugin leverages two primary, authoritative sources for content:

### 1. Microsoft Learn MCP Server
The **Microsoft Learn MCP Server** is a public remote MCP (Model Context Protocol) server that provides access to Microsoft's official documentation. The server is hosted at:

```
https://learn.microsoft.com/api/mcp
```

### 2. Copilot Developer Camp
The **[Copilot Developer Camp](https://microsoft.github.io/copilot-camp/)** provides official training materials, labs, and hands-on tutorials, complementing the Microsoft Learn resources with structured learning paths and real-world scenarios.

### Key Characteristics

| Property | Value |
|----------|-------|
| **URL** | https://learn.microsoft.com/api/mcp |
| **Authentication** | None required |
| **Transport** | Streamable HTTP with JSON-RPC 2.0 |
| **TLS** | Required (TLS 1.2+) |
| **Uptime SLA** | 99.9% availability |
| **Rate Limits** | Reasonable limits for enterprise use |
| **Response Time** | Typically < 5 seconds per call |

## Server Capabilities

The Microsoft Learn MCP Server exposes tools for:

### 1. Search Documentation
- **Tool**: `search-learn`
- **Purpose**: Full-text search across Microsoft Learn
- **Usage**: Find relevant articles on a topic
- **Returns**: List of matching articles with titles, URLs, and summaries

### 2. Fetch Article Content
- **Tool**: `get-learn-article`
- **Purpose**: Retrieve full content of a specific article
- **Usage**: Get detailed information on a topic
- **Returns**: Article text, metadata, code examples

### 3. Fetch Code Samples
- **Tool**: `get-learn-samples`
- **Purpose**: Access code samples from Learn
- **Usage**: Find implementation examples
- **Returns**: Code snippets with language and context

## Copilot Developer Camp as Complementary Source

The **[Copilot Developer Camp](https://microsoft.github.io/copilot-camp/)** serves as a complementary data source, providing:

- **Official Training Materials**: Structured labs and learning modules
- **Hands-On Tutorials**: Step-by-step walkthroughs with working examples
- **Real-World Scenarios**: Practical use cases and patterns from training curriculum
- **Best Practices**: Recommended approaches based on training content
- **Code Samples**: Working examples from the Dev Camp labs
- **Slide Templates**: Presentation materials for training and sharing

Skills integrate Dev Camp resources alongside Microsoft Learn to provide:
1. Comprehensive coverage of both foundational concepts and practical applications
2. Real-world scenarios demonstrated in training
3. Structured learning paths from official curriculum
4. Code samples tested in hands-on labs

## How Skills Use Both Data Sources

### Data Integration Strategy

Skills use a two-stage research approach:

**Stage 1: Microsoft Learn (via MCP Server)**
- Search for comprehensive technical documentation
- Fetch detailed architecture and implementation guides
- Access official API references and best practices

**Stage 2: Copilot Developer Camp**
- Reference official training content for context
- Include practical examples from Dev Camp labs
- Align with training curriculum and learning objectives

## How Skills Use the MCP Server

### 🧠 Foundry Research Skill

**Workflow**:
1. User provides a topic (e.g., "Microsoft Foundry architecture")
2. Skill uses `search-learn` tool to search for:
   - "Microsoft Foundry platform overview"
   - "Microsoft Foundry models and capabilities"
   - "Microsoft Foundry deployment options"
   - "Microsoft Foundry best practices"
3. Skill collects results from multiple searches
4. Uses `get-learn-article` to fetch full content of top matches
5. Organizes findings into research summary
6. Includes direct links to Learn articles

**MCP Tool Calls**: 4-6 searches + 5-8 article fetches

### 📊 Dev Camp PowerPoint Deck Skill

**Workflow**:
1. User specifies topic, audience, and duration
2. Skill researches using `search-learn`:
   - Topic overview and introduction
   - Architecture and design patterns
   - Implementation guide
   - Best practices and optimization
   - Code examples and quickstarts
   - Real-world scenarios
3. Uses `get-learn-article` for comprehensive content
4. Organizes into slide structure
5. Creates PowerPoint with speaker notes and source links

**MCP Tool Calls**: 5-7 searches + 8-12 article fetches

### 📝 Dev Camp Document Skill

**Workflow**:
1. User specifies topic, audience, and document type
2. Skill researches using `search-learn`:
   - Topic overview and context
   - Architecture and design
   - Implementation and configuration
   - Best practices and optimization
   - Troubleshooting and common issues
   - Comparisons with related technologies
3. Uses `get-learn-article` for detailed information
4. Structures based on document type (one-pager, guide, etc.)
5. Creates Word document with formatting and citations

**MCP Tool Calls**: 5-7 searches + 8-12 article fetches

## Tool Specifications

### search-learn

Searches Microsoft Learn documentation.

**Input**:
```json
{
  "query": "string",           // Search query
  "max_results": 10,          // Optional: max results to return
  "include_samples": false    // Optional: include code samples
}
```

**Output**:
```json
{
  "results": [
    {
      "title": "Article Title",
      "url": "https://learn.microsoft.com/...",
      "description": "Short summary",
      "service": "Azure AI",
      "updated": "2026-06-15"
    }
  ],
  "total_results": 42
}
```

### get-learn-article

Retrieves full content of a Learn article.

**Input**:
```json
{
  "url": "https://learn.microsoft.com/...",  // Learn article URL
  "format": "markdown"                       // Optional: markdown or html
}
```

**Output**:
```json
{
  "title": "Article Title",
  "url": "https://learn.microsoft.com/...",
  "content": "Full article markdown content...",
  "metadata": {
    "author": "Author Name",
    "updated": "2026-06-15",
    "service": "Azure AI",
    "level": "Beginner"
  }
}
```

### get-learn-samples

Retrieves code samples associated with topics.

**Input**:
```json
{
  "query": "Foundry model deployment",
  "language": "python",              // Optional: python, csharp, javascript
  "max_samples": 5                   // Optional: max samples
}
```

**Output**:
```json
{
  "samples": [
    {
      "title": "Sample Name",
      "language": "python",
      "code": "def example(): ...",
      "description": "What this does",
      "source_url": "https://..."
    }
  ]
}
```

## Configuration in manifest.json

The plugin configures the MCP server connection in `manifest.json`:

```json
{
  "agentConnectors": [
    {
      "id": "microsoft-learn-mcp",
      "displayName": "Microsoft Learn MCP Server",
      "description": "Access to Microsoft documentation for research",
      "toolSource": {
        "remoteMcpServer": {
          "mcpServerUrl": "https://learn.microsoft.com/api/mcp"
        }
      }
    }
  ]
}
```

### No Authentication Required

The Microsoft Learn MCP Server is public and requires no authentication:
- ✅ No API key needed
- ✅ No OAuth setup required
- ✅ No credentials stored in manifest
- ✅ Immediate access for all users

## Performance Characteristics

### Response Times

Typical response times for MCP operations:

| Operation | Time |
|-----------|------|
| Search 10 results | 2-4 seconds |
| Fetch article (10 KB) | 1-2 seconds |
| Fetch article (50 KB) | 3-5 seconds |
| Multiple searches (5x) | 10-15 seconds |

### Throttling & Rate Limits

The server implements reasonable rate limits:
- **Per-user**: 100 requests/minute (typical)
- **Per-tenant**: 1000 requests/minute
- **Burst capacity**: Handles 10-20 concurrent requests

Most skills complete within these limits.

### Timeout Configuration

- **Cowork timeout**: 30 seconds per tool call
- **MCP Server timeout**: 60 seconds (internal)
- **Connection timeout**: 10 seconds

Skills should complete within Cowork's 30-second window.

## Content Coverage

The Microsoft Learn MCP Server indexes:

### Documentation Areas
- Azure services and products
- Microsoft 365 and collaboration
- Microsoft Foundry and AI/ML
- Developer tools and frameworks
- Security and compliance
- Training paths and learning modules

### Content Types
- Overview and architecture articles
- Getting started guides
- How-to and tutorial articles
- API reference documentation
- Code samples and quickstarts
- Best practices and patterns
- Migration guides and decision trees

### Update Frequency
- **Incremental updates**: Continuous (within hours)
- **Full refresh**: Daily (overnight, typically)
- **Latest content**: Within 24 hours of publish

## Best Practices for Using MCP Server

### ✅ Do's

- **Use specific search queries**: "Foundry model deployment Azure" instead of "Foundry"
- **Search multiple aspects**: "architecture", "implementation", "best practices"
- **Fetch top results**: Get detailed content from top 3-5 matches
- **Cite sources**: Include direct links to Learn articles
- **Handle pagination**: Request results in chunks if needed
- **Cache results**: Reuse search results within same session
- **Provide context**: Tell users results come from Learn

### ❌ Don'ts

- **Don't search for off-topic content**: Server focuses on Microsoft tech
- **Don't expect real-time updates**: Content refreshes overnight
- **Don't abuse rate limits**: Spread requests over time
- **Don't ignore errors**: Handle timeouts gracefully
- **Don't return raw JSON**: Format results for users
- **Don't embed secrets**: Never store API keys in skills
- **Don't bypass authentication**: Use configured connection

## Troubleshooting MCP Connection

### Connection Failures

**Symptom**: "Cannot connect to Microsoft Learn MCP Server"

**Diagnosis**:
1. Check internet connectivity
2. Verify firewall allows HTTPS to learn.microsoft.com
3. Confirm TLS 1.2+ support
4. Check network proxy doesn't block domain

**Solution**:
```bash
# Test connectivity
curl -I https://learn.microsoft.com/api/mcp
# Should return HTTP 200 or 405 (not error)

# Verify DNS
nslookup learn.microsoft.com
```

### Timeout Errors

**Symptom**: "Request timed out" or skill hangs

**Causes**:
- Network latency > 30 seconds
- Server experiencing high load
- MCP tool call too expensive (too many results)

**Solutions**:
1. Reduce search scope (fewer queries)
2. Limit results per query (`max_results: 5`)
3. Retry after waiting
4. Check MCP server status

### Empty Results

**Symptom**: "No results found" for valid queries

**Causes**:
- Topic not covered in Learn documentation
- Search query too specific
- Typo in search term
- Content not indexed yet

**Solutions**:
1. Try broader search terms
2. Check alternative keywords
3. Wait for content to index (usually < 24 hours)
4. Verify topic is in Microsoft Learn coverage

## Future Enhancements

Potential improvements to MCP integration:

- [ ] Custom content indexing for organization-specific docs
- [ ] Enhanced search filtering (by service, level, language)
- [ ] Video content access
- [ ] Interactive learning path recommendations
- [ ] Feedback loop to improve search relevance
- [ ] Multi-language support
- [ ] Premium content access for enterprise tenants

## References

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Microsoft Learn](https://learn.microsoft.com/)
- [Microsoft Learn MCP Server](https://learn.microsoft.com/en-us/training/support/mcp)
- [Cowork Plugin Development](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development)

---

**Last updated**: June 2026
**MCP Server URL**: https://learn.microsoft.com/api/mcp
**Status**: Production
