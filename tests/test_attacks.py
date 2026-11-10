from __future__ import annotations

from judge_robustness.attacks import FAMILIES
from judge_robustness.formats import decoy, is_correct
from judge_robustness.tasks import DATASET_FORMATS, load_tasks


def test_generators_are_deterministic(tasks):
    reloaded = {d: load_tasks(d, 20, seed=7) for d in DATASET_FORMATS}
    for dataset, items in tasks.items():
        for a, b in zip(items, reloaded[dataset], strict=True):
            for gen in FAMILIES.values():
                assert gen(a) == gen(b)


def test_variant_ids_unique_and_stable_per_dataset(tasks):
    for items in tasks.values():
        for family, gen in FAMILIES.items():
            ids = [v for v, _ in gen(items[0])]
            assert len(ids) == len(set(ids)), family
            assert 7 <= len(ids) <= 12, family
            for task in items[1:]:
                assert [v for v, _ in gen(task)] == ids


def test_oracle_accepts_gold_and_rejects_decoy(tasks):
    for items in tasks.values():
        for task in items:
            assert is_correct(task, task.gold), task.task_id
            # Contradictory logic premises entail everything, so no decoy exists there.
            if not is_correct(task, "(P ∧ ¬P)"):
                assert not is_correct(task, decoy(task)), task.task_id


def test_payload_attacks_are_wrong(tasks):
    for items in tasks.values():
        for task in items:
            for family in ("verdict_tokens", "forged_delimiters", "hedged", "empty_filler"):
                for variant, answer in FAMILIES[family](task):
                    assert not is_correct(task, answer), (task.task_id, family, variant)
