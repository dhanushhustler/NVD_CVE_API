# CVE Binary Tool quick start / README

[![Build Status](https://github.com/intel/cve-bin-tool/actions/workflows/cve_bin_tool_action.yml/badge.svg?branch=main&event=push)](https://github.com/intel/cve-bin-tool/actions)
[![codecov](https://codecov.io/gh/intel/cve-bin-tool/branch/main/graph/badge.svg)](https://codecov.io/gh/intel/cve-bin-tool)
[![Gitter](https://badges.gitter.im/cve-bin-tool/community.svg)](https://gitter.im/cve-bin-tool/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![On ReadTheDocs](https://readthedocs.org/projects/cve-bin-tool/badge/?version=latest&style=flat)](https://cve-bin-tool.readthedocs.io/en/latest/)
[![On PyPI](https://img.shields.io/pypi/v/cve-bin-tool)](https://pypi.org/project/cve-bin-tool/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5380/badge)](https://bestpractices.coreinfrastructure.org/projects/5380)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/intel/cve-bin-tool/badge)](https://securityscorecards.dev/viewer/?uri=github.com/intel/cve-bin-tool)

The CVE Binary Tool is a free, open source tool to help you find known vulnerabilities in software, using data from the [National Vulnerability Database](https://nvd.nist.gov/) (NVD) list of [Common Vulnerabilities and Exposures](<https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures#:~:text=Common%20Vulnerabilities%20and%20Exposures%20(CVE)%20is%20a%20dictionary%20of%20common,publicly%20known%20information%20security%20vulnerabilities.>) (CVEs) as well as known vulnerability data from [Redhat](https://access.redhat.com/hydra/rest/securitydata), [Open Source Vulnerability Database (OSV)](https://osv.dev/), [Gitlab Advisory Database (GAD)](https://advisories.gitlab.com/about/index.html), and [Curl](https://curl.se/docs/vuln.json).

CVE Binary Tool uses the NVD API but is not endorsed or certified by the NVD.

The tool has two main modes of operation:

1. A binary scanner which helps you determine which packages may have been included as part of a piece of software. There are <!-- NUMBER OF CHECKERS START-->360<!--NUMBER OF CHECKERS END--> checkers.  Our initial focus was on common, vulnerable open source components such as openssl, libpng, libxml2 and expat.

2. Tools for scanning known component lists in various formats, including .csv, several linux distribution package lists, language specific package scanners and several Software Bill of Materials (SBOM) formats.  

It is intended to be used as part of your continuous integration system to enable regular vulnerability scanning and give you early warning of known issues in your supply chain.  It can also be used to auto-detect components and create SBOMs.

What CVE Binary Tool does when it runs:

![Diagram of cve-bin-tool's workflow, described in text with more detail below.](https://raw.githubusercontent.com/intel/cve-bin-tool/main/doc/images/cve-bin-tool-workflow-800px.png)

1. Download CVE Data (from NVD, Redhat, OSV, Gitlab, and Curl).
   - This happens once per day by default, not every time a scan is run.
   - On first run, downloading all data can take some time.
2. Create/read a component list. There are two modes of operation:
   1. Creates a component list (including versions) using a combination of binary checkers and language component lists (such as python's requirements.txt).
   2. Read SBOM (use an existing component list in a standardized Software Bill of Materials format.)
3. Create CVE List
   - This looks up all components found or read from an existing bill of materials and reports back any known issues associated with them
4. Include triage/additional data
   - There are several options for adding triage/notes, information from previous reports to track vulnerability change over time, or known fix data
5. Generate report in one or more formats (console, json, csv, html, pdf)

## Installing CVE Binary Tool

CVE Binary Tool can be installed using pip:

```console
pip install cve-bin-tool
```

If you want to try the latest code from
[the cve-bin-tool github](https://github.com/intel/cve-bin-tool) or do development, you can also `pip install --user -e .` to install a local copy from a directory.  The [Contributor Documentation](https://github.com/intel/cve-bin-tool/blob/main/CONTRIBUTING.md) covers how to set up for local development in more detail.

Pip will install the python requirements for you, but for some types of extraction we use system libraries. If you have difficulties extracting files, you may want to look at our [additional Requirements lists for Linux and Windows](#additional-requirements).

On first usage (and by default, once per day) The tool will download vulnerability data from [a set of known vulnerability data sources](https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#data-sources).  Due to reliability issues with NVD, as of release 3.3 we will be using our own NVD mirror at [https://cveb.in/](https://cveb.in/) by default rather than contacting NVD directly.  If you wish to get data directly from the NVD servers you must [provide your own NVD_API_KEY](https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--nvd-api-key-nvd_api_key) to use their API.

## Most popular usage options

### Finding known vulnerabilities using the binary scanner

To run the binary scanner on a directory or file:

```bash
cve-bin-tool <directory/file>
```

> **Note**: That this option will also use any [language specific checkers](#language-specific-checkers) to find known vulnerabilities in components.

By default, the tool assumes you are attempting to scan a whole directory, but if you provide it with a single .csv or .json file that lists dependencies it will treat it as a bill of materials.  You can also specify bill of materials files directly using [the `--input-file` option](https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-i-input_file---input-file-input_file) or scan SBOMs with the instructions below.

### Scanning an SBOM file for known vulnerabilities

To scan a software bill of materials file (SBOM):

```bash
cve-bin-tool --sbom <sbom_filetype> --sbom-file <sbom_filename>
```

Valid SBOM types are [SPDX](https://spdx.dev/specifications/),
[CycloneDX](https://cyclonedx.org/specification/overview/), and [SWID](https://csrc.nist.gov/projects/software-identification-swid/guidelines).
Scanning of product names within an SBOM file is case insensitive.

The [SBOM scanning how-to guide](https://github.com/intel/cve-bin-tool/blob/main/doc/how_to_guides/sbom.md) provides additional SBOM scanning examples.

### Generating an SBOM

As well as scanning SBOMs, CVE Binary Tool can be used to generate an SBOM from a scan as follows:

```bash
cve-bin-tool  --sbom-type <sbom_type> --sbom-format <sbom-format> --sbom-output <sbom_filename> <other scan options as required>
```

Valid SBOM types are [SPDX](https://spdx.dev/specifications/) and [CycloneDX](https://cyclonedx.org/specification/overview/).

The generated SBOM will include product name, version and supplier (where available). License information is not provided.

The [SBOM generation how-to guide](https://github.com/intel/cve-bin-tool/blob/main/doc/how_to_guides/sbom_generation.md) provides additional SBOM generation examples.

### Triaging vulnerabilities

The `--triage-input-file` option can be used to add extra triage data like remarks, comments etc. while scanning a directory so that output will reflect this triage data and you can save time of re-triaging (Usage: `cve-bin-tool --triage-input-file test.vex /path/to/scan`).
The supported format is the [CycloneDX](https://cyclonedx.org/capabilities/vex/) VEX format which can be generated using the `--vex` option.

Typical usage:

1. Generate triage file using `cve-bin-tool /path/to/scan --vex triage.vex`
2. Edit triage.vex with your favourite text editor to provide triage information on the vulnerabilities listed.
3. Use this triage file for future scans as follows: `cve-bin-tool /path/to/scan --triage-input-file triage.vex`

It should be possible to share triage data across different runs of cve-bin-tool or with other tools that support the CycloneDX VEX format.  This would be particularly useful for teams that scan related products or containers, teams that need to use multiple tools for compliance reasons, companies that have a central security policy group that provides guidance on vulnerability triage, and more.

## Output Options

The CVE Binary Tool provides console-based output by default. If you wish to provide another format, you can specify this and a filename on the command line using `--format`. The valid formats are CSV, JSON, console, HTML and PDF. The output filename can be specified using the `--output-file` flag.

You can also specify multiple output formats by using comma (',') as separator:

```bash
cve-bin-tool file -f csv,json,html -o report
```

Note: You must not use spaces between the commas (',') and the output formats.

The reported vulnerabilities can additionally be reported in the
Vulnerability Exchange (VEX) format by specifying `--vex` command line option.
The generated VEX file can then be used as a `--triage-input-file` to support
a triage process.

If you wish to use PDF support, you will need to install the `reportlab`
library separately.

If you intend to use PDF support when you install cve-bin-tool you can specify it and report lab will be installed as part of the cve-bin-tool install:

```console
pip install cve-bin-tool[PDF]
```

If you've already installed cve-bin-tool you can add reportlab after the fact
using pip:

```console
pip install --upgrade reportlab
```

## Configuration

You can use `--config` option to provide configuration file for the tool. You can still override options specified in config file with command line arguments. See our sample config files in the
[test/config](https://github.com/intel/cve-bin-tool/blob/main/test/config/)

## Full option list

Usage:
`cve-bin-tool <directory/file to scan>`

<pre>
options:
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-h---help">-h, --help</a>            show this help message and exit
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-e-exclude---exclude-exclude">-e EXCLUDE, --exclude</a> EXCLUDE
                        Comma separated Exclude directory path
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-v---version">-V, --version</a>         show program's version number and exit
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--disable-version-check">--disable-version-check</a>
                        skips checking for a new version
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--disable-validation-check">--disable-validation-check</a>
                        skips checking xml files against schema
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--offline">--offline</a>             operate in offline mode
  --detailed            add CVE description in csv or json report (no effect on console, html or pdf)

CVE Data Download:
  Arguments related to data sources and Cache Configuration

  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-n-json-nvdjson-mirrorapiapi2---nvd-json-nvdjson-mirrorapiapi2">-n {api,api2,json,json-mirror,json-nvd}, --nvd {api,api2,json,json-mirror,json-nvd}</a>
                        choose method for getting CVE lists from NVD
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-u-nowdailyneverlatest---update-nowdailyneverlatest">-u {now,daily,never,latest}, --update {now,daily,never,latest}</a>
                        update schedule for data sources and exploits database (default: daily)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--nvd-api-key-nvd_api_key">--nvd-api-key NVD_API_KEY</a>
                        specify NVD API key (used to improve NVD rate limit)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-d-nvdosvgadcurl-nvdosvgadcurl----disable-data-source-nvdosvgadcurl-nvdosvgadcurl-">-d DISABLE_DATA_SOURCE, --disable-data-source DISABLE_DATA_SOURCE</a>
                        comma-separated list of data sources (CURL, EPSS, GAD, NVD, OSV, REDHAT, RSD) to disable (default: NONE) 

  --use-mirror USE_MIRROR
                        use an mirror to update the database

Input:
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#directory-positional-argument">directory</a>             directory to scan
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-i-input_file---input-file-input_file">-i INPUT_FILE, --input-file INPUT_FILE</a>
                        provide input filename
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--triage-input-file-input_file">--triage-input-file TRIAGE_INPUT_FILE</a>
                        provide input filename for triage data
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-c-config---config-config">-C CONFIG, --config CONFIG</a>
                        provide config file
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-l-package_list---package-list-package_list">-L PACKAGE_LIST, --package-list PACKAGE_LIST</a>
                        provide package list
  --sbom {spdx,cyclonedx,swid}
                        specify type of software bill of materials (sbom) (default: spdx)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--sbom-file-sbom_file">--sbom-file SBOM_FILE</a>
                        provide sbom filename

Output:
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#quiet-mode">-q, --quiet</a>           suppress output
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#logging-modes">-l {debug,info,warning,error,critical}, --log {debug,info,warning,error,critical}</a>
                        log level (default: info)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-o-output_file---output-file-output_file">-o OUTPUT_FILE, --output-file OUTPUT_FILE</a>
                        provide output filename (default: output to stdout)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--html-theme-html_theme">--html-theme HTML_THEME</a>
                        provide custom theme directory for HTML Report
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-f-csvjsonconsolehtml---format-csvjsonconsolehtml">-f {csv,json,console,html,pdf}, --format {csv,json,console,html,pdf}</a>
                        update output format (default: console)
                        specify multiple output formats by using comma (',') as a separator
                        note: don't use spaces between comma (',') and the output formats.
  --generate-config {yaml,toml,yaml,toml,toml,yaml}
                        generate config file for cve bin tool in toml and yaml formats.
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-c-cvss---cvss-cvss">-c CVSS, --cvss CVSS</a>  minimum CVSS score (as integer in range 0 to 10) to report (default: 0)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-s-lowmediumhighcritical---severity-lowmediumhighcritical">-S {low,medium,high,critical}, --severity {low,medium,high,critical}</a>
                        minimum CVE severity to report (default: low)
  --metrics             
                        check for metrics (e.g., EPSS) from found cves
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--epss-percentile">--epss-percentile EPSS_PERCENTILE</a>
                        minimum epss percentile of CVE range between 0 to 100 to report
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--epss-probability">--epss-probability EPSS_PROBABILITY</a>
                        minimum epss probability of CVE range between 0 to 100 to report
  --no-0-cve-report     only produce report when CVEs are found
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-a-distro_name-distro_version_name---available-fix-distro_name-distro_version_name">-A [<distro_name>-<distro_version_name>], --available-fix [<distro_name>-<distro_version_name>]</a>
                        Lists available fixes of the package from Linux distribution
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-b-distro_name-distro_version_name---backport-fix-distro_name-distro_version_name">-b [<distro_name>-<distro_version_name>], --backport-fix [<distro_name>-<distro_version_name>]</a>
                        Lists backported fixes if available from Linux distribution
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--affected-versions">--affected-versions</a>   Lists versions of product affected by a given CVE (to facilitate upgrades)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--vex-vex_file">--vex VEX</a>             Provide vulnerability exchange (vex) filename
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--sbom-output-sbom_output">--sbom-output SBOM_OUTPUT</a>
                        provide software bill of materials (sbom) filename to generate
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--sbom-type">--sbom-type {spdx,cyclonedx}</a>
                        specify type of software bill of materials (sbom) to generate (default: spdx)
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--sbom-format">--sbom-format {tag,json,yaml}</a>
                        specify format of software bill of materials (sbom) to generate (default: tag)

Merge Report:
  Arguments related to Intermediate and Merged Reports

  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-a-intermediate_path---append-intermediate_path">-a [APPEND], --append [APPEND]</a>
                        save output as intermediate report in json format
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-t-tag---tag-tag">-t TAG, --tag TAG</a>     add a unique tag to differentiate between multiple intermediate reports
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-m-intermediate_reports---merge-intermediate_reports">-m MERGE, --merge MERGE</a>
                        comma separated intermediate reports path for merging
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-f-tags---filter-tags">-F FILTER, --filter FILTER</a>
                        comma separated tag string for filtering intermediate reports

Checkers:
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-s-skips---skips-skips">-s SKIPS, --skips SKIPS</a>
                        comma-separated list of checkers to disable
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-r-checkers---runs-checkers">-r RUNS, --runs RUNS</a>  comma-separated list of checkers to enable

Database Management:
  --import-json IMPORT_JSON
                        import database from json files chopped by years
  --ignore-sig          do not verify PGP signature while importing json data
  --log-signature-error
                        when the signature doesn't match log the error only instead of halting (UNSAFE)
  --verify PGP_PUBKEY_PATH
                        verify PGP sign while importing json files
  --export-json EXPORT_JSON
                        export database as json files chopped by years
  --pgp-sign PGP_PRIVATE_KEY_PATH
                        sign exported json files with PGP
  --passphrase PASSPHRASE
                        required passphrase for signing with PGP
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--export-export">--export EXPORT</a>       export database filename
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--import-import">--import IMPORT</a>       import database filename

Exploits:
  --exploits            check for exploits from found cves

Deprecated:
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#-x---extract">-x, --extract</a>         autoextract compressed files
  <a href="https://github.com/intel/cve-bin-tool/blob/main/doc/MANUAL.md#--report">--report</a>              Produces a report even if there are no CVE for the respective output format
</pre>

