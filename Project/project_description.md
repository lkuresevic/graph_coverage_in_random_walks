# Description
This research-driven internship project explores the emerging field of AI coding agents—automated systems powered by large language models (LLMs) that can independently interact with integrated development environments (IDEs) to tackle complex programming tasks. Although significant progress has been made in developing coding agents, current solutions are typically focused on task completion rather than efficiency. Each tool or method these agents employ can vary greatly in terms of time complexity, resource consumption, and financial cost when deployed on a server. However, there has been little research on creating coding agents that not only complete tasks accurately but also optimize these costs, reducing unnecessary resource expenditure.


This project aims to bridge that gap by developing a framework for creating cost-efficient AI coding agents. If successful, this research could lay the foundation for building smarter, more economical coding agents, advancing the field and potentially leading to a high-quality publication.


More formally:


Imagine a set of tools or functions f1, f2, ... fN , each with an associated cost c1, c2, ... cN. These tools and their costs may vary and can be dynamically defined based on the specific task at hand. The objective is to develop a coding agent that collaborates with a large language model (LLM), selectively calling these tools to accomplish a given task.
Each time the agent invokes a tool f_i, it incurs a cost c_i. At the end of the task, if the agent has called f1 a total of n1 times, f2 a total of n2 times, and so on, the total cost incurred by the agent is n1 * c1 + n2 * c2 +…+nN*cN.
The goal of this project is to develop a coding agent that optimizes this process, minimizing the total cost required to complete the task while ensuring task success.


Research Significance and Impact:


Success in this project has strong potential for a high-quality research publication, as this problem has not yet been thoroughly explored. Furthermore, cost-optimized coding agents have valuable real-world applications, particularly in production environments where resource efficiency is critical.
