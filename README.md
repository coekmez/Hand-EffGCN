# Efficient Graph Convolutional Network (EfficientGCN) (ResGCNv2.0)

## 1 Paper Details
Project based on the paper below:

Yi-Fan Song, Zhang Zhang, Caifeng Shan and Liang Wang. **EfficientGCN: Constructing Stronger and Faster Baselines for Skeleton-based Action Recognition**. Submitted to IEEE T-PAMI, 2021. [[Arxiv Preprint]](https://arxiv.org/pdf/2106.15125.pdf)

Source EfficientGCN code (which is sadly no longer hosted on GitHub): [[Gitee]](https://gitee.com/yfsong0709/EfficientGCNv1)

## 2 Prerequisites

### 2.1 Libraries

This code is based on [Python3](https://www.anaconda.com/) (anaconda, >=3.5) and [PyTorch](http://pytorch.org/) (>=1.6.0). 

Use of conda environments are strongly recommended due to possible dependency issues caused by CUDA. Make sure to install the necessary CUDA version to make use of your GPU capabilities.

Other Python libraries are presented in the **'scripts/requirements.txt'**, which can be installed by 
```
pip install -r scripts/requirements.txt
```


### 2.2 Experimental Dataset

Our models are experimented the HoloLens recordings which can be found under **scripts/non-processed data**

It is then converted to the NTU dataset format. For comparison, please refer to: [GitHub](https://github.com/shahroudy/NTURGB-D)

### 2.3 Pretrained Models

Several pretrained models are provided, under the **workdir** folder. However, it is recommended to start a new training from scratch since that folder contains all previous checkpoints as well. A full training session of 70 epochs are expected to take around 15 minutes with the provided dataset.


## 3 Parameters

Before training and evaluating, there are some parameters should be noticed.

* (1) **'--config'** or **'-c'**: The config of EfficientGCN. You must use this parameter in the command line or the program will output an error. There are 4 configs given in the **configs** folder, which can be illustrated in the following tabel.

| config             | 2000      | 2001           | 3000      | 3001           |
| :----------------: | :-------: | :------------: | :-------: | :------------: |
| left or rigth hand | left only | left and right | left only | left and right |
| normalization      | yes       | yes            | no         | no            |


* (2) **'--work_dir'** or **'-w'**: The path to workdir, for saving checkpoints and other running files. Default is **'./workdir'**.

* (3) **'--resume'** or **'-r'**: Resume from the recent checkpoint (**'<--work_dir>/checkpoint.pth.tar'**).

* (4) **'--evaluate'** or **'-e'**: Only evaluate models. You can choose the evaluating model according to the instructions.

* (5) **'--extract'** or **'-ex'**: Extract features from a trained model for visualization. Using this parameter will make a data file named **'extraction_<--config>.npz'** at the **'./visualization'** folder.

* (6) **'--visualization'** or **'-v'**: Show the information and details of a trained model. You should extract features by using **<--extract>** parameter before visualizing.

* (7) **'--iterations'** or **'-it'**: Determine for how many iterations the whole training session will run. Used only in **benchmarking.sh** in order to measure the mean accuracy of a given configuration and its standard deviation.

Other parameters can be updated by modifying the corresponding config file in the **'configs'** folder.


## 4 Running

### 4.1 Modify Configs

Firstly, you should modify the **'path'** parameters in all config files of the **'configs'** folder.

A python file **'scripts/modify_configs.py'** will help you to do this. You need only to change three parameters in this file to your path to NTU datasets.
```
python scripts/modify_configs.py --path <path/to/save/numpy/data> --ntu60_path <path/to/processed/dataset> --work_dir <path/to/work/dir>
```
All the commands above are optional. The code should work as it is right after cloning. 

### 4.2 Generate Datasets

The non-processed HoloLens data is found under **scripts/non-processed data**. In case there are any new additions to the dataset recorded by the HoloLens, name the new recording folder in a similar format with the existing folders. Then, run the script **'scripts/convert_data_new.py'**. This will convert HoloLens data to the NTU format in a folder named **data** in the root directory.

To generate the numpy dataset after converting them from the HoloLens format, you can generate numpy data for one benchmark by the following command (only the first time to use this benchmark).
```
python main.py -c <config> -gd
```
where `<config>` is the config file name in the **'configs'** folder, e.g., 2001.

### 4.3 Train

You can simply train the model by 
```
python main.py -c <config>
```
If you want to restart training from the saved checkpoint last time, you can run
```
python main.py -c <config> -r
```

### 4.4 Evaluate

Before evaluating, you should ensure that the trained model corresponding the config is already existed in the **<--pretrained_path>** or **'<--work_dir>'** folder. Then run
```
python main.py -c <config> -e
```

### 4.5 Visualization

To visualize the details of the trained model, you can run
```
python main.py -c <config> -ex -v
```
where **'-ex'** can be removed if the data file **'extraction_`<config>`.npz'** already exists in the **'./visualization'** folder.


## 5 Results

Top-1 Accuracy for the 3 action dataset.

| configs | Mean accuracy  | Standard deviation | 
| :-----: | :------------: | :----------------: |
| 2000    | 83%            | 7.14%              |
| 2001    | 78%            | 9.05%              |  
| 3000    | 82%            | 11.56%             | 
| 3001    | 89%            | 2.75%              |

Top-1 Accuracy for the 4 action dataset.

| configs | Mean accuracy  | Standard deviation | 
| :-----: | :------------: | :----------------: |
| 2000    | 61%            | 9.17%              |
| 2001    | 81%            | 2.49%              |  
| 3000    | 71%            | 10.67%             | 
| 3001    | 70%            | 2.65%              |

For benchmarking, run **'benchmarking.sh'** which will train and evaluate each model 20 times and save the mean and standard deviation in a file called **results.txt**

## 6 Citation and Contact

If you have any questions regarding the setup or the code itself, please send an e-mail to `mcoekmez@student.ethz.ch`.
