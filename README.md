# Daksh SCRA (Source Code Review Assist)

The Daksh SCRA (Source Code Review Assist) tool enhances the efficiency of the source code review process.

Rather than flagging everything as a potential issue, Daksh SCRA promotes thoughtful analysis, encouraging investigation and confirmation. Using this approach reduces the confusion and wasted time associated with false positives and the scramble to tag every concern as a bug.

## ☀️ Debut

Daksh SCRA was initially introduced during a source code review training session I conducted at Black Hat USA 2022 (August 6 - 9), where it was subtly presented to a specific audience. However, this introduction was carried out with a low-profile approach, avoiding any major announcements.

While this tool was quietly published on GitHub after the 2022 training, its official public debut took place at Black Hat USA 2023 in Las Vegas.

## 🚀 Features and Functionalities

- **Identifies Areas of Interest in Source Code:** Encourage focused investigation and confirmation rather than indiscriminately labeling everything as a bug.

- **Identifies Areas of Interest in File Paths (World’s First):** Recognizes patterns in file paths to pinpoint relevant sections for review.

- **Software-Level Reconnaissance to Identify Technologies Utilized:** Identifies project technologies, enabling code reviewers to conduct precise scans with appropriate rules.

- **Automated Scientific Effort Estimation for Code Review (World’s First):** Providing a measurable approach for estimating efforts required for a code review process.

> While this tool has progressed beyond its early stages, it has reached a usable and effective state. However, active enhancements are underway, and several new features and improvements are expected soon.

Additionally, the tool offers the following functionalities:

- Options to use platform-specific rules specific for finding areas of interests
- Options to extend or add new rules for any new or existing languages
- Generates report in text, HTML and PDF format for inspection

Refer to the wiki for the tool setup and usage details - [DakshSCRA Wiki](https://github.com/coffeeandsecurity/DakshSCRA/wiki).

Feel free to contribute towards updating or adding new rules and future development.

If you find any bugs, report them to [Contact](mailto:d3basis.m0hanty@gmail.com).

## 🔧 Tool Setup

### Pre-requisites

- Python3

### Setting up local environment

#### 1. Download Daksh SCRA

To Download the latest build click [here](`https://github.com/coffeeandsecurity/DakshSCRA`).
Save and unzipped the ZIP file.

##### Alternative:

```bash
	# Clone the repo
	$ git clone https://github.com/coffeeandsecurity/DakshSCRA.git

	# Go into the cloned folder
	$ cd ./DakshSCRA
```

#### 2. Setup a virtual environment

```bash
    $ pip install virtualenv

	# Create a virtualenv
    $ virtualenv -p python3 venv

	# To activate virtual environment you just created
    $ source ./venv/bin/activate

	# Ensure your virtualenv is activated successfully
	(venv) $
```

#### 3. Install Required Libraries in the Virtual Environment

```bash
	# Install all dependencies
	$ pip install -r ./requirements.txt
```

Once the libraries are installed, refer to the tool usage commands to run the tool.

## 🤖 Tool General Usage

1. To view the help page:

```bash
	# Show helps
	$ python3 dakshscra.py -h
```

2. Useful flags:

```notepad

    -r    [RULE_FILE], Specify platform-specific rule name | Default: auto

    -f    [FILE_TYPES], Specify file types to scan

    -v    Specify verbosity level {'-v', '-vv', '-vvv'}

    -t    [TARGET_DIR], Specify target directory path

    -l {R,RF} | --list {R,RF}    List rules [R] OR rules and filetypes [RF]

    -recon    Detects platform, framework, and programming language used

    -estimate    Estimate efforts required for code review
```

### Example Usage

```bash
	# To view tool usage along with examples
	$ python3 dakshscra.py
```

#### Useful flags

```bash
    # '-f' [optional]. If not specified, it will default to the corresponding filetypes of the selected rule:

	-r php -f dotnet -t /path_to_source_dir

    -r php -f custom -t /path_to_source_dir

    # '-r' (single or multiple) for platform-specific rules:

    -r auto -t /source_dir_path    # Auto-detect Platforms

    -r php -t /source_dir_path    # Single platform

    -r php,java,cpp -t /source_dir_path    # Multiple platforms

    -recon -r php -t /path_to_source_dir  # Perform reconnaissance and rule-based scanning

    -recon -t /path_to_source_dir    # Perform only reconnaissance

    # Verbosity: '-v' is default, '-vvv' will display all rules check within each rule category.

    -r php -vv -t /path_to_source_dir
```

## 📒 Reports

The tool generates reports in three formats: HTML, PDF, and TEXT. Although the HTML and PDF reports are still being improved, they are currently in a reasonably good state. With each subsequent iteration, these reports will continue to be refined and improved even further.

### Scanning (Areas of Security Concerns) Reports

###### HTML Report:

- `DakshSCRA/reports/html/report.html`

###### PDF Report:

- `DakshSCRA/reports/html/report.pdf`

###### RAW TEXT Based Reports:

- Areas of Interest - Identified Patterns : `DakshSCRA/reports/text/areas_of_interest.txt`
- Areas of Interest - Project Files: `DakshSCRA/reports/text/filepaths_aoi.txt`
- Identified Project Files: `DakshSCRA/runtime/filepaths.txt`

### Reconnaissance (Recon) Report

- Reconnaissance Summary: `/reports/text/recon.txt`

📝 Note: Currently, the reconnaissance report is created in a text format. However, in upcoming releases, the plan is to incorporate it into the vulnerability scanning report, which will be available in both HTML and PDF formats.

### Code Review Effort Estimation Report

- Effort estimation report: `/reports/html/estimation.html`

📝 Note: At present, the effort estimation for the source code review is in its early stages. It is considered experimental and will be developed and refined through several iterations. Improvements will be made over multiple releases, as the formula and the concept are new and require time to be honed to achieve accuracy or reasonable estimation.

✨ Currently, the report is generated in HTML format. However, in future releases, there are plans to also provide it in PDF format.

## Example Reports

| Supported language | Sample App Type | Affected File | Status     | Report                                                                  |
| ------------------ | --------------- | ------------- | ---------- | ----------------------------------------------------------------------- |
| Python             | Flask App       | `app.py`      | vulnerable | [view](sample/sample_output_documents/vulnerable-python-app-report.pdf) |
| Javascript         | Node.js App     | `app.js`      | vulnerable | [view](sample/sample_output_documents/vulnerable-js-app-report.pdf)     |
| PHP                | PHP Website     | `index.php`   | vulnerable | [view]()                                                                |

## 📧 Contact Information

**Author:** Debasis Mohanty

- Mail: [Debasis Mohanty ](mailto:d3basis.m0hanty@gmail.com)
- Twitter: [@coffeensecurity](https://x.com/coffeensecurity)
- Website: [coffeeandsecurity](www.coffeeandsecurity.com)

## 🔑 License

This Tool comes with [GNU GENERAL PUBLIC LICENSE](LICENSE).
