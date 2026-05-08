# 🧮 Square Root Pipeline

![CI Status](https://github.com/robson-lachat/square-root/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![Linter](https://img.shields.io/badge/linter-ruff-orange.svg)
![OS](https://img.shields.io/badge/OS-WSL2--Ubuntu-linux.svg)

A mathematical processing pipeline focused on series square root calculations. This project was developed to demonstrate modern software engineering practices, Linux automation, and rigorous testing.

## 🎯 Project Goal
To provide robust logic for calculating square roots in series, ensuring data integrity and proper handling of mathematical exceptions (such as negative numbers).

## 🚀 Technologies & Tools
- **Language:** Python 3.14+
- **Package Manager:** [Poetry](https://python-poetry.org/) (Isolated environments and dependency management)
- **QA & Style:** [Ruff](https://github.com/astral-sh/ruff) (Ultra-fast linter and formatter)
- **Testing:** [Pytest](https://docs.pytest.org/) (TDD and edge-case coverage)
- **Automation:** GNU Make (Standardization of terminal commands)

## 📦 Environment Setup

This project is optimized for **Linux/WSL2** environments.

1.  **Install Poetry** (if not already installed):
    ```bash
    curl -sSL [https://install.python-poetry.org](https://install.python-poetry.org) | python3 -
    ```

2.  **Install project dependencies**:
    ```bash
    make install
    ```

## 🎮 How to Use (Makefile)

To streamline development and code reviews, a `Makefile` is provided with the following targets:

| Command | Description |
| :--- | :--- |
| `make install` | Installs dependencies via Poetry. |
| `make test` | Runs the unit test suite. |
| `make lint` | Checks for logic and style errors using Ruff. |
| `make format` | Automatically fixes code formatting (PEP 8). |
| `make check` | **The definitive command:** Runs format, lint, and test in sequence. |

## 🧪 Testing Strategy
The project follows a **Fail-Fast** philosophy. The tests cover:
- **Output Integrity:** Ensures the generated list contains the exact number of requested elements.
- **Precision:** Validates that $\sqrt{4} = 2.0$ and $\sqrt{9} = 3.0$.
- **Safety:** Ensures the system raises a `ValueError` when attempting to process negative numbers.

## 🧠 Architecture Notes (WSL/Bash)
The environment was configured respecting the Bash initialization hierarchy in Debian/Ubuntu. It utilizes the bridge between `.profile` (login shell) and `.bashrc` (interactive shell) to ensure Poetry environment variables are consistently available in the system PATH.

---
**Developer:** Robson Aguiar-Lachat