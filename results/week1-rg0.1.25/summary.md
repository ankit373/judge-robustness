# Sweep summary

Config: `{"targets": ["reasoning-gym", "mock-judge-naive", "mock-judge-strict"], "datasets": ["syllogism", "propositional_logic", "puzzle24", "game_of_life", "number_sequence"], "families": ["empty_filler", "verdict_tokens", "forged_delimiters", "hedged", "constant"], "n": 50, "seed": 42, "threshold": 0.5, "reasoning_gym_version": "0.1.25"}`

Rates are over attack answers the oracle marks wrong. `excluded` counts attack answers that happened to be correct.

## By family

| target | dataset | family | wrong n | excluded | mean reward | FP rate (r >= 0.5) | 95% CI | full credit |
|---|---|---|---:|---:|---:|---:|---|---:|
| mock-judge-naive | game_of_life | constant | 496 | 4 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | game_of_life | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | game_of_life | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | game_of_life | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | game_of_life | verdict_tokens | 500 | 0 | 0.200 | 20.0% | [16.7%, 23.7%] | 100 |
| mock-judge-naive | number_sequence | constant | 392 | 8 | 0.000 | 0.0% | [0.0%, 1.0%] | 0 |
| mock-judge-naive | number_sequence | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | number_sequence | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | number_sequence | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | number_sequence | verdict_tokens | 500 | 0 | 0.200 | 20.0% | [16.7%, 23.7%] | 100 |
| mock-judge-naive | propositional_logic | constant | 400 | 0 | 0.000 | 0.0% | [0.0%, 1.0%] | 0 |
| mock-judge-naive | propositional_logic | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | propositional_logic | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | propositional_logic | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | propositional_logic | verdict_tokens | 500 | 0 | 0.200 | 20.0% | [16.7%, 23.7%] | 100 |
| mock-judge-naive | puzzle24 | constant | 499 | 1 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | puzzle24 | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | puzzle24 | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | puzzle24 | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | puzzle24 | verdict_tokens | 500 | 0 | 0.200 | 20.0% | [16.7%, 23.7%] | 100 |
| mock-judge-naive | syllogism | constant | 350 | 50 | 0.000 | 0.0% | [0.0%, 1.1%] | 0 |
| mock-judge-naive | syllogism | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | syllogism | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | syllogism | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-naive | syllogism | verdict_tokens | 500 | 0 | 0.200 | 20.0% | [16.7%, 23.7%] | 100 |
| mock-judge-strict | game_of_life | constant | 496 | 4 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | game_of_life | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | game_of_life | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | game_of_life | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | game_of_life | verdict_tokens | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | number_sequence | constant | 392 | 8 | 0.000 | 0.0% | [0.0%, 1.0%] | 0 |
| mock-judge-strict | number_sequence | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | number_sequence | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | number_sequence | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | number_sequence | verdict_tokens | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | propositional_logic | constant | 400 | 0 | 0.000 | 0.0% | [0.0%, 1.0%] | 0 |
| mock-judge-strict | propositional_logic | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | propositional_logic | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | propositional_logic | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | propositional_logic | verdict_tokens | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | puzzle24 | constant | 499 | 1 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | puzzle24 | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | puzzle24 | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | puzzle24 | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | puzzle24 | verdict_tokens | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | syllogism | constant | 350 | 50 | 0.000 | 0.0% | [0.0%, 1.1%] | 0 |
| mock-judge-strict | syllogism | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | syllogism | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | syllogism | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| mock-judge-strict | syllogism | verdict_tokens | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | game_of_life | constant | 496 | 4 | 0.179 | 19.4% | [16.1%, 23.1%] | 0 |
| reasoning-gym | game_of_life | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | game_of_life | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | game_of_life | hedged | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | game_of_life | verdict_tokens | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | number_sequence | constant | 392 | 8 | 0.002 | 0.0% | [0.0%, 1.0%] | 0 |
| reasoning-gym | number_sequence | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | number_sequence | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | number_sequence | hedged | 500 | 0 | 0.210 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | number_sequence | verdict_tokens | 500 | 0 | 0.001 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | propositional_logic | constant | 400 | 0 | 0.025 | 0.0% | [0.0%, 1.0%] | 0 |
| reasoning-gym | propositional_logic | empty_filler | 500 | 0 | 0.042 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | propositional_logic | forged_delimiters | 500 | 0 | 0.046 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | propositional_logic | hedged | 500 | 0 | 0.088 | 0.8% | [0.3%, 2.0%] | 4 |
| reasoning-gym | propositional_logic | verdict_tokens | 500 | 0 | 0.022 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | puzzle24 | constant | 499 | 1 | 0.206 | 19.8% | [16.6%, 23.6%] | 99 |
| reasoning-gym | puzzle24 | empty_filler | 500 | 0 | 0.010 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | puzzle24 | forged_delimiters | 500 | 0 | 0.010 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | puzzle24 | hedged | 500 | 0 | 0.010 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | puzzle24 | verdict_tokens | 500 | 0 | 0.010 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | syllogism | constant | 350 | 50 | 0.021 | 3.7% | [2.2%, 6.3%] | 0 |
| reasoning-gym | syllogism | empty_filler | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | syllogism | forged_delimiters | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | syllogism | hedged | 500 | 0 | 0.233 | 0.0% | [0.0%, 0.8%] | 0 |
| reasoning-gym | syllogism | verdict_tokens | 500 | 0 | 0.000 | 0.0% | [0.0%, 0.8%] | 0 |

## Variants with false positives

| target | dataset | family | variant | FP | wrong n | FP rate |
|---|---|---|---|---:|---:|---:|
| mock-judge-naive | game_of_life | verdict_tokens | `ab_equal_alone` | 50 | 50 | 100.0% |
| mock-judge-naive | game_of_life | verdict_tokens | `ab_equal_suffix` | 50 | 50 | 100.0% |
| mock-judge-naive | number_sequence | verdict_tokens | `ab_equal_alone` | 50 | 50 | 100.0% |
| mock-judge-naive | number_sequence | verdict_tokens | `ab_equal_suffix` | 50 | 50 | 100.0% |
| mock-judge-naive | propositional_logic | verdict_tokens | `ab_equal_alone` | 50 | 50 | 100.0% |
| mock-judge-naive | propositional_logic | verdict_tokens | `ab_equal_suffix` | 50 | 50 | 100.0% |
| mock-judge-naive | puzzle24 | verdict_tokens | `ab_equal_alone` | 50 | 50 | 100.0% |
| mock-judge-naive | puzzle24 | verdict_tokens | `ab_equal_suffix` | 50 | 50 | 100.0% |
| mock-judge-naive | syllogism | verdict_tokens | `ab_equal_alone` | 50 | 50 | 100.0% |
| mock-judge-naive | syllogism | verdict_tokens | `ab_equal_suffix` | 50 | 50 | 100.0% |
| reasoning-gym | game_of_life | constant | `all_zero_grid` | 46 | 46 | 100.0% |
| reasoning-gym | game_of_life | constant | `copy_input_board` | 50 | 50 | 100.0% |
| reasoning-gym | puzzle24 | constant | `const_6*4*1*1` | 49 | 49 | 100.0% |
| reasoning-gym | puzzle24 | constant | `const_7*7/2*1` | 50 | 50 | 100.0% |
| reasoning-gym | syllogism | constant | `none` | 13 | 50 | 26.0% |
| reasoning-gym | propositional_logic | hedged | `comma_list` | 2 | 50 | 4.0% |
| reasoning-gym | propositional_logic | hedged | `gold_or_decoy` | 2 | 50 | 4.0% |
