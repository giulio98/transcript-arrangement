import itertools
import numpy as np


def subset_sum(weigths, target, partial=None, res=None):
    if res is None:
        res = []
    if partial is None:
        partial = {}
    s = sum(partial.values())

    # check if the partial sum is equals to target
    if s == target:
        res.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(weigths.values())):
        n = dict(itertools.islice(weigths.items(), i, len(weigths.values()), len(weigths.values())))
        remaining = dict(itertools.islice(weigths.items(), i + 1, len(weigths.values()), 1))
        new = {}
        for d in (partial, n):
            new.update(d)
        subset_sum(remaining, target, new, res)


def get_disjoint_two_set(all_combinations_):
    dis_comb = []
    for i, j in itertools.combinations(all_combinations_, 2):
        # an empty set is True, a nonempty set is False
        if not set(i).intersection(set(j)):
            dis_comb.append((i, j))
    return dis_comb


def block_score(comb, subject_grade_, i):
    weighted_vals = {
        k: comb[i].get(k, 0) * subject_grade_.get(k, 0)
        for k in set(comb[i]) & set(subject_grade_)
    }
    return sum(weighted_vals.values()) / sum(comb[i].values())


def get_maximum_score(filtered_comb_, subject_grade_):
    best_ = filtered_comb_[0]
    min_dist = np.Inf
    best_score = 0
    best_calibrated_ = filtered_comb_[0]
    # compute best score
    for comb in filtered_comb_:
        poli_first_block = block_score(comb, subject_grade_, 0) * 1.8
        poli_second_block = block_score(comb, subject_grade_, 1) * 1.8

        score = round(poli_first_block) + round(poli_second_block)

        if score > best_score:
            best_score = score
            best_ = comb
    # compute the best calibrated score
    for comb in filtered_comb_:
        poli_first_block = block_score(comb, subject_grade_, 0) * 1.8
        poli_second_block = block_score(comb, subject_grade_, 1) * 1.8

        dist = np.abs(poli_first_block - poli_second_block)
        score = round(poli_first_block) + round(poli_second_block)
        if score == best_score and dist < min_dist:
            min_dist = dist
            best_calibrated_ = comb

    return best_, best_calibrated_


def print_blocks(blocks, subject_grade_):
    print("===============================================")
    print("FIRST BLOCK")
    for key, value in blocks[0].items():
        print(key)
    weighted_sum = {k: blocks[0].get(k, 0) * subject_grade_.get(k, 0) for k in set(blocks[0]) & set(subject_grade_)}
    first_block = sum(weighted_sum.values()) / sum(blocks[0].values())
    print("===============================================")
    print("EURECOM average: ", first_block)
    print("Poli average: ", first_block * 1.8, ", which round up to: ", round(first_block * 1.8))
    print("===============================================")
    print("===============================================")
    print("SECOND BLOCK")
    for key, value in blocks[1].items():
        print(key)
    second_weighted_sum = {k: blocks[1].get(k, 0) * subject_grade_.get(k, 0) for k in
                           set(blocks[1]) & set(subject_grade_)}
    second_block = sum(second_weighted_sum.values()) / sum(blocks[1].values())
    print("===============================================")
    print("EURECOM average: ", second_block)
    print("Poli average: ", second_block * 1.8, ", which round up to: ", round(second_block * 1.8))
    print("===============================================")


if __name__ == '__main__':
    # {<subject_name> : <ects_weight>} !!!attenzione, la somma dei crediti deve essere 50!!!
    subject_weight = {'clouds': 5, 'malis': 5, 'dbsys': 5, 'stats': 2.5, 'quantis': 2.5, 'optim': 2.5,
                      'aml': 2.5, 'improc': 2.5, 'semproj': 10, 'asi': 5, 'deep': 2.5, 'malcom': 5}
    # {<subject_name> : <grade>} !!!attenzione, inserisci i voti in ventesimi!!!
    subject_grade = {'clouds': 0, 'malis': 0, 'dbsys': 0, 'stats': 0, 'quantis': 0, 'optim': 0,
                     'aml': 0, 'improc': 0, 'semproj': 0, 'asi': 0, 'deep': 0, 'malcom': 0}
    credits_per_block = 25
    all_combinations = []
    subset_sum(subject_weight, credits_per_block, res=all_combinations)
    filtered_comb = get_disjoint_two_set(all_combinations)
    best, best_calibrated = get_maximum_score(filtered_comb, subject_grade)
    print("The best arrangement is:")
    print_blocks(best, subject_grade)
    print("The best calibrated arrangement is:")
    print_blocks(best_calibrated, subject_grade)
