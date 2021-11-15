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
If you want to automate the process even further, you can add two keys inside .env file
- `jsonbin_api_key` to upload the json data.
- `bitly_api_key` to shorten the final link.

You can get your jsonbin api key from [here](https://jsonbin.io/api-keys). <br>
You can get your bitly api key from [here](https://app.bitly.com/settings/api/) and click generate token. <br>

### Output
The output will be in one or two files
- `output/output.json` contains the json data
- `output/links.txt` contains all links (if api keys are applied inside .env)

