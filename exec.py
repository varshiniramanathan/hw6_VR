import pandas as pd
import convert_matrices

if __name__ == '__main__':
    ## USER MUST CHANGE THE FOLLOWING THREE LINES ###
    txt_dir = '/Users/varshiniramanathan/Documents/20.440'
    DP_HiC = 'GSE79422_DP_KZ621KZ761GA9929GA9930GA9932.Bin1kMin1kMax2000m.sbsmp.iii.genWashU.sort.txt'
    HSC_HiC = 'GSE79422_HSC_KZ614KZ757GA9757.Bin1kMin1kMax2000m.sbsmp.iii.genWashU.sort.txt'

    # Read in Hi-C data
    DP_lr = pd.read_csv(f"{txt_dir}/{DP_HiC}", sep = '\t', names=["chr", "start", "end", "info", "id", "dir"])
    HSC_lr = pd.read_csv(f"{txt_dir}/{HSC_HiC}", sep = '\t', names=["chr", "start", "end", "info", "id", "dir"])

    # Format and process data
    # User may change these lines if visualizing differently
    DP_chr17 = convert_matrices.make_matr_chr(DP_lr, 'chr17')
    HSC_chr17 = convert_matrices.make_matr_chr(HSC_lr, 'chr17')

    # Plot Data
    # User may change these lines if visualizing differently
    names = ['HSC chr17', 'DP chr17']
    all_matr = [HSC_chr17, DP_chr17]
    convert_matrices.plot_matr(all_matr, names)