# Motivation

I am currently working on a project that solves a similiar problem in a different discipline. Namely, I am exploring *reinforcement learning in logic synthesis* as a project for a seminar course on "Algorithms in Hardware Design":
In short, an RL agent is trained to call a logic synthesis tool (Berkeley's ABC) to perform optimizing operations (rewrite, ) with the goal minimizing the number of nodes in the and-inverter graph representing a logic circuits Boolean function. What I believe makes these problems similiar, is the fact that the order in which these operations are performed matters, although in different ways. In logic synthesis, the order in which optimizations are performed influences quallity of results (QoR). Here, the order (and selection) of actions influences the cost of the process. One of the biggest drawbacks of using RL models for logic synthesis in an industrial hardware design contexts, is the fact that their runtimes last many multiples of commonly used heuristics, and the improvements in QoR. More recent papers that explored RL in logic synthesis tried to adress this, but still have not outperformed heuristic solutions.

There are a couple of algorithms in electronic design automation, whoose performance depends on the order in which steps are taken. Since there are no deterministic solutions to the ordering problems, these algorithms are heuristic in nature. Although logic synthesis is a field in which reinforcement learning has been explored to some extent, I am considering researching other RL approaches to EDA in the future, perhaps even as part of my master or doctoral thesis. Even if the project implements a solution that does not include RL, I am curious to learn about other approaches to "ordering" problems and eager to expand my research skillset in preparation for more searious research in higher levels of studies.

# Implementation

A good starting point might be the evaluation of costs of current agent strategies. For example, we could compare costs that agents produce when based on:
* **ReAct** [Yao et. al.](https://arxiv.org/pdf/2210.03629)
* **Tool-Planning** [Wang et. al.](https://arxiv.org/pdf/2305.04091)
* **Rule-Based Tool Usage** [Zhang et. al.](https://arxiv.org/pdf/2401.07339)
The most promising strategy can then be redesigned with cost efficiency in mind.

Alternatively, the problem might be addressable as a **Markov decision process**. It is possible that a fixed strategy is not the one that provides the best results, as is the case in logic synthesis. An RL agent might be able to avoid unneccessary function calls, and reduce cost in that way. The agent will use a state representation given to him to decide which of the N functions he should call, while being rewarded for solving the task with minimum cost.

This means that the agent has two objectives: solve the task and do so as efficiently as possible. However, considering the fact that episodes in which the agent does not solve the task will incurr large costs, cost minimization is enough to base rewards on.

The most challenging tasks would be finding a useful state representation, but planning stages in existing strategies might be a good starting point. 

A key task in designing an RL agent would be optimizing the methods that extract state representations, as those methods would be regularly called in between agent's decisions. If a state representation can be designed, such that its extraction cost is cheap, the cost-cutting through elimination unneccessary function calls would be justified. In RL approaches to logic synthesis, an [interesting result](https://arxiv.org/pdf/2205.07614) has shown that a "random tensor" state representation can outperform those based on extracting graph features or statistical information from and-inverter graphs representing the system logic. Perhaps the state representation can be surprisingly simple and easily computable.

