# ggim - Git Graph Improved
[![](https://img.shields.io/badge/code%20style-black-000000)](https%3A%2F%2Fgithub.com%2Fpsf%2Fblack)

I could not find a tool which prints me a git log graph on the console that satisfies my needs, i. e.
- shows the first parent history of a specific commit all in one layer (up until the branching point)
- represents the parent order (first parent, second parent, …) graphically and correctly
- draws different branches in different colors
- orders commits strictly chronological
- takes `git log` arguments like e. g. `--reflog`
- can export the graph (including commit info) as e. g. ascii, svg or html
- is able to show commits with more than two parents

This is my attemt at such a tool.
