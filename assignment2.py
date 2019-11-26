import numpy as np
def bootrep(data, func):
    return func(np.random.choice(data, size=len(data)))
def draw_bs_reps(data, func, size=1):
    bs_reps = np.empty(shape=size)
    for i in range(size):
        bs_reps[i] = bootrep(data, func)
    return bs_reps

if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('gandhi_et_al_bouts.csv', skiprows=4)
    bout_len_wt = np.array(df[df.genotype == 'wt'].bout_length)
    bout_len_mut = np.array(df[df.genotype == 'mut'].bout_length)
    mean_wt = np.mean(bout_len_wt)
    mean_mut = np.mean(bout_len_mut)
    # Draw bootstrap replicates
    bs_reps_wt = draw_bs_reps(bout_len_wt, np.mean, size=10000)
    bs_reps_mut = draw_bs_reps(bout_len_mut, np.mean, size=10000)
    # Compute 95% confidence intervals
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
    # Print the results
    print("""
    wild type:  mean = {0:.3f} min. 
                confidence interval = [{1:.1f}, {2:.1f}] min.
    mutant:     mean = {3:.3f} min. 
                confidence interval = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))



