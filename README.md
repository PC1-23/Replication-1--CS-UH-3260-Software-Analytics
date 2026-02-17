<p style="border:1px; border-style:solid; border-color:black; padding: 1em;">
CS-UH 3260 Software Analytics<br/>
Replication Study 1<br/>
Pragya Chapagain and Pavel Nikolaitchev, NYUAD
</p>

# Replication Repository 1 README -- CS-UH-3260 Software Analytics


## Overview

This repo provides a template and and guidelines for creating a README file for your replication study repository. The README serves as the primary documentation for your repository and helps evaluators understand your work, navigate your repository structure, and reproduce your replication. You can create a repo based on this template and modify the README and content as needed.


## README Structure Template

Your repository README should include the following sections:

### 1. Project Title and Overview

- **Paper Title**: How do Developers Improve Code Readability? An Empirical Study of Pull Requests
- **Authors**: Anonymous 1, Anonymous 2, Anonymous 3
- **Replication Team**: Pragya Chapagain and Pavel Nikolaitchev
- **Course**: CS-UH 3260 Software Analytics, NYUAD
- **Brief Description**: 
  - The original paper studies how developers improve code readability through pull requests in open-source Java projects. The authors mined 109 GitHub repositories, identified readability-related PRs using keyword search, and manually classified them into a taxonomy of improvement types to understand what kinds of readability changes developers make and accept. The study also contrasts developer intended readability improvements with SonarQube detected issues, concluding that many practical readability changes are not fully captured by existing static analysis rules.
  - This replication study validates the original authors' methodology by manually classifying a random sample of 10 PRs from their dataset (RQ1) and running their SonarQube analysis (RQ2). We also extend the study by collecting new PRs from 2021-2026 across 5 selected repositories to analyze how the distribution of readability improvement types has changed over time compared to the original study period.

### 2. Repository Structure

Document your repository structure clearly. Organize your repository using the following standard structure:

```
README                    # This file
datasets/                 # Data used in the replication
replication_scripts/      # Scripts used for data collection (created new script)
outputs/                  # Classification results and analysis
logs/                     # Console outputs screenshot from running collect_new_prs.py

```

**For each folder and file, provide a brief description of what it contains.**

- datasets/

  - 10_sampled_prs.xlsx - Random sample of 10 PRs from the original authors' dataset used for manual classification validation (RQ1 replication).

- replication_scripts/

  - collect_new_prs.py - New script written to collect readability related PRs from 5 selected repositories for the period 2021-2026. Adapted from the authors' original importPullRequests.py. Uses the same GitHub GraphQL API, same 8 readability keywords, and same search filters (is:pr is:merged review:approved), but outputs directly to CSV instead of storing in a MySQL database.

- outputs/

  - Classification results and distribution analysis will be added here.
  - new_prs_2021_2026.csv - New pull requests collected from 5 selected repositories for the period 2021-2026. Mined using the same keyword search methodology as the original study. Contains PR number, URL, title, body, merge date, author, merged by, matched keywords, commit messages, and comments.

- logs/

  -  Screenshots and console output from data collection runs (collect_new_prs.py).

- notes/


### 3. Setup Instructions

### What you need:
- Python 3.7+
- GitHub account

### Setup:

1. Clone this repo
2. Install requests: `pip install requests`
3. Get a GitHub token from https://github.com/settings/tokens (needs `public_repo` scope)
4. Create `replication_scripts/config.py` with your token:
```python
   GITHUB_TOKEN = 'ghp_yourTokenHere'
```
5. Run the script:
```bash
   cd replication_scripts
   python3 collect_new_prs.py
```

### 4. GenAI Usage

**GenAI Usage**: Briefly document any use of generative AI tools (e.g., ChatGPT, GitHub Copilot, Cursor) during the replication process. Include:

  - Understanding the original authors' script (importPullRequests.py) - Claude helped explain the MySQL database structure, GraphQL API queries, and the overall data collection workflow
  - Debugging - Claude assisted with Git issues (token security, .gitignore setup, staging files) and Python errors during script development
  - Understanding the GraphQL API when writing new script


## Grading Criteria for README

Your README will be evaluated based on the following aspects (Total: 40 points):

### 1. Completeness (10 points)
- [ ] All required sections are present
- [ ] Each section contains sufficient detail
- [ ] Repository structure is fully documented
- [ ] All files and folders are explained
- [ ] GenAI usage is documented (if any AI tools were used)

### 2. Clarity and Organization (5 points)
- [ ] Information is well-organized and easy to follow
- [ ] Instructions are clear and unambiguous
- [ ] Professional writing and formatting
- [ ] Proper use of markdown formatting (headers, code blocks, lists)

### 3. Setup and Reproducibility (10 points)
- [ ] Setup instructions are complete and accurate, i.e., we were able to rerun the scripts following your instructions and obtain the results you reported


## Best Practices

1. **Be Specific**: Include exact versions, paths, and commands rather than vague descriptions
2. **Keep It Updated**: Ensure the README reflects the current state of your repository
3. **Test Your Instructions**: Have someone else (or yourself in a fresh environment) follow the setup instructions
4. **Document AI Usage**: If you used any GenAI tools, be transparent about how they were used (e.g., understanding scripts, exploring datasets, understanding data fields)


## Acknowledgement

This guideline was developed with the assistance of [Cursor](https://www.cursor.com/), an AI-powered code editor. This tool was used to:

- Draft and refine this documentation iteratively
