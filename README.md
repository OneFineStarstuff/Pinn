# Enterprise AI Agent Interoperability Protocol (EAIP)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

The Enterprise AI Agent Interoperability Protocol (EAIP) defines a standard for the secure, scalable, and efficient interaction between AI agents in an enterprise environment. This repository contains the formal technical specification (version 3.4.1) and a collection of experimental AGI blueprints and reinforcement learning simulations that demonstrate various facets of agentic behavior, from self-reflection to complex reasoning.

### Technical Specification (EAIP v3.4.1)

The core protocol focuses on three primary pillars:

1.  **Transport Layer (gRPC):** All inter-service communication is mandated to use gRPC, ensuring binary efficiency and native support for bidirectional streaming.
2.  **Identity & Security (SPIFFE/SPIRE):** Employs a zero-trust architecture using SPIFFE Verifiable Identity Documents (SVIDs) for mutual TLS authentication.
3.  **State Management (Recursive Context Envelope - RCE):** A formalized structure for propagating state and context across distributed agentic pipelines.

For full details, see [eaip_specification.xml](./eaip_specification.xml) and the accompanying schema [eaip-spec-v3.xsd](./eaip-spec-v3.xsd).

## AGI Experiments & Blueprints

This repository includes several Jupyter notebooks demonstrating advanced AI and AGI concepts:

*   **Unified AGI Agent Blueprint:** A comprehensive architectural template for multi-modal, self-improving agents.
*   **MCTS Example (Tic-Tac-Toe):** Implementation of Monte Carlo Tree Search for strategic decision-making.
*   **Self-Reflective CartPole:** Experiments in reinforcement learning where agents monitor and adjust their own reward functions.
*   **Multi-hop Reasoner:** Scripts for training and evaluating agents on tasks requiring several steps of logical inference.
*   **Differentiable Neural Computer (DNC) Copy Task:** Demonstrating external memory usage in neural architectures.
*   **MAML (Model-Agnostic Meta-Learning):** Implementation of meta-learning for fast adaptation to new tasks.

## Getting Started

### Prerequisites

*   Python 3.8+
*   Jupyter Notebook or JupyterLab
*   gRPC and Protocol Buffers (for protocol implementation)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/onefinestarstuff/eaip.git
    cd eaip
    ```
2.  Install dependencies (if applicable):
    ```bash
    pip install -r requirements.txt # Note: Use standard AGI/RL libraries like torch, numpy, etc.
    ```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Citation

If you use EAIP in your research, please cite it as follows:

```bibtex
@software{eaip_2025,
  author = {One Fine Starstuff},
  title = {Enterprise AI Agent Interoperability Protocol (EAIP)},
  version = {3.4.1},
  year = {2025}
}
```
