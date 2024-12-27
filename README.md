![](https://github.com/user-attachments/assets/0efd69aa-b9c3-4876-b080-5fe8c18381a9)

<h2 align="center"> Daksh SCRA: A Source Code Review Assist Tool</h2>

<div id="header" align="center">
  <div id="badges">
  <a href="https://x.com/coffeensecurity">
    <img src="https://img.shields.io/badge/Twitter-blue?style=flat-square&logo=x&logoColor=black" alt="Follow Coffee & Security"/>
  </a>
  <a href="mailto:d3basis.m0hanty@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-red?style=flat-square&logo=gmail&logoColor=white" alt="Mail to Debasis Mohanty"/>
  </a>
  <a href="https://www.coffeeandsecurity.com">
    <img src="https://img.shields.io/badge/Website-indigo?style=flat-square&logo=&logoColor=white" alt="Visit Website"/>
  </a>
  </div>

  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-GPL-brightgreen?style=flat-square" alt="GPL License">
  </a>
  <a href="https://github.com/coffeeandsecurity/DakshSCRA/stargazers">
    <img src="https://badgen.net/github/stars/coffeeandsecurity/DakshSCRA?style=flat-square" alt="DakshSCRA GitHub Stars">
  </a>
  <a href="https://github.com/coffeeandsecurity/DakshSCRA/fork">
    <img src="https://badgen.net/github/forks/coffeeandsecurity/DakshSCRA?style=flat-square" alt="DakshSCRA GitHub Forks">
  </a>
</div>
<br/>

```
Author:
- Debasis Mohanty (d3basis.m0hanty@gmail.com)
- Twitter: @coffeensecurity
- www.coffeeandsecurity.com
```

## Introduction

The [Daksh SCRA Tool](https://github.com/coffeeandsecurity/DakshSCRA) is built to enhance the efficiency of the source code review process, providing a well-structured and organized approach for code reviewers.

Rather than indiscriminately flagging everything as a potential issue, Daksh SCRA promotes thoughtful analysis, urging the investigation and confirmation of potential problems. This approach mitigates the scramble to tag every potential concern as a bug, cutting back on the confusion and wasted time spent on false positives.

What sets Daksh SCRA apart is its emphasis on avoiding unnecessary bug tagging. Unlike conventional methods, it advocates for thorough investigation and confirmation of potential issues before tagging them as bugs. This approach helps mitigate the issue of false positives, which often consume valuable time and resources, thereby fostering a more productive and efficient code review process.

## Getting Started

### Setup DakshSCRA

Before using DakshSCRA, make sure you have installed [Python3](https://www.python.org/downloads/) and the packages through the command line using [pip](https://pip.pypa.io/en/stable/installation/).

#### 1. Clone the repository

```bash
$ git clone https://github.com/coffeeandsecurity/DakshSCRA.git

$ cd ./DakshSCRA
```

#### 2. Setup a virtual environment

```bash
$ pip install virtualenv

# Create virtual environment
$ virtualenv -p python3 venv

# Active the virtual environment
$ source ./venv/bin/activate
```

#### 3. Install All Dependencies

```bash
# Install dependencies after activating the virtualenv
(venv) $ pip install -r ./requirements.txt
```

## Features

- **Identifies Areas of Interest in Source Code:** Encourage focused investigation and confirmation rather than indiscriminately labeling everything as a bug.

- **Identifies Areas of Interest in File Paths (World’s First):** Recognizes patterns in file paths to pinpoint relevant sections for review.

- **Software-Level Reconnaissance to Identify Technologies Utilized:** Identifies project technologies, enabling code reviewers to conduct precise scans with appropriate rules.

- **Automated Scientific Effort Estimation for Code Review (World’s First):** Providing a measurable approach for estimating efforts required for a code review process.

> While this tool has progressed beyond its early stages, it has reached a usable and effective state. However, active enhancements are underway, and several new features and improvements are expected soon.

Refer to the wiki for the tool setup, functionalities and usage details - [DakshSCRA Wiki](https://github.com/coffeeandsecurity/DakshSCRA/wiki).

## Supported Languages and Frameworks

DakshSCRA supports a wide range of programming languages and frameworks. Here are some of the popular languages and frameworks that you can scan your source code with DakshSCRA Tool:

<p align="left">
  <img width="65" height="65" src="https://img.icons8.com/color/65/javascript--v1.png" alt="javascript--v1"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/php.png" alt="php"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/net-framework.png" alt="net-framework"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/java-coffee-cup-logo--v1.png" alt="java-coffee-cup-logo--v1"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/kotlin.png" alt="kotlin"/>
  <br>
  <img width="65" height="65" src="https://img.icons8.com/color/65/python--v1.png" alt="python--v1"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/golang.png" alt="golang"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/c-programming.png" alt="c-programming"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/c-plus-plus-logo.png" alt="c-plus-plus-logo"/>
  <img width="65" height="65" src="https://img.icons8.com/color/65/android-os.png" alt="android-os"/>
</p>

## Usage

1. To get the help page:

```bash
# Show helps
(venv) $ python3 dakshscra.py -h
```

2. Supported options:

```bash 
usage: dakshscra.py [-h] [-r RULE_FILE] [-f FILE_TYPES] [-v] [-t TARGET_DIR] [-l {R,RF}] [-recon] [-estimate]
```

| Option    | Stands         | Requirement | Default Values | Extended Values                                      | Definition                                                 |
| --------- | -------------- | ----------- | -------------- | ---------------------------------------------------- | ---------------------------------------------------------- |
| -r        | RULE_FILE      | Required    | N/A            | `auto`, Single and Multiple platform rules           | Specify platform-specific rule name                        |
| -f        | FILE_TYPES     | Optional    | N/A            | `custom`, Other supported filetypes                  | Explicitly specify file types to scan                      |
| -v        | Verbosity      | Optional    | `-v`           | {`-v`, `-vv`, `-vvv`}                                | Specify verbosity level                                    |
| -t        | TARGET_DIR     | Required    | N/A            | N/A                                                  | Specify target directory path                              |
| -l        | RULES_LIST     | Optional    | N/A            | {`R`, `RF`}                                          | List rules [R] OR rules and filetypes [RF]                 |
| -recon    | Reconnaissance | Optional    | N/A            | N/A                                                  | Detects platform, framework, and programming language used |
| -estimate | Estimate       | Optional    | N/A            | N/A                                                  | Estimate efforts required for code review                  |

### Example Usage

```bash
# To view tool usage along with examples
(venv) $ python3 dakshscra.py
```

#### With options

```bash
# '-r' (single or multiple) for platform-specific rules:

-r auto -t /source_dir_path    # Auto-detect the project platform rules

-r php -t /source_dir_path    # Declear Single platform rule

-r php,java,cpp -t /source_dir_path    # Declear Multiple platform rules

# '-f' is optional. If not specified, it will default to the corresponding filetypes of the selected rule.

-r php -f dotnet -t /path_to_source_dir    # Declear filetype explicitly under specific rule (Optional)

-r php -f <custom> -t /path_to_source_dir    # Define custom filetype

# '-recon' perform reconnaissance and rule-based scanning

-recon -r php -t /path_to_source_dir    # Perform reconnaissance with rule based platform

-recon -t /path_to_source_dir    # Perform only reconnaissance

# Verbosity: '-v' is default, '-vvv' will display all rules check within each rule category.

-r php -vv -t /path_to_source_dir    # Perform verbosity at level 2
```

## Reports

The tool generates reports in three formats: HTML, PDF, and TEXT. Although the HTML and PDF reports are still being improved, they are currently in a reasonably good state. With each subsequent iteration, these reports will continue to be refined and improved even further.

### Scanning (Areas of Security Concerns) Reports

###### HTML Report Path:

- `DakshSCRA/reports/html/report.html`

###### PDF Report Path:

- `DakshSCRA/reports/html/report.pdf`

###### RAW TEXT Based Report Paths:

- Areas of Interest - Identified Patterns : `DakshSCRA/reports/text/areas_of_interest.txt`
- Areas of Interest - Project Files: `DakshSCRA/reports/text/filepaths_aoi.txt`
- Identified Project Files: `DakshSCRA/runtime/filepaths.txt`

###### Reconnaissance (Recon) Report Path:

- Reconnaissance Summary: `/reports/text/recon.txt`

Note: Currently, the reconnaissance report is created in a text format. However, in upcoming releases, the plan is to incorporate it into the vulnerability scanning report, which will be available in both HTML and PDF formats.

###### Code Review Effort Estimation Report Path:

- Effort estimation report: `/reports/html/estimation.html`

Note: Currently, the report is generated in HTML format. However, in future releases, there are plans to also provide it in PDF format.

## Debut (2022-Present)

Daksh SCRA was initially introduced during a source code review training session I conducted at Black Hat USA 2022 (August 6 - 9), where it was subtly presented to a specific audience. However, this introduction was carried out with a low-profile approach, avoiding any major announcements.

While this tool was quietly published on GitHub after the 2022 training, its official public debut took place at Black Hat USA 2023 in Las Vegas.

## Community
Our developer community is the backbone of the ongoing Daksh SCRA project. We sincerely welcome you to join our community, participate in the conversation and stay connected with us for the latest updates.

Feel free to contribute to the DakshSCRA project, submit any issues on our GitHub page. Read our [Contribution guidelines](https://github.com/coffeeandsecurity/DakshSCRA/wiki/Contribution-guidelines).

If you find any bugs, report them to [d3basis.m0hanty@gmail.com](mailto:d3basis.m0hanty@gmail.com).

> Please consider sharing your experience or thoughts about [DakshSCRA]([https://github.com/rajmanna-dev/DakshSCRA/](https://github.com/coffeeandsecurity/DakshSCRA)) with the border Open Source community. It really does help!

[![GitHub Repo stars](https://img.shields.io/badge/share%20on-reddit-red?style=flat-square&logo=reddit)](https://reddit.com/submit?url=https://github.com/coffeeandsecurity/DakshSCRA&title=Daksh%20SCRA%20A%20Source%20Code%20Review%20Assist%20Tool)
[![GitHub Repo stars](https://img.shields.io/badge/share%20on-twitter-black?style=flat-square&logo=x)](https://twitter.com/share?url=https://github.com/coffeeandsecurity/DakshSCRA&text=Daksh%20SCRA%20A%20Source%20Code%20Review%20Assist%20Tool)
[![GitHub Repo stars](https://img.shields.io/badge/share%20on-facebook-1976D2?style=flat-square&logo=facebook)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/coffeeandsecurity/DakshSCRA)
[![GitHub Repo stars](https://img.shields.io/badge/share%20on-linkedin-3949AB?style=flat-square&logo=linkedin)](https://www.linkedin.com/shareArticle?url=https://github.com/coffeeandsecurity/DakshSCRA&title=Daksh%20SCRA%20A%20Source%20Code%20Review%20Assist%20Tool)

## License

DakshSCRA is a Source Code Review Assist Tool. It is a free and open-source software licensed under the [GPL](https://github.com/coffeeandsecurity/DakshSCRA/blob/main/README.md).
