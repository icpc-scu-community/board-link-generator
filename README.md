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

you should run this order to automate the process
- `pip install python-dotenv`

- `jsonbin_api_key` to upload the json data.
- `rebrandly_api_key` and `rebrandly_workspace_id` to shorten the final link with your custom slashtag.

You can get your jsonbin api key from [here](https://jsonbin.io/api-keys). <br>
You can get your rebrandly api key from [here](https://app.rebrandly.com/account/api-keys) and click generate token. <br>
You can get your rebrandly workspace id from [here](https://developers.rebrandly.com/reference/list-workspaces-endpoint) put your api_key and click the button to get your workspace id. <br>

### Output
The output will be in one or two files
- `output/output.json` contains the json data
- `output/links.txt` contains all links (if api keys are applied) 

<p align="center">
  <img src="https://i.ibb.co/fXNmvsw/Parser.png" />
</p>
