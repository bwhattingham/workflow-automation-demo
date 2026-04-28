Workflow Automation Demo
This project demonstrates a simple workflow automation pattern: scanning a directory, processing files, and generating a structured summary.

What This Demonstrates
Basic automation logic
File processing workflows
JSON output for downstream systems
Clean, readable scripting
DevOps‑style thinking

flowchart TD

    A[Input Folder] --> B[Automation Script]
    B --> C[Scan Files]
    C --> D[Count File Types]
    D --> E[Generate JSON Summary]
    E --> F[Output to Console]

    B -. triggered by .-> G[GitHub Action]
    G --> B

How to Extend This Project