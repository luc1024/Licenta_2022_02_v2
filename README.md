## The Problem
A large amount of **_"items"_** - questions along with answer choices, was collected through a Google Form. The data collection spreadsheet looks like the sample file in the `fake_samples` folder.
From these entries, assignments had to be generated for the students, each containing 7 questions, randomly chosen based on an algorithm.
These assignments then had to be saved separately in a PDF file formatted in two columns and landscape. Also, for each assignment, the solution was saved in a separate PDF file.
There were several examination boards and several examination days. Each board received a ZIP file each day containing a pre-determined number of assignments and their solutions.

## The Algorithm
The courses were divided into 4 categories. 
From the first category, 4 items from 4 different courses had to be randomly selected.
From each of the other 3 categories only one item was chosen.

The special requirement was that the distribution of the frequency of occurrence of the items in assignments should be as uniform as possible (i.e. there should not be some questions that occur very often and others that occur very rarely). The item frequency file in the `fake_samples` folder is presented as evidence that this requirement has been met to the maximum extent possible.

## (Fake) Sample Data in `fake_samples` Folder
| File name                                                      | Description                                                                                                                                                                                                         |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fake_sample_input.xlsx`                                       | A file that looks like the original input Google Spreadsheet data collection file from Google Form. Sensitive data has been replaced with fake data. The number of items is real.                                   |
| `fake_Assignment_LK_03.pdf`                                    | A sample file of what an assignment file looks like. Sensitive data has been replaced with fake data.                                                                                                               |
| `fake_Solution_LK_03.pdf`                                      | A sample file of what an solution file looks like. Sensitive data has been replaced with fake data.                                                                                                                 |
| `fake_Assignments & Solutions, Board 11, Luni, 14.02.2022.zip` | A sample of what a ZIP file for the exam board looks like. Sensitive data has been replaced with fake data.                                                                                                         |
| `fake_items.json`                                              | This is a file used to load items locally. Its use is indicated in the section _[How to run the project with fake data](#how-to-run-the-project-with-fake-data)_.  Sensitive data has been replaced with fake data. |
| `(real)_frecvente_itemi.xlsx`                                  | This file contains _real_ data about the item _frequency_ distribution for 2 exam days, 11 boards and 32 items per board per day (which happened in the summer sessions during the COVID pandemic).                 |


## Requirements
This project needs Microsoft Word in order to convert DOC files to PDF.

If the Word application is not present on the host machine, the output will consist of ZIPs of DOC files instead of PDFs.
## How to run the project with fake data
```
git clone https://github.com/luc1024/Licenta_2022_02_v2.git
cd Licenta_2022_02_v2
pip install -r requirements.txt
cp fake_samples/fake_items.json secret/items.json
cp .env-example .env
```
Then edit the `.env` file, and set
```
GET_FROM_LOCAL_FILE = TRUE
```

Run it with
```
python main.py
```

That's all.