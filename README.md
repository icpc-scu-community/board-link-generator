# Board link generator
Board generator is a script for generating board's link for your custom data. <br>
Currently, our board requires a specific queryString variable `configs` with custom groups' and trainees' data. <br>
The main purpose of the script is to automate the process of creating json from your data, uploading json data to jsonbin, and shorten the board's link!

# Usage
### Required data
You are required to insert two files, and one optional parameters.
- `data/groups.txt`
- `data/trainees.csv` 

groups file must contain the full links of the sheets you want to add. <br>
trainees file must contain two columns with names (first row) and handles (second row) for each trainee using csv format.

### Optional parameters
If you want to automate the process even further, you can add three keys inside .env file

In order to do this process you have to install python-dotenv using the following command(s)
```
sudo apt install python3-pip
pip install python-dotenv
```

Create your .env file and add the following keys
- `jsonbin_api_key` to upload the json data.
- `cuttly_api_key` to shorten the final link with your custom slashtag.

You can get your jsonbin api key from [jsonbin api dashboard](https://jsonbin.io/api-keys) after logging in. <br>
You can get your cuttly api key from [cuttly dashboard](https://cutt.ly/edit) after logging in and click generate token. <br>

### Output
The output will be in one or two files
- `board.json` contains the json data
- `links.txt` contains all links (if api keys are applied) 

<p align="center">
  <img src="https://i.ibb.co/fXNmvsw/Parser.png" />
</p>

## Changelog
### v1.1
Including slashtag feature by using cuttly api instead of bitly.

### v1.0
First release using jsonbin and bitly for link shorten.
