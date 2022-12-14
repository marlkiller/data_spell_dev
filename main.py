"""
pip3 install jupyter
pip3 install pandas
pip3 install matplotlib

[root@ip-172-26-9-224 data_spell_dev]# find  / -name jupyter
/opt/rh/rh-python38/root/usr/local/bin/jupyter
/opt/rh/rh-python38/root/usr/local/etc/jupyter
/opt/rh/rh-python38/root/usr/local/share/jupyter

export PATH=$PATH:/opt/rh/rh-python38/root/usr/local/bin



# 生成配置文件
jupyter notebook --generate-config
Writing default config to: /root/.jupyter/jupyter_notebook_config.py


    修改端口 c.NotebookApp.port = 8888
    修改可连接的服务器 c.NotebookApp.ip='*'

# 设置密码
jupyter notebook password

# 启动项目
jupyter notebook --allow-root
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root


# convert
ln -s  /opt/homebrew/share/jupyter  /Users/artemis/Library/Python/3.10/share/jupyter
jupyter nbconvert --to markdown jupyter_dev.ipynb

"""
if __name__ == '__main__':
    import pandas as pd

    result = pd.read_csv("account_clean.csv")
    group = result.groupby("Status").mean()
    print(group)

