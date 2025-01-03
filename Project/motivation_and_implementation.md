# Motivation

I am currently working on a project that addresses a similar problem in a different discipline. Specifically, I am exploring *reinforcement learning in logic synthesis* as part of a seminar course on "Algorithms in Hardware Design."  
In essence, an RL agent is trained to interact with a logic synthesis tool (Berkeley's ABC) to perform optimization operations (e.g., rewrite, refactor, renode, balance) with the goal of minimizing the number of nodes in the and-inverter graph representing a logic circuit's Boolean function. 

What makes these problems similar, I believe, is that the order in which these operations are performed matters—though in different ways. In logic synthesis, the sequence of optimizations directly influences the quality of results (QoR). In the case of coding agents, the order (and selection) of actions impacts the overall cost of the process.  

One significant drawback of using RL models for logic synthesis in industrial hardware design contexts is their runtime, which often vastly exceeds the runtime of commonly used heuristics, despite only marginal improvements in QoR. While recent research in RL for logic synthesis has sought to address this issue, heuristic solutions still outperform these approaches.

Many algorithms in electronic design automation rely on the order in which steps are executed. Since no deterministic solutions exist for these ordering problems, these algorithms are generally heuristic in nature. While logic synthesis has seen some exploration with reinforcement learning, I am considering researching RL approaches in other areas of EDA in the future, potentially as part of my master’s or doctoral thesis. Within my research considerations, I am also interested in working on compiler heuristics and code-generation (possibly also through applying ML methodologies) in the future. Even if this project does not incorporate RL, I am eager to explore alternative approaches to "ordering" problems and develop my research skillset in preparation for higher-level studies and a career in research.

# Implementation

A good starting point might involve evaluating the costs associated with current agent strategies. For instance, we could compare the costs produced by agents employing the following strategies:

* **ReAct:** [Yao et. al.](https://arxiv.org/pdf/2210.03629)  
* **Tool-Planning:** [Wang et. al.](https://arxiv.org/pdf/2305.04091)  
* **Rule-Based Tool Usage:** [Zhang et. al.](https://arxiv.org/pdf/2401.07339)  (repo-level coding agent)

The most promising strategy could then be redesigned with cost efficiency in mind.

Alternatively, the problem might be formulated as a **Markov decision process**. It is possible that a fixed strategy is not optimal, as is the case in logic synthesis. An RL agent might reduce costs by avoiding unnecessary function calls. Using a state representation provided to it, the agent could decide which of the N functions to call, receiving rewards for solving the task with minimal cost.

This approach would give the agent two objectives: solve the task and do so as efficiently as possible. However, since episodes where the agent fails to solve the task incur significant costs, cost minimization alone may suffice as the reward basis.

The most challenging aspect would be designing a useful state representation. However, the planning stages of existing strategies might serve as a good starting point.  

A crucial task in designing the RL agent would involve optimizing the methods used to extract state representations, as these methods would be called inbetween every two decisions that the agent makes. If a state representation can be designed to be both simple and inexpensive to compute, the cost savings from avoiding unnecessary function calls would be worthwhile.  

An [interesting result](https://arxiv.org/pdf/2205.07614) in RL for logic synthesis shows that a "random tensor" state representation can outperform those based on extracting graph features or statistical information from and-inverter graphs representing system logic. This suggests that a surprisingly simple and computationally cheap state representation might suffice.

Benchmarks used for evaluating performance could be repurposed for training the agent.
