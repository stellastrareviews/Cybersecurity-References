# Cybersecurity References 🛡️🔒

Welcome to my personal collection of cybersecurity resources, tools, and references.

## 📁 Directory Structure

### [Automation](./Automation-Scripts)

Personal automation scripts are kept here.

[`firewall_rules.py`](./Automation-Scripts/firewall_rules.py): takes in the URL of a CSV file to block known problematic IP addresses. 

> The default URL downloads the "Botnet C2 Indicators of Compromise (IOCs)" from FEODOtracker, which contains "information on tracked botnet c2s but also IP addresses that were acting as a botnet C2 within the **past 30 days**."

[`extract_video_audio.py`](./Automation-Scripts/extract_video_audio.py): CLI tool that creates an MP3 audio file from a MP4 file, or files in a directory.

[`Reset-DockerWslIntergration.ps1`](./Automation-Scripts/Reset-DockerWslIntegration.ps1): PowerShell script that stops Docker Desktop, Stops WSL, and Unregisters the Docker Destop data.

### [Documents](./Documents)

This directory contains a collection of documents that can be useful for cybersecurity professionals. It includes a variety of documents that can be useful for different purposes.
- [Compliance](./Documents/Compliance)
    - [Security and Privacy Controls for Information Systems and Organizations](./Documents/Compliance//800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf "PDF")
        - [Spreadsheet](./Documents/Compliance/800-53r5/sp800-53r5-control-catalog.xlsx "XLSX")
    - [Implementing the Health Insurance Portability and Accountability Act (HIPAA) Security Rule](./Documents/Compliance/800-66r2/NIST.SP.800-66r2.pdf "PDF")
    - [Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](./Documents/Compliance/800-171/NIST.SP.800-171r2.pdf "PDF")
        - [Spreadsheet](./Documents/Compliance/800-171/sp800-171r2-security-reqs.xlsx "XLSX")
    - [Framework for Improving Critical Infrastructure Cybersecurity](./Documents/Compliance/NIST.CSWP.04162018.pdf "PDF")
- [Continuous Learning](./Documents/Continuous-Learning/)
    - [Generative AI](./Documents/Continuous-Learning/Generative-AI/)
    - [Privacy](./Documents/Continuous-Learning/Privacy/ "Learn about digital privacy.")
    - [US State Surveillance & Psychological Operations](./Documents/Continuous-Learning/US-State_Surveillance-Psyops/ "Learn about state-sanctioned psyops in the US and abroad.")
- [Starter Penetration Testing Resources by TCM Security](./Documents/Pentest_Resources-TCM_Security/ "Resources for pentesters in the making.")
- [Sample Datasets](./Documents/Sample_Datasets/ "A collection of datasets to practice working on.")

### [References](./References)

This directory contains various files, notably [Maderas' list of necessary cybersecurity skills](./References/Get_Started-MaderasSecurityArsenal.md "Maderas Security Arsenal") for learners. It also has a few [text processing](./References/text-processing/ "Directory") reference docs, and a list of [search engines for pentesters](./References/Search_Engines_for_Pentesters.jpg "Search Engines for Pentesters").

### [UsefulRepositories](./UsefulRepositories)

This is a meta-directory with links to useful cybersecurity-related GitHub repositories. You'll find offensive, defensive, and multi-purpose tools.

Please see the [README](./UsefulRepositories/README.md).

### [Web-Applications](./Web-Applications)

Here you'll find documents for common web application vulnerabilities, like those of the OWASP Top Ten. Each document is different, but all of them contain code examples, injection payloads, that could theoretically be used in the wild. [XSS](./Web-Applications/XSS.md), [SSRF], and [CORS](./Web-Applications/CORS.md) are just a few examples. The [WebApp Exploit Checklist](./Web-Applications/WebApp-ExploitsChecklist.pdf) is a great visual reference.

## How to Contribute
This project could be way better than it is, we both know that.

Please consider contributing your own knowledge files, automation scripts, add to the [Useful Repositories README](./Useful-Repositories/README.md), and see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## 📜 License

Distributed under the GNU AGPL-3.0 License. See [LICENSE](./LICENSE) for more information.
