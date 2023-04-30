# GitHub Analyzer Project

This project creates a Command Line Interface (CLI) that displays relevent metrics related to a GitHub user! The displayed metrics are total number of repositories, most frequently used programming language, most starred and forked repositories, and a user's weekly commit frequency.


## Set Up 
After **cloning this repository**, take a look at the technologies and dependencies required to successfully run the CLI locally. 

### Requirements 
This project was developed with the following: 
| Technology | Version |
| ------------- | ------------- |
| Python | v3.10+  |
| Pip  | v23.1+  |


### Dependencies 
Run the following in command line to install the necessary dependencies 

Needed to send HTTP requests using Python
```
pip install requests  
```

```
pip install numpy
```

```
pip install pandas
```

PrettyTable allows us to display data in ASCII table
```
pip install prettytable
```

```
pip install matplotlib
```

```
pip install termplotlib
```

```
pip install plotext
```




## Run 
Now that set up is complete, you can run the CLI! Follow these steps: 
1. Open command line 
2. In command line, navigate to the cloned repository directory 
3. Run the following script, entering in the GitHub username you would like to see metrics for: 

```
python3 metrics.py <github_username>
```

#### Note: 
This CLI uses argparser to take in arguments. To see the possible arguments it will take, run the following: 
```
python3 metrics.py -h
```



## Test



## Helpful Links



Code Documentation 