# Board link generator

- Board generator is a script for generating board's link for your custom data.
- Currently, our board requires a specific queryString variable `configs` with custom groups' and trainees' data.
- The main purpose of the script is to automate the process of creating json from your data, uploading json data to jsonbin, and shorten the board's link!

## Usage

### Required data

You are required to insert two files, and one optional parameters.

- `data/groups.txt`
- `data/trainees.csv`

groups file must contain the full links of the sheets you want to add.

trainees file must contain two columns with names (first row) and handles (second row) for each trainee using csv format.

### Optional parameters

If you want to automate the process even further, you can add two keys inside .env file

In order to do this process you have to install python-dotenv using the following command(s)

```bash
sudo apt install python3-pip
pip install python-dotenv
```

Create your .env file and add the following keys

- `jsonbin_api_key` to upload the json data.
- `cuttly_api_key` to shorten the final link with your custom slashtag.
- `jsonbin_bin_id` to update the json data (optional).

**if you leave `jsonbin_bin_id` empty, the script will create a new bin for you.**

### How to get the API keys

You can get your jsonbin api key from [jsonbin api dashboard](https://jsonbin.io/api-keys) after logging in.

You can get your cuttly api key from [cuttly dashboard](https://cutt.ly/edit) after logging in and click generate token.

### Output

The output will be in one or two files

- `board.json` contains the json data
- `links.txt` contains all links (if api keys are applied)

![Demo Picture](https://i.ibb.co/x8jpHRf/Terminal.png)

## Changelog

## [v1.2](https://github.com/icpc-scu-community/board-link-generator/tree/v1.2)

In this version we added the ability to:

- update the jsonbin bin with the new data.
- Asks first to create shorten Link or not.

### [v1.1](https://github.com/icpc-scu-community/board-link-generator/tree/v1.1)

Including slashtag feature by using cuttly api instead of bitly.

### v1.0

First release using jsonbin and bitly for link shorten.
