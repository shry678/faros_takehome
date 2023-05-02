# GitHub Analyzer Project

This project creates a Command Line Interface (CLI) that displays metrics for a specified GitHub user! The metrics are: total number of repositories, most frequently used programming language, most starred and forked repositories, and a user's weekly commit frequency.


## Set Up 
1. Start by **cloning this repository**. 

2. Create a personal token in GitHub, following these [instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). The access token authenticates your requests. Without an access token, you are heavily limited in requests (60 requests/hour). 

3. Open `metrics.py`. Update the `access_token` and `user` fields in this file with your own token and username.

4. Now, take a look at the technologies and dependencies required to successfully run the CLI locally!

### Requirements 
This project was developed with the following: 
| Technology | Version |
| ------------- | ------------- |
| Python | v3.10+  |
| Pip  | v23.1+  |


### Dependencies 
Run the following in command line to install the necessary dependencies:


```
pip install requests  
```
```
pip install prettytable
```
```
pip install matplotlib
```
```
pip install argparse
```
```
pip install colored
```


## Run 
Now that set up is complete, you can run the CLI! Follow these steps: 
1. Navigate to the cloned repository's directory in command line, if you haven't already done so.
2. Run the following script, entering in the GitHub username you would like to see metrics for. `github_username` is a required argument

```
python3 metrics.py <github_username>
```

#### Note: 
This CLI uses `argparser`. To see the acceptable arguments and their descriptions, run the following command with the 'help' flag: 
```
python3 metrics.py -h
```
As you will see from the output, the CLI also accepts two optional flags: 

` --save` : optional flag to save data retrieved in JSON file

`--gr` : optional flag to generate and save graph images




## Test
Try running the script with different usernames and the optional parameters. 

Cases to try: 
-  Run the script with a GitHub username that does not exist. You should expect to see a 404 Error message in command line.
-  Run the script with a username that has many repositories (i.e. user: `postmodern`) and save the graph images generated. You should expect to see 4 graph images saved as .png's in the project directory!  


Unit tests are written in `test_metrics.py`. The unit tests compare the actual API responses to mock JSON data. 
Run the following command to run the tests: 
```
python3 -m unittest test_metrics.py
```


## Helpful Links
- [Endpoints Available for GitHub Apps](https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps?apiVersion=2022-11-28) - this documentation gives you an idea of requests you can make

- [PrettyTable Library](https://pypi.org/project/prettytable/) - library used to print ASCII tables

- [MatPlotLib Library](https://pypi.org/project/matplotlib/) - library that creates visualization, like various graphs

- [ArgsParse](https://docs.python.org/3/library/argparse.html) - parser for command-line options and arguments

- [Colored Library](https://pypi.org/project/colored/) - library used for color and formatting in command line



