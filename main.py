"""
pip3 install jupyter
pip3 install pandas
pip3 install matplotlib
"""
if __name__ == '__main__':
    import pandas as pd

    result = pd.read_csv("account_clean.csv")
    group = result.groupby("Status").mean()
    print(group)

